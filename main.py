import time

from logger import Logger
from bot import MargonemBot
from settings import  NPC_TO_LOCATE, SERVER

if __name__ == '__main__':
    try:
        event_logger = Logger()
        margonem_bot = MargonemBot(NPC_TO_LOCATE, SERVER, event_logger)
        margonem_bot.open_game()
        time.sleep(5)
        while True:
            margonem_bot.hunt_npc()
    except Exception as e:
        print(f"Error: {e}")