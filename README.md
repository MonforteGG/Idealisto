# 🏠 Idealisto Telegram Bot

This Python project automates the retrieval of housing listings from Idealista and saves only new listings to a local SQLite database (no server required). It compares the price per square meter to the average of previously stored listings and sends notifications to a Telegram group with the most relevant information, including new listings and price changes.

![Telegram_screenshots](https://i.imgur.com/y07o3yI.png)

## 🚀 Features

- **Automated listing retrieval** for properties in your area using the Idealista API.
- **New listing verification**: Only saves listings that are not already in the database.
- **Price per m² comparison** with the average price from previously stored listings.
- **Price change notifications**: Alerts you when there are changes in the prices of existing listings.
- **Formatted notifications** with the most important details of the listing.


## 🔄 Work Flow

1. **Retrieve data from Idealista API**: Call the Idealista API and store the obtained JSON.
2. **Get existing property codes and prices**: Fetch all property codes and prices from the database.
3. **Process each property**:
   - If the property is new, send a notification for the new listing and add it to the database.
   - If the property is not new, check if the price has changed. If it has, send a price change notification and update the price in the database.

## 🛠 Technologies Used

- **Python** for the backend and program logic.
- **SQLite** for local data storage.
- **SQLAlchemy** for database interaction.
- **Idealista API** for retrieving property listings.
- **Telegram Bot API**: for sending notifications and updates.
- **Task automation** using cron on Linux or Task Scheduler on Windows.


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
│   ├── conection.py   # Handles the connection to the SQLite database.
│   ├── model.py       # SQLAlchemy database model definition.
│   └── queries.py      # SQLAlchemy queries and database operations.
└── README.md          # Project documentation.
```

## 📋 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/MonforteGG/idealisto.git
    cd idealisto
    ```

2. Create a virtual environment and activate it (Recommended):
   ```bash
   python -m venv venv
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

   On Linux:
   ```bash
   source venv/bin/activate
   ```



3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables for your Idealista API connection and SQL database. Create a `.env` file in the root directory and add your credentials:
    ```env
    IDEALISTA_API_KEY=your_idealista_api_key
    IDEALISTA_CLIENT_SECRET=your_idealista_client_secret
    TELEGRAM_TOKEN=your_telegram_bot_token
    TELEGRAM_GROUP_ID=your_telegram_group_id
    ```

5. Adapt parameters.py:
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

6. Run the bot:
    ```bash
    python bot.py
    ```

## ⚙️ Automated Tasks

To execute the task 2 times a day (15:00, 20:00):

On Linux, set up cron:

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following lines:
   ```bash
   00 15 * * * . /home/your_username/Idealisto/venv/bin/activate && python3 /home/your_username/Idealisto/main.py >> /home/your_username/Idealisto/cron.log 2>&1
   00 20 * * * . /home/your_username/Idealisto/venv/bin/activate && python3 /home/your_username/Idealisto/main.py >> /home/your_username/Idealisto/cron.log 2>&1
   ```
   > ❗ **Warning**: Replace `your_username` with your actual username on your system.
   
   > ⏰ **Reminder**: Check your system date and time and adjust the hours (15:00 and 20:00) to match your local time zone.


   

On Windows, use Task Scheduler:

1. Open Task Scheduler.
2. Create a new task that runs the following command:
   ```bash
   path\to\venv\Scripts\python.exe path\to\Idealisto\main.py
   ```
3. Set the trigger to run the task at the 15:00 and 20:00 every day.



## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

If you have any questions or suggestions, feel free to contact me at [albdiamun@gmail.com](mailto:albdiamun@gmail.com).
