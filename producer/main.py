import argparse
import json
import logging
import random
import re
import requests
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[PRODUCER] %(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S')

def is_valid_url(url: str) -> bool:
    """Validate the given URL."""
    regex = re.compile(
        r'^(https?):\/\/'  # Protocol
        r'([\w.-]+)'       # Hostname
        r'(:\d+)?'         # Optional port
        r'(\/.*)?$',       # Path and query string
        re.IGNORECASE
    )
    if not re.match(regex, url):
        raise argparse.ArgumentTypeError(f"Invalid URL: {url}")
    return url

def load_arguments() -> dict:
    parser = argparse.ArgumentParser(description="Event Producer")

    parser.add_argument('--period', type=float, required=True, help="The period of the events in seconds")
    parser.add_argument('--url', type=is_valid_url, required=True, help="Events endpoint")
    parser.add_argument('--file', type=str, required=True, help="Path to the events json file")
    
    args = parser.parse_args()
    
    return args

def load_events(file_path: str) -> dict:
    with open(file_path, "r") as file:
        events = json.load(file)
        
    if not isinstance(events, list):
        raise ValueError(f"The JSON data in {file_path} is not a list.")
    
    return events
    
def send_event(url, event):
    try:
        response = requests.post(url, json=event)
        response.raise_for_status()
        
        logging.info("Successfully sent an event to the consumer service")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred while sending data: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def main():
    args = load_arguments()

    events = load_events(args.file)
        
    while True:
        period_start = datetime.now()
        
        send_event(args.url, random.choice(events))
        
        time.sleep(args.period - (datetime.now() - period_start).total_seconds())

if __name__ == "__main__":
    main()