from game import *
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f'log/{__name__}.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def main():
    logger.info("Starting main function")
    try:
        
        board = Board(game_atts["board"])
        cursor = Cursor(randomizer())
        #terminal_Game(board, cursor)
        Pygame_init(board, cursor)
    except Exception as e:
        logger.error(f"Error in main: {e}", exc_info=True)
        raise
    finally:
        
        logger.info("Program end")


if __name__ == "__main__":
    main()
