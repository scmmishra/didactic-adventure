# Some Stupid Project

## Installation

1. Clone this repository

    `git clone https://github.com/adityahase/didactic-adventure`

2. Change directory

    `cd didactic-adventure`

3. Create virtual environment

    `virtualenv -p python3 env`

4. Activate virtual environment

    `source env/bin/activate`

5. Install requirements

    `pip install -r requirements.txt`

## Running application

1. Go to django directory

    `cd backend`

2. Migrate models

    `./manage.py migrate`

3. Run django development server

    `./manage.py runserver_plus`
