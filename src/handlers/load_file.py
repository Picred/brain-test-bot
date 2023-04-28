"""Load file module"""
from telegram.ext import CallbackContext
from src.data.costanti import LIVELLO, CATEGORIA
import json


def load_file(context: CallbackContext) -> dict:
    """Loads a file from a path.

    Args:
        context: context passed by the handler
    
    Returns:
        the loaded file
    """
    match context.user_data[LIVELLO]:
        case "1: Facile":
            path = 'facile.json'
        case "2: Intermedio":
            path = 'intermedio.json'
        case "3: Difficile":
            path = 'difficile.json'

    with open(f'src/data/{path}', 'r', encoding="utf-8") as f:
        data = json.load(f)[f"{context.user_data[CATEGORIA]}"]

    return data
