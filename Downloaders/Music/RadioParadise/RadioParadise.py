#!/usr/bin/env python
# @emreYbs https://github.com/emreYbs
# FILEPATH: /D:/Python Projects/Download Related Projects/RadioParadise.py
# FILENAME: RadioParadise.py
# This script will work on a Windows PC and you can listen to Radio Paradise Stream via VLC Player
# It will also download the playlist of the songs played on Radio Paradise


print("\n")
from colorama import Fore

def banner():
    print(Fore.RED + "\t\tRadio Paradise (https://radioparadise.com)")
    print(Fore.WHITE +"\t\tby emreYbs")
    print("\n")
    print(Fore.BLUE + "Listen to Radio Paradise via VLC Player\n")  
    print(Fore.GREEN + "Download the playlist of the songs played on Radio Paradise")  
    print("\n")

banner()

import requests
from bs4 import BeautifulSoup
import os
import colorama
import platform
import subprocess
import time

def check_vlc():
    try:
        subprocess.call(["vlc", "--version"])
        return True
    except OSError:
        return False

def check_os():
    if platform.system() == "Windows":
        return True
        print("This script only works on Windows")
    else:
        return False
        print("Exiting...")

if check_os() and check_vlc():
    print("OS is Windows and VLC Player is installed.")
else:
    print("\nWarning: This script may not work properly if VLC Player is NOT installed in its default path.")

print(Fore.YELLOW + ".....Downloading Radio Paradise Stream.....")

from time import sleep
def download_radio_stream():
    audio_url = 'https://radioparadise.com/m3u/mp3-192.m3u'
    if audio_url:
        response = requests.get(audio_url)
        with open('RadioParadise.m4a', 'wb') as f:
            f.write(response.content)
            sleep(1)
            print(Fore.BLUE + "\nRadio Paradise Stream downloaded\n")   
            sleep(0.1) 
            print(Fore.GREEN + "You can listen to Radio Paradise Stream via VLC Player\n")

    else:
        print(Fore.RED + "Could not find audio URL")
        print(Fore.ORANGE + "Exiting...")

    
    if os.path.exists('RadioParadise.m4a'):
        os.startfile('RadioParadise.m4a')
    else:
        print("Audio file not found")

def download_playlist():
    playlist_url = 'https://radioparadise.com/playlist'
    response = requests.get(playlist_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    song_urls = [a['href'] for a in soup.find_all('a', {'class': 'track'})]

    
    for i, song_url in enumerate(song_urls):
        response = requests.get(song_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        song_title = soup.find('h1', {'class': 'track'}).text.strip()
        mp3_url = soup.find('a', {'class': 'download'})['href']
        with open(f'{i+1}. {song_title}.mp3', 'wb') as f:
            f.write(requests.get(mp3_url).content)

def test_download_radio_stream():
    download_radio_stream()
    assert os.path.exists('RadioParadise.m4a')

if __name__ == '__main__':
    download_radio_stream()
    download_playlist()







