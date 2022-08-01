# tans-t-train-tracker
Finds the next departing train for stops on the MBTA T train system.


## Backend Setup

Requires Python 3.10

cd into the backend folder - `cd backend`

Install pipenv - `pip install pipenv`

Install dependencies - `pipenv install`

Open the pipenv shell - `pipenv shell`

Run the backend - `python manage.py runserver`

# Optional - Add an API Key

Register for an [MTBA API Key](https://api-v3.mbta.com/)

Add the key to the system environment variables with the name `MBTA_API_KEY`