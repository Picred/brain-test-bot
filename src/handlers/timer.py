from telegram.ext import CallbackContext


def timer(context: CallbackContext) -> None:
    args = context.job.context
    from src.handlers.risposta import risposta_vuota
    risposta_vuota(args[0],args[1],args[2])
