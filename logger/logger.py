import sys
import logging
import telebot
from logging import StreamHandler, Handler, \
    Formatter, LogRecord

bot = telebot.TeleBot("5371849568:AAHCnnUNQ-DvgX7jFDKCvwA43lXlJmsNR2c")


class TelegramBotHandler(Handler):

    def __init__(self, token: str):

        super().__init__()
        self.token = token
        self.bot = bot

    def emit(self, record: LogRecord):

        for chat_id in ["1499730239", "459484043"]:
            self.bot.send_message(
                chat_id,
                self.format(record)
            )


class Logger():

    def __init__(self):

        logger = logging.getLogger("my_logger")
        logger.setLevel(logging.ERROR)

        telegramBotHandler = TelegramBotHandler()
        telegramBotHandler.setFormatter(
            fmt='[%(asctime)s: %(levelname)s] %(message)s')
        handler = StreamHandler(stream=sys.stdout)
        handler.setFormatter(
            Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        logger.addHandler(handler)
        logger.addHandler(TelegramBotHandler)

        self.logger = logger


logger = Logger().logger
logger.debug('sd')
logger.error('sasd')
