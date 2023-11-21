#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Duolingo Podcast Downloader
by emreybs """
# This script will download all the mp3 files from the Duolingo Podcast website: https://podcast.duolingo.com/
# https://frpodcast.libsyn.com/rss has all the French podcasts of Duolingo. So, I used this RSS Feed for French podcasts.
# I only need French so, I will comment out the other languages. Added for others who may prefer to use them.
# I hope this helps you to learn French as well by listening to these lovely podcasts by Duolingo.
# I am not affiliated with Duolingo:) I just love their podcasts and I wanted to download them to listen offline.


from time import sleep
import requests
from bs4 import BeautifulSoup
import os
import re


# Define the base URL
print("\n\t\t\033[91mDuolingo Podcast Downloader\033[0m")  #For colorful output in the terminal. It may not work on some OS.
sleep(0.7)
print("\t\t\033[94m                          by emreYbs\n\033[0m") 
sleep(1)
print("This program downloads the mp3 files from the Duolingo Podcast website: https://podcast.duolingo.com/\n")
sleep(0.5)
print("\nThe mp3 files are saved in the 'Downloads' folder.\n") #Check your Downloads Folder, the mp3 files will be there.
print("For French podcasts of Duolingo, you can check this later: https://podcast.duolingo.com/french\n")

sleep(0.5)
# Prompt the user to enter the base URL
print("\033[91mThis script will use this RSS Feed for French podcasts: https://frpodcast.libsyn.com/rss\033[0m\n")
base_url = "https://frpodcast.libsyn.com/rss"

# Check if the entered URL is valid
url_pattern = r'^https?://(?:www\.)?(?:podcast\.duolingo\.com/french|frpodcast\.libsyn\.com/rss)$'
if not re.match(url_pattern, base_url):
    print("Please enter a valid URL like https://podcast.duolingo.com/french or https://frpodcast.libsyn.com/rss")
    print("Exiting...")
    print("Next time, write like this: 'https://podcast.duolingo.com/french' or 'https://frpodcast.libsyn.com/rss'\n")
    exit()


def userWantsquit():
    while True:
        user_input = input("Press 'q' to quit or 'Enter' or any key to continue: ")
        if user_input == "q":
            print("Exiting...")
            exit()
        else:
            print("Continuing...\n")
            break
quit = userWantsquit()


# Send a GET request to the download URL and retrieve the RSS feed
response = requests.get(base_url)
rss_feed = response.text

# Parse the RSS feed using BeautifulSoup
soup = BeautifulSoup(rss_feed, "xml")

# Find all the <item> tags in the RSS feed
items = soup.find_all("item")

# Create a "Downloads" folder if it doesn't exist
if not os.path.exists("Duolingo_downloads"):  #Check your Downloads Folder, the mp3 files will be there.
    os.makedirs("Duolingo_downloads")  #Sometimes, you may need to search for the folder in your computer.
                                       # It can be in your Home Folder or in your Downloads Folder.
    print("The 'Duolingo_downloads' folder has been created in your Downloads Folder.\n")
    sleep(0.5)
    print("The mp3 files will be saved in the 'Duolingo_downloads' folder.\n")
    print("It can be in your Home Folder or in your Downloads Folder.")

# Download the mp3 files
print("Downloading mp3 files...\n")
for item in items:
    # Extract the episode title and download URL
    episode_title = item.title.text
    download_url = item.enclosure["url"] 

    # Replace invalid characters in the episode title
    episode_title = re.sub(r'[<>:"/\\|?*]', '', episode_title)
    

    # Check if the podcast has already been downloaded
    if f"{episode_title}.mp3" in os.listdir("Duolingo_downloads"):
        print(f"Skipped: {episode_title} (already downloaded)")
        continue

    # Download the mp3 file and save it in the "Downloads" folder
    print(f"Downloading....")
    response = requests.get(download_url)
    file_name = os.path.join("Duolingo_downloads", f"{episode_title}.mp3")
    with open(file_name, "wb") as file:
        file.write(response.content)

    # Print a message indicating the successful download
    print(f"Downloaded: {episode_title}")

print("\033[94mAudio files downloaded and saved in the 'Downloads' folder.\033[0m") 
sleep(0.5)
print("\n\t\tDuolingo Podcast Downloader\n")
