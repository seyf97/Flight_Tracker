from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


# Create instances of the classes
data_manager = DataManager()
flight_search = FlightSearch()

# Get cities
cities = data_manager.get_cities()

# Get IATA codes
codes = flight_search.get_iata_code(cities)

# Fill IATA codes in Google Sheets
data_manager.put_iata_codes(codes)

# Get min prices for flights
prices = data_manager.get_prices()

# Get cheapest available flights for cities
flights = flight_search.get_flights()

# For each city, compare the prices with our initial limit
for i in range(len(cities)):
    print(f'Min price: {flights[i]["price"]}eur')
    if (flights[i]["price"]) < prices[i]:  # If we find a cheaper price
        # Collect data about the flight and create a message string
        flight_data = FlightData(flights[i])
        # Send sms to the client with the created string
        notification = NotificationManager(flight_data.msg)

