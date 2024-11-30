# Django Producer-Consumer Application

This project is a producer-consumer application built with python and Django. It features:
- A **Producer** service that sends events to a consumer endpoint.
- A **Consumer** service (Django app) that processes incoming events.

## Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Virtualenv
- pip
- make 4.3

## Configuration

Create a .env file in the root directory with the following variables:

    PORT=8000
    PRODUCER_PERIOD_S=3.0
    PRODUCER_URL=http://127.0.0.1:${PORT}/api/event/
    PRODUCER_EVENT_PATH=producer/events.json
    CONSUMER_DB_NAME=db.sqlite3


## Setup
In the root directory, run the following command:

    make setup

This will create python virtual env and prepare the databse.

## Running the Application 

To run the producer service run the following command:

    make run-producer

To run the consumer service run the following command:

    make run-consumer

Or to run both services in the same terminal window, run the following command:

    make run

## Cleanup

To cleanup use the following command:

    make cleanup