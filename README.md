# Countries API New Wave Biotech Task Documentation

This API provides access to country information and a comparison service between two countries based on different criteria.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3.x

### Installing

To set up the development environment, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Create a Python virtual environment:
```bash
python3 -m venv venv
```
4. Activate the virtual environment:
    - On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```
    - On Windows (Command Prompt):
    ```bash
    venv\Scripts\activate
    ```
3. Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```
4. Start the Flask server:
```bash
python3 app.py
```

## Environment Setup

To run this application, you will need to set up environment variables to manage different configurations for development and production environments. This is done through the use of `.env`, `.env.development`, and `.env.production` files.

### Step 1: Create Environment Files

Create three files in the root directory of the project:

- `.env`
- `.env.development`
- `.env.production`

### Step 2: Configure `.env`

The `.env` file is used to specify the mode in which your application should run. You can set it to either `development` or `production` based on your current requirements.

**.env**
```plaintext
FLASK_ENV=development
```

Change the value of `FLASK_ENV` to `production` if you wish to run the application in production mode.

### Step 3: Configure `.env.development` and `.env.production`

These files contain the environment-specific configurations for your application.

#### Development Environment Configuration

**.env.development**
```plaintext
MONGODB_USERNAME=your_development_username
MONGODB_PASSWORD=your_development_password
MONGODB_HOST=your_development_host
MONGODB_APP_NAME=your_development_app_name
REDIS_HOST=your_development_redis_host
REDIS_PORT=your_development_redis_port
REDIS_USERNAME=your_development_redis_username
REDIS_PASSWORD=your_development_redis_password
```

#### Production Environment Configuration

**.env.production**
```plaintext
MONGODB_USERNAME=your_production_username
MONGODB_PASSWORD=your_production_password
MONGODB_HOST=your_production_host
MONGODB_APP_NAME=your_production_app_name
REDIS_HOST=your_production_redis_host
REDIS_PORT=your_production_redis_port
REDIS_USERNAME=your_production_redis_username
REDIS_PASSWORD=your_production_redis_password
```

Replace the placeholder values in `.env.development` and `.env.production` with your actual environment settings.

## Populating the Database with Countries Data

This application includes a script to automatically populate your MongoDB database with countries information by fetching data from an external API. Before running the script, ensure you have configured your environment files as described in the [Environment Setup](#environment-setup) section, as the script relies on these settings to connect to your MongoDB instance.

### Running the Population Script

Once your environment files are configured, you can populate the database by running the following command from the root directory of the project:

```bash
python3 populate_database.py
```

This script will connect to the specified external API to fetch country data and then insert this data into your MongoDB database. Ensure that your database is accessible and that the MongoDB credentials provided in your environment files are correct.

## API Endpoints

### Get Country Information

- **URL**: `/countries/<cca2>`
- **Method**: `GET`
- **URL Params**: 
  - **Required**: `cca2=[string]` where `cca2` is the 2-letter country code.

- **Success Response**:
  - **Code**: 200 
  - **Content**: Country information in JSON format.

- **Sample Call**: 
```bash
curl http://localhost:5000/countries/PL
```

### Compare Two Countries

- **URL**: `/countries/compare`
- **Method**: `GET`
- **Query Params**: 
  - **Required**: 
    - `country1=[string]` where `country1` is the 2-letter code of the first country.
    - `country2=[string]` where `country2` is the 2-letter code of the second country.
    - `criteria=[string]` the criteria to compare the countries on.

- **Sample Call**: 
```bash
curl http://localhost:5000/countries/compare?country1=GB&country2=PL&criteria=population
```

## Built With

- [Flask](http://flask.pocoo.org/) - The web framework used
- [PyMongo](https://api.mongodb.com/python/current/) - MongoDB driver for Python
- [Redis](https://redis.io/) - In-memory data structure store, used as a database, cache, and message broker.
- [Pytest](https://pytest.org/) - Testing framework used to develop and execute unit tests.

## Authors

- Przemyslaw Baj


