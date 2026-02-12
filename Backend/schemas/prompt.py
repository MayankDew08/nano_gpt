from typing import Optional
from pydantic import BaseModel

class Prompt(BaseModel):
    text: Optional[str] = None
    new_tokens: Optional[int] = None  # If None, will randomly select from predefined options