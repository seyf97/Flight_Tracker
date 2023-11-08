# Flight_Tracker
Tracks flights from google docs to see if there's a cheaper flight.

The document: https://docs.google.com/spreadsheets/d/1jUyN6Koa4EH4F2rLjUcaolG7IO4wGzbZgQ0kxgB2NnA/edit?usp=sharing

Users edit the city name and the minimum cost they desire. 

Using Sheety API, the program first reads the city names from the sheet. Then, it finds the relevant IATA codes and fills the sheets.
After this, using the Kiwi API, the program goes through available flights and finds the cheapest return ticket.
If the price is lower than the one stated on google sheets, the user is notified with an SMS via the Twilio API.


Example:
![image](https://github.com/seyf97/Flight_Tracker/assets/111386377/d4d25c54-7953-4bb7-be39-42102171b48b)
