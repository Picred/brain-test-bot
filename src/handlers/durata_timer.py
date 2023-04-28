""" Timer set"""
from telegram.ext import CallbackContext
from src.data.costanti import LIVELLO


def durata_timer(context: CallbackContext) -> int:
    """Sets the duration of the timer.

    Args:
        context: context passed by the handler
    
    Returns:
        the duration of the timer
    """
    match(context.user_data[LIVELLO]):
        case '1: Facile':
            return 10
        case '2: Intermedio':
            return 7
        case '3: Difficile':
            return 5
