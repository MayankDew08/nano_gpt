import os
import logging
import torch

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(lineno)d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Define token length options for random selection
TOKEN_LENGTH_OPTIONS = [500, 750, 1000, 1500, 2000, 2500]

# Get the path to the nano_gpt folder (parent of Backend folder)
BACKEND_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Backend folder
NANO_GPT_PATH = os.path.dirname(BACKEND_PATH)  # nano_gpt folder (one level up from Backend)
MODEL_PATH = os.path.join(NANO_GPT_PATH, 'model.pth')
INPUT_PATH = os.path.join(BACKEND_PATH, 'input.txt')

# Load vocabulary from training data ONCE at module import time
logger.info(f"Loading vocabulary from {INPUT_PATH}")
with open(INPUT_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

# Create character mappings ONCE
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

# Define encode/decode functions ONCE (these are now module-level, not recreated)
encode = lambda s: [stoi[c] for c in s]  # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l])  # decoder: take a list of integers, output a string

logger.info(f"Vocabulary loaded: {vocab_size} unique characters")

# Global variables for model
model = None
device = 'cuda' if torch.cuda.is_available() else 'cpu'

def load_model_and_vocab():
    """Load the trained model once at startup (vocab already loaded at module import)"""
    global model
    
    logger.info(f"Loading model from {MODEL_PATH}")
    
    # Import the model architecture (no training code executed - clean import)
    import sys
    sys.path.insert(0, BACKEND_PATH)
    from model import GPTLanguageModel
    
    # Instantiate model with the correct vocab size
    model = GPTLanguageModel(vocab_size=vocab_size)
    
    # Load the trained weights (pre-trained model.pth)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.to(device)
    model.eval()
    
    logger.info(f"Model loaded successfully - using pre-trained weights")
    logger.info(f"Device: {device}")