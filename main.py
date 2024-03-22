import os
import sentry_sdk
import logging
from sentry_sdk import add_breadcrumb

from dotenv import load_dotenv, dotenv_values
from controller.start_menu_controller import StartMenuController

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


load_dotenv()
# print('env:', os.getenv("DB_PASS"), os.getenv("DB_USER"))

def main():

    ###### SENTRY ######
    """sentry_sdk.init(
    dsn="https://1f514c6dc8b9839a67a308611eb041fe@o4506869492940800.ingest.us.sentry.io/4506869497069568",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    )"""
    ##### END SENTRY #####
    
    # logging.error("I am an event", extra=dict(bar=43))
    # logging.exception("An exception happened")
    logging.debug("Program is starting!")
    print('Repertoire de base: ', os.getcwd(),'\n')
    main_app = StartMenuController()
    main_app.start_dbepic_app()
    # logging.info("Program end!")



if __name__ == "__main__":
    main()