################################################################################
################################################################################
import json
import schedule
import time
import logging
import logging.config
from datetime import date

from last import get_recent_tracks
from top import get_top_tracks
import conf

################################################################################
# Main variables
################################################################################
SCHEDULED_TASK_DELAY = 60  # Sec
USERNAME = conf.USERNAME

logger = logging.getLogger('main_logging')

################################################################################
# Functions
################################################################################
################################################################################
# name:        update_info
# description: 
################################################################################
def update_info():
    """

    """
    logger.info("update_info: Start")
    get_recent_tracks(USERNAME, 15)
    get_top_tracks(USERNAME, 15)

################################################################################
# name:        scheduled_task
# description: Task for scheduled routine
################################################################################
def scheduled_task():
    """
    Scheduled task
    """
    schedule.every(2).hours.do(update_info)
    logger.info("scheduled_task: Start")
    while True:
        logger.info("scheduled_task: while")
        schedule.run_pending()
        time.sleep(SCHEDULED_TASK_DELAY)

################################################################################
# Main
################################################################################
def main():
    """
    Main
    """
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.basicConfig(filename='log.log')
    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(encoding='utf-8')

    logger.setLevel(logging.DEBUG)
    logger.info("Starting LASTFM BOT")
    scheduled_task()


if __name__ == "__main__":
    main()
