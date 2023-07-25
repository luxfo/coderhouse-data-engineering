from utils import logger
from etl import pipeline

def main():
    try:
        logger.info('Started')
        pipeline.etl()
        logger.info('Finished')
    except Exception as err:
        logger.exception(err)

# starting the app
if __name__ == "__main__":
    main()

