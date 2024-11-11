## BeachBuddy
BeachBuddy is a web application designed to help beachgoers by providing real-time data on ocean and weather conditions, allowing users to make informed decisions about recreational activities at their favorite beaches. The app leverages oceanographic and meteorological data from the INCOIS and OpenWeatherMap APIs to ensure accurate, location-based insights.

 ## Features

- **Location-based Alerts**: Receive notifications about current beach conditions.
- **Beach Explorer**: Discover beaches based on location, and see real-time data.
- **Safety Guidelines**: Access up-to-date beach safety information.
- **Geospatial Visualizations**: Visualize data to make beach-going decisions.
  
## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **APIs**: INCOIS
- **Data Processing**: JSON files for beach data storage and retrieval

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bhavilavajhalla/beachbuddy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd beachbuddy
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up API keys for INCOIS and OpenWeatherMap.

5. Run the application:
   ```bash
   flask run
   or
   Use live server extension on vscode
   ```

## Usage

1. Open your browser and go to `http://localhost:5000`.
2. Use the Explore page to search for beaches and view real-time data.
3. Refer to the Safety Guidelines page for helpful information.

## Project Structure (not yet done)

- **app/**: Contains the main application files.
- **static/**: Static assets (CSS, JavaScript).
- **templates/**: HTML files for frontend views.
- **data/**: JSON files for beach data storage.
  
## Future Improvements

- Integrate additional weather and ocean condition data sources.
- Improve search functionality on the Explore page.
- Enhance UI/UX for a more user-friendly experience.

## Contributing

Contributions are welcome! Please create an issue or pull request to discuss any improvements or features.
