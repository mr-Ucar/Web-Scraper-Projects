#!/usr/bin/env python3
#https://github.com/emreYbs
# I modified this script which works well:https://github.com/ibuetler/unsplash-image-downloader-python
# Some modifications:  -save the images in subfolders named after the topic
# input validation, logging, sleep module, etc.
# You can use the script with command-line arguments or let the user enter the necessary values.

import requests
import argparse
import string
import random
import os
import hashlib
from pathlib import Path
from urllib.parse import urlparse
import logging # Added logging module to the script for debugging and informing the user about the process.
from time import sleep # Added sleep module to the script for better user experience.


logging.basicConfig(level=logging.INFO)

print("")
print("\033[94m**************************************\033[0m")
print("\033[94m* Unsplash Image *\033[0m")
print("\033[94m*   Downloader   *\033[0m")
print("Original Script: github.com/ibuetler")
print("Modified Script: github.com/emreYbs")
print("\033[94m**************************************\033[0m")
print("\nYou can check the official website: https://unsplash.com/\n")
print("\nThis program allows you to download random images from Unsplash based on a topic.")
sleep(1)
print("\033[92mUSAGE: python unsplash-image-downloader.py --topic <topic> --resolution <resolution> --amount <amount>\033[0m")
sleep(1)
print("\033[95mEXAMPLE: python unsplash-image-downloader.py --topic nature --resolution 1920x1080 --amount 5\033[0m")
sleep(1)
print("Options:")
sleep(0.5)
print("  --topic: The topic of the photo  (-required-)")
sleep(0.5)
print("  --resolution: The resolution of photos (-required-)")
sleep(0.5)
print("  --amount: The amount of images to download (-required-)")
sleep(0.5)
print("Example: python unsplash-image-downloader.py --topic city --resolution 1280x720 --amount 10")

def validate_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == "source.unsplash.com":
        return True
    else:
        return False

def download_image(search_term, resolution, amount):
    for x in range(amount): 
        url = f"https://source.unsplash.com/random/{resolution}/?{search_term}"
        if not validate_url(url):
            logging.error("Invalid URL")
            return
        logging.info(f"Downloading image {x + 1} of {amount} from {url}")
        response = requests.get(url, allow_redirects=True)
        filename = f"{search_term}_{generate_random_string(5)}_{x + 1}.png"
        save_path = os.path.join("photos", search_term, filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        logging.info(f"Saving image to: {save_path}")
        with open(save_path, 'wb') as file:
            file.write(response.content)
        logging.info(f"Saved image to: {save_path}")

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def calculate_hash_value(path, blocksize=65536):
    hasher = hashlib.md5()
    with open(path, 'rb') as file:
        buf = file.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(blocksize)
    return hasher.hexdigest()

def remove_duplicate_files(input_files):
    unique_files = {}
    duplicate_files = {}

    for file_path in input_files:
        if Path(file_path).exists():
            file_hash = calculate_hash_value(file_path)
            if file_hash in unique_files:
                logging.info(f"Removing duplicate file: {file_path}")
                os.remove(file_path)
            else:
                logging.info(f"Adding file: {file_path}")
                unique_files[file_hash] = file_path
        else:
            logging.error(f"{file_path} is not a valid path, please verify")

def main():
    parser = argparse.ArgumentParser(description="Unsplash Downloader")
    parser.add_argument('--topic', type=str, help="Topic the photo will be about")
    parser.add_argument('--resolution', type=str, help="Resolution of Photos")
    parser.add_argument('--amount', type=int, help="Amount of images: How many photos do you want to download")
    args = parser.parse_args()

    topic = args.topic
    resolution = args.resolution
    amount = args.amount

    if not topic:
        topic = input("\n\tEnter a topic: ")
    if not resolution:
        resolution = input("\n\tEnter a resolution: ")
    if not amount:
        amount = int(input("\n\tEnter an amount: \n"))

    download_image(topic, resolution, amount)

    input_files_path = "photos"  # Directory
    input_files = [os.path.join(input_files_path, f) for f in os.listdir(input_files_path) if 
                   os.path.isfile(os.path.join(input_files_path, f))]
    remove_duplicate_files(input_files)
    logging.info("Done\n")

if __name__ == "__main__":
    main()
    logging.info("Exiting...\n")
