from logger import Logger
from bot import MargonemBot
from settings import  NPC_TO_LOCATE, SERVER, LOG_IN

if __name__ == '__main__':
    try:
        event_logger = Logger()
        margonem_bot = MargonemBot(NPC_TO_LOCATE, SERVER, event_logger)
        if LOG_IN:
            margonem_bot.go_to_main_page()
            margonem_bot.log_in()
        else:
            margonem_bot.open_game()
        while True:
            margonem_bot.hunt_npc()
    except Exception as e:
        print(f"Error: {e}")
        margonem_bot.logger.log_event(f"Critical Error: {e}")