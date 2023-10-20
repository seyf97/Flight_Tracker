from datetime import datetime, timedelta


class FlightData:
    """This class is responsible for structuring the flight data"""

    def __init__(self, flight):
        date_from = flight["local_departure"].split("T")[0]
        date_from_obj = datetime.strptime(date_from, "%Y-%m-%d")
        date_to = (date_from_obj + timedelta(int(flight["nightsInDest"]))).strftime("%Y-%m-%d")

        self.msg = f'Low price alert! Only {flight["price"]}eur to fly from ' \
              f'{flight["cityFrom"]}-{flight["cityCodeFrom"]} to {flight["cityTo"]}-' \
              f'{flight["cityCodeTo"]} from {date_from} to ' \
              f'{date_to}.'
