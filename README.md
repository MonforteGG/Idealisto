# 🏠 Idealisto Telegram Bot

This Python project automates the retrieval of housing listings from Idealista and saves only new listings to a MySQL database. It compares the price per square meter to the average of previously stored listings and sends notifications to a Telegram group with the most relevant information, including new listings and price changes.

![Telegram_screenshots](https://i.imgur.com/y07o3yI.png)

## 🚀 Features

- **Automated listing retrieval** for properties in your area using the Idealista API.
- **New listing verification**: Only saves listings that are not already in the database.
- **Price per m² comparison** with the average price from previously stored listings.
- **Price change notifications**: Alerts you when there are changes in the prices of existing listings.
- **Formatted notifications** with the most important details of the listing.
- **Daily automation**: The program runs 3 times a day at 09:00, 15:00, and 20:00. (This is because the Idealista API only allows 100 queries per month.)

## 🛠 Technologies Used

- **Python** for the backend and program logic.
- **MySQL** for data storage.
- **SQLAlchemy** for database interaction.
- **Idealista API** for retrieving property listings.
- **Telegram Bot API**: for sending notifications and updates.
- **Task automation** using Python’s `schedule`.

## 🗂 Project Structure
```
Idealista/
├── .env               # Environment variables for API and DB configuration.
├── auth.py            # Authentication handling for Idealista API.
├── bot.py             # Main file to run the bot and listing checks.
├── main.py            # Entry point for the program execution.
├── parameters.py      # Search parameters for the Idealista API.
├── requirements.txt   # Python dependencies.
├── search.py          # Idealista API search implementation.
├── task.py            # Contains the recurring tasks scheduled for fetching listings.
├── utils.py           # Helper functions for data handling.
├── database/          # Database-related files.
│   ├── conection.py   # Handles the connection to the Azure MySQL database.
│   ├── model.py       # SQLAlchemy database model definition.
│   └── queries.py      # SQLAlchemy queries and database operations.
└── README.md          # Project documentation.
```

## 📋 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/youruser/idealisto.git
    cd idealisto
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables for your Idealista API connection and Azure database. Create a `.env` file in the root directory and add your credentials:
    ```env
    IDEALISTA_API_KEY=your_idealista_api_key
    IDEALISTA_CLIENT_SECRET=your_idealista_client_secret
    DB_HOST=your_database_host
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_NAME=your_database_name
    TELEGRAM_TOKEN=your_telegram_bot_token
    TELEGRAM_GROUP_ID=your_telegram_group_id
    ```

4. Adapt parameters.py:
    ```python
    base_url = 'https://api.idealista.com/3.5/'  # Base search URL
    country = 'es'  # Search country (es, it, pt)
    language = 'es'  # Search language (es, it, pt, en, ca)
    max_items = '50'  # Max items per call, the maximum set by Idealista is 50
    operation = 'sale'  # Kind of operation (sale, rent)
    property_type = 'homes'  # Type of property (homes, offices, premises, garages, bedrooms)
    order = 'publicationDate'  # Order of the listings
    center = '37.404762,-5.973923'  # Coordinates of the search center
    distance = '900'  # Max distance from the center
    sort = 'desc'  # How to sort the found items
    maxprice = '190000'  # Max price of the listings
    ```

5. Run the bot:
    ```bash
    python bot.py
    ```

## ⚙️ Automated Tasks

The program executes a task 3 times a day (09:00, 15:00, 20:00) with the following flow:

1. **Retrieve data from Idealista API**: Call the Idealista API and store the obtained JSON.
2. **Get existing property codes and prices**: Fetch all property codes and prices from the database.
3. **Process each property**:
   - If the property is new, send a notification for the new listing and add it to the database.
   - If the property is not new, check if the price has changed. If it has, send a price change notification and update the price in the database.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

If you have any questions or suggestions, feel free to contact me at [albdiamun@gmail.com](mailto:albdiamun@gmail.com).
