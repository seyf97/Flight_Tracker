import requests
from dotenv import load_dotenv
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.ENDPOINT_SHEETY = os.getenv("ENDPOINT_SHEETY")

    def put_iata_codes(self, codes):
        """Puts the input codes list into the sheets"""
        idx = 2
        for code in codes:
            resp = requests.put(
                url=f"{self.ENDPOINT_SHEETY}/{idx}",
                json= {
                    "price": {
                        "iataCode": code
                    }
                }
            )
            resp.raise_for_status()
            idx += 1

    def get_cities(self):
        """Returns a list of cities"""
        resp = requests.get(self.ENDPOINT_SHEETY)
        resp.raise_for_status()
        return [row["city"] for row in resp.json()["prices"]]

    def get_prices(self):
        """Returns a list of prices"""
        resp = requests.get(self.ENDPOINT_SHEETY)
        resp.raise_for_status()
        return [row["lowestPrice"] for row in resp.json()["prices"]]
