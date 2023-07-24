from utils import logger
from etl import pipeline

def main():
    logger.info('Started')
    pipeline.etl()
    logger.info('Finished')

# starting the app
if __name__ == "__main__":
    main()

