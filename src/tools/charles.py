import os
import logging
import schwabdev
from dotenv import load_dotenv
from time import sleep
import json
from datetime import datetime


def main():
    # place your app key and app secret in the .env file
    load_dotenv()  # load environment variables from .env file

    # warn user if they have not added their keys to the .env
    if len(os.getenv("app_key")) != 32 or len(os.getenv("app_secret")) != 16:
        raise Exception("Add you app key and app secret to the .env file.")

    # set logging level
    logging.basicConfig(level=logging.INFO)
    # create client
    client = schwabdev.Client(os.getenv("app_key"), os.getenv("app_secret"), os.getenv("callback_url"))

    # print("\nGet a list of quotes")
    # print(client.quotes(["AAPL", "AMD"]).json())
    # sleep(3)

    # print("\nGet a single quote")
    # print(json.dumps(client.quote("AAPL").json()))
    # sleep(3)

    print("\nGet price history")
    print(json.dumps(client.price_history("AAPL", periodType="day", period=1, frequencyType="daily",frequency=1,startDate=datetime.strptime("2025-03-20", "%Y-%m-%d"), endDate=datetime.strptime("2025-03-31", "%Y-%m-%d") ).json()))
    sleep(3)


if __name__ == "__main__":
    print("Welcome to Schwabdev, The Unofficial Schwab API Python Wrapper!")
    print("Documentation: https://tylerebowers.github.io/Schwabdev/")
    main()  # call the user code above
