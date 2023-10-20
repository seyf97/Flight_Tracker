import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.ENDPOINT_TEQUILA_LOCS = os.getenv("ENDPOINT_TEQUILA_LOCS")
        self.ENDPOINT_TEQUILA_SEARCH = os.getenv("ENDPOINT_TEQUILA_SEARCH")
        self.API_TEQUILA = os.getenv("API_TEQUILA")
        self.iata_codes = []
        self.FROM_IATA = "BUH"  # Bucharest IATA Code
        self.flights = []

    def get_iata_code(self, cities):
        """Gets iata code list for the input cities list"""
        for city in cities:
            resp = requests.get(
                url=self.ENDPOINT_TEQUILA_LOCS,
                params={
                    "term": city,
                    "locale": "en-US",
                },
                headers={
                    "apikey": self.API_TEQUILA
                }
            )
            resp.raise_for_status()
            self.iata_codes.append(resp.json()["locations"][0]["code"])
        return self.iata_codes

    def get_flights(self):
        for code in self.iata_codes:
            params_tequila_fly = {
                "fly_from": self.FROM_IATA,
                "fly_to": code,
                "date_from": (datetime.now()+timedelta(1)).strftime("%d/%m/%Y"),
                "date_to": (datetime.now()+timedelta(90)).strftime("%d/%m/%Y"),
                "return_from": (datetime.now()+timedelta(10)).strftime("%d/%m/%Y"),
                "return_to": (datetime.now() + timedelta(100)).strftime("%d/%m/%Y"),
                "nights_in_dst_from": 2,
                "nights_in_dst_to": 10,
                "limit": 500
            }
            headers_tequila = {
                "apikey": self.API_TEQUILA,
            }
            resp = requests.get(
                url=self.ENDPOINT_TEQUILA_SEARCH,
                params=params_tequila_fly,
                headers=headers_tequila
            )
            resp.raise_for_status()
            self.flights.append(resp.json()["data"][0])
        return self.flights

