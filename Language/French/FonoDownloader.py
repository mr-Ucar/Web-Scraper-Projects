#emreYbs 
#!/usr/bin/env python

# This simple script was written for my French language learning project. 
# It downloads audio files from the Fono website (https://fono.com.tr/) and saves them in the 'downloads' folder.
# You can download other languages like German, Enlish to practise your pronunciation.
# You can also use this script to download audio files from other websites. I also use it to download DuoLingo Podcasts.

import os
import requests
from termcolor import colored

print(colored("\n\t\tFono Audio Downloader\n", "blue"))
print(colored("This program downloads the audio files from the Fono website: https://fono.com.tr/"))
print("\nThe audio files are saved in the 'downloads' folder.\n")

base_url = input("\nEnter the download link: ")
audio_name = input("\nEnter the name of the audio file: ")

# Validate user input
try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
except ValueError:
    print("Invalid input. Please enter numbers for the starting and ending numbers. Like this: 1, 2, 3, 4, 5, etc.")
    exit()

# Create the downloads folder if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")
    print(colored("\nCreated the 'downloads' folder.", "green"))
# Use file permissions to restrict access to sensitive files or use a secure file storage service
    os.chmod("downloads", 0o700)
    print(colored("Changed the permissions of the 'downloads' folder.", "blue"))
    

# Download the audio files
print(colored("Downloading audio files...\n", "yellow"))

for i in range(start, end+1):
    audio_url = base_url.format(i)
    if i == 1:
        file_name = f"{audio_name}.mp3"
    else:
        file_name = f"{audio_name}_{i}.mp3"
    file_path = os.path.join("downloads", file_name)
    try:
        response = requests.get(audio_url, stream=True)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(colored(f"Audio file {i} downloaded.", "blue"))
    except Exception as e:
        print(colored(f"Error downloading audio file {i}: {e}", "red"))
        continue


print(colored("\nAudio files downloaded and saved in the 'downloads' folder.", "green"))
print(colored("Exiting...", "red"))




