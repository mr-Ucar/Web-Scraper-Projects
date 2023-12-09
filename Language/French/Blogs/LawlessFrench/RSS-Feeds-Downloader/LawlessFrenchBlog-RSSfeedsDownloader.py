#!/usr/bin/env python3
#emreYbs: github.com/emreYbs
# -*- coding: utf-8 -*-

import json
import csv 
import feedparser #pip3 install feedparser
from time import sleep #Not normally needed but I wanted the script to slow down.
import os #Needed for automatic Folder creation for the downloaded RSS Feeds şn csv, html, json
from datetime import datetime

def format_time(time_str):
    # Convert the time string to a datetime object
    time_obj = datetime.strptime(time_str, "%a, %d %b %Y %H:%M:%S %z")
    # Format the datetime object as a user-friendly string without timezone offset
    # Example: 2020-05-01 12:00:00 The reason I wrote like this is to enable the user a little more privacy. So their geo location will not be revealed in the saved .csv, .json and .html files.
    # Not important for many, but for a OSINT practitioner, this is important.
    formatted_time = time_obj.strftime("%a, %d %b %Y %H:%M:%S")
    return formatted_time

def download_rss_feed(base_url):
    # Check if the RSS feed has already been downloaded
    json_file_path = os.path.join("French Blogs", "LawlessFrenchBlog", "rss_feed.json")
    if os.path.exists(json_file_path):
        print("\n\033[31m\tRSS feed has already been downloaded. Skipping...\033[0m\n") 
        return

    # Download the RSS feed
    print("")
    sleep(0.1)
    print("\033[34m▁ ▂ ▄ ▅ ▆ ▇ █ Lawless French Blog RSS Feed Downloader █ ▇ ▆ ▅ ▄ ▂ ▁\033[0m") 
    print("\033[35m\t\t\tby emreYbs\033[0m") 
    sleep(0.2)
    print("\033[34m\nA good and helpful Blog for French learners and teachers.\033[0m") 
    print("\nThis Python script will download RSS Feeds from the Lawless French Blog.")
    sleep(0.2)
    print("""       //     https://www.lawlessfrench.com/        //
                               """)
    sleep(0.2)
    print("\nThe RSS feed links will be saved in rss_feed.json, rss_feed.csv and rss_feed.html files.")
    sleep(0.1)
    print("'https://feeds.feedblitz.com/LawlessFrenc' is the RSS feed link of the Lawless French Blog.")
    sleep(0.1)
    print(f"\n\033[32mDownloading {base_url}...\033[0m") 
    sleep(0.1)
    print("")

    feed = feedparser.parse(base_url)
    print(f"Downloaded {len(feed.entries)} entries")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(f"Feed title: {feed.feed.title}") 
    sleep(0.1)
    print(f"Feed link: {feed.feed.link}")
    sleep(0.1)
    print(f"Feed description: {feed.feed.description}")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(f"Last updated: {feed.feed.updated}")
    sleep(0.1)
    print("")
    print(f"Feed language: {feed.feed.language}")

    # Save as JSON
    with open(json_file_path, "w") as json_file: 
        print(f"Saving to {json_file.name}...")
        sleep(0.1)
        print("")
        json.dump(feed, json_file, indent=4)
        sleep(0.1)
        print("\033[35mSaved\033[0m")
        sleep(0.1)
        print("")
    print(f"\033[34mThe RSS feed links are saved in {os.path.abspath(json_file_path)}\033[0m")
    sleep(0.1)

    # Save as CSV
    csv_file_path = os.path.join("French Blogs", "LawlessFrenchBlog", "rss_feed.csv")
    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        sleep(0.1)
        writer.writerow(["Title", "Link", "Published"])
        print(f"Saving to {csv_file.name}...")
        sleep(0.1)
        print("")
        for entry in feed.entries:
            sleep(0.1)
            writer.writerow([entry.title, entry.link, entry.published])
            sleep(0.1)
            print(f"Title: {entry.title}")
            sleep(0.1)
            print(f"Link: {entry.link}")
            sleep(0.1)
            print(f"Published: {entry.published}")
            sleep(0.1)
            print("")

    # Save as HTML
    html_file_path = os.path.join("French Blogs", "LawlessFrenchBlog", "rss_feed.html")
    with open(html_file_path, "w") as html_file:
        sleep(0.1)
        print(f"Saving to {html_file.name}...")
        sleep(0.1)
        print("")
        html_file.write("<html>")
        html_file.write("<head>")
        sleep(0.1)
        html_file.write("<title>RSS Feed</title>")
        sleep(0.1)
        html_file.write("</head>")
        html_file.write("<body>")
        sleep(0.1)
        html_file.write("<h1>RSS Feed</h1>")
        html_file.write("<ul>")
        sleep(0.1)
        for entry in feed.entries:
            html_file.write("<li>")
            html_file.write(f"<a href='{entry.link}'>{entry.title}</a>")
            sleep(0.2)
            html_file.write("</li>")
        html_file.write("</ul>")
        sleep(0.2)
        html_file.write("</body>")
        sleep(0.2)
        html_file.write("</html>")
        print("\033[35mSaved\033[0m")
        print("")
        sleep(0.1)
    sleep(0.2)
    print(f"\033[34mThe RSS feed links are saved in {os.path.abspath(html_file_path)}\033[0m")  
    print("\n\033[31mThank you for using this script to download RSS Feeds from the Lawless French Blog.\033[0m\n") 
    print("""
        \033[31     
          
            \ /      
 _ __  __ _  Y |_  _ 
(/_||| | (/_ | |_)_>   
                         
                            
        says thank you to
╦  ┌─┐┬ ┬┬─┐┌─┐  ╦╔═   ╦  ┌─┐┬ ┬┬  ┌─┐┌─┐┌─┐
║  ├─┤│ │├┬┘├─┤  ╠╩╗   ║  ├─┤││││  ├┤ └─┐└─┐
╩═╝┴ ┴└─┘┴└─┴ ┴  ╩ ╩o  ╩═╝┴ ┴└┴┘┴─┘└─┘└─┘└─┘

           for her great work and her great Blog as a French learner.
        \033[0m""") 
    sleep(0.1)

    # Print the JSON output in a more readable format
    print("")
    sleep(0.1)
    #print("JSON Output:") #uncomment this line to print the JSON output if you need. Personally, generally I prefer the terminal outputs to be clean and simple. 
    # But I wrote this line for you to see the JSON output.Sometimes it is good to see the JSON output in the terminal for my own needs.
    sleep(0.1)
    print("")
    sleep(0.4)
   # pprint.pprint(feed)     #uncomment this line to print the JSON output.
   # Generally I prefer the terminal outputs to be clean and simple. 
    # But I wrote this line for you to see the JSON output.Sometimes it is good to see the JSON output in the terminal for my own needs.
    sleep(0.3)
    print("")

# Base URL of the RSS feedclear
base_url = "https://feeds.feedblitz.com/LawlessFrench"

# Define the json_file_path variable
json_file_path = os.path.join("French Blogs", "LawlessFrenchBlog", "rss_feed.json")

# Create the directory path if it doesn't exist
os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

download_rss_feed(base_url)
