from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import torch
from schemas import Prompt
import random
import os
import time
import logging
from dotenv import load_dotenv
import services.model_load as model_service

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="NanoGPT API", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    """Load model when the API starts"""
    logger.info("Starting NanoGPT API Server...")
    model_service.load_model_and_vocab()
    logger.info("Server startup complete!")

@app.get("/")
def read_root():
    return {
        "message": "API for NanoGPT is up and running!",
        "status": "online",
        "endpoints": {
            "generate": "/generate",
            "docs": "/docs"
        }
    }

@app.post("/generate")
async def generate_text(prompt: Prompt):
    # Start timing
    start_time = time.time()
    
    # Access model and functions from the loaded module (no re-import overhead)
    if model_service.model is None:
        logger.error("Model not loaded")
        return {"error": "Model not loaded. Please restart the server."}
    
    try:
        # Determine the number of tokens to generate
        if prompt.new_tokens is not None:
            max_tokens = prompt.new_tokens
        else:
            # Randomly select from predefined options
            max_tokens = random.choice(model_service.TOKEN_LENGTH_OPTIONS)
        
        logger.info(f"Generating {max_tokens} tokens")
        
        # Use empty string if no prompt provided
        input_text = prompt.text if prompt.text else ""
        
        # Encode the input prompt (using pre-loaded encode function)
        if input_text:
            context = torch.tensor([model_service.encode(input_text)], dtype=torch.long, device=model_service.device)
        else:
            # Start with a newline character if no prompt
            context = torch.zeros((1, 1), dtype=torch.long, device=model_service.device)
        
        # Generate text
        generation_start = time.time()
        with torch.no_grad():
            generated_indices = model_service.model.generate(context, max_new_tokens=max_tokens)
            generated_text = model_service.decode(generated_indices[0].tolist())
        generation_time = time.time() - generation_start
        
        # Calculate total response time
        total_time = time.time() - start_time
        
        logger.info(f"Generation completed in {generation_time:.2f}s, Total response time: {total_time:.2f}s")
        
        return {
            "prompt": input_text,
            "generated_text": generated_text,
            "tokens_generated": max_tokens,
            "total_length": len(generated_text),
            "generation_time_seconds": round(generation_time, 3),
            "total_response_time_seconds": round(total_time, 3)
        }
    
    except Exception as e:
        total_time = time.time() - start_time
        logger.error(f"Error during generation: {str(e)} (after {total_time:.2f}s)")
        return {
            "error": str(e),
            "total_response_time_seconds": round(total_time, 3)
        }
