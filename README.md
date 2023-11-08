# Flight_Tracker
Just enter where you'd like to fly and for how much in google sheets, and let the app send you an SMS once it finds a cheap flight in the next 3 months.

The document it reads from: https://docs.google.com/spreadsheets/d/1jUyN6Koa4EH4F2rLjUcaolG7IO4wGzbZgQ0kxgB2NnA/edit?usp=sharing

Users edit the city name and the minimum cost they desire. 

## Classes
**DataManager:** This class is responsible for talking to the Google Sheet.

**FlightSearch:** This class is responsible for getting IATA codes of cities and finding flights.

**FlightData:** This class is responsible for structuring the flight data

**NotificationManager:** This class is responsible for sending notifications with the deal flight details.


## Execution
1. Using Sheety API, the program reads the city names from the sheet. 
2. It finds the relevant IATA codes and fills the sheets.
3. Using the Kiwi API, the program goes through available flights and finds the cheapest return ticket.
4. If the price is lower than the one stated on google sheets, the user is notified with an SMS via the Twilio API.


Example:
![image](https://github.com/seyf97/Flight_Tracker/assets/111386377/d4d25c54-7953-4bb7-be39-42102171b48b)



