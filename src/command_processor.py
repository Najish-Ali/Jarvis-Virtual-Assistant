import webbrowser
import musiclibrary
import requests
import os
import time
from config import NEWSAPI_KEY

# process_command Function
def process_command(command, speak_fucntion, ai_process_function):
    # Converts the entire command to lowercase to ensure case-insensitive comparison.Converts the entire command to lowercase to ensure case-insensitive comparison.
    command = command.lower()
    # Checking Commands
    if command.startswith("open "):  # Checks if the command starts with "open ".
        #  A dictionary mapping site names to their URLs.
        url_map = {
            "google": "https://www.google.com",
            "gmail": "https://www.gmail.com",
            "youtube": "https://www.youtube.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "twitter": "https://www.twitter.com",
            "wikipedia": "https://www.wikipedia.org"
        }
        # Extracts the site name from the command.
        site = command[len("open "):]
        # condions..
        if site in url_map:
            # Opens the URL in a web browser if the site is in the dictionary
            webbrowser.open(url_map[site])
        else:
            #  Responds if the site is not recognized.
            speak_fucntion("Sorry I don't know that site.")

    # Checks if the command starts with "play "
    elif command.startswith("play "):
        # Extracts and trims the song name from the command.
        song_name = command[len("play "):].strip()
        # Checks if the song is in the musiclibrary.
        if song_name in musiclibrary.music:
            # Opens the song URL in a web browser if found.
            webbrowser.open(musiclibrary.music[song_name])
        else:
            #  Responds if the song is not in the musiclibrary.
            speak_fucntion("Sorry I don't know that song.")

    # Checks if the command contains the word "news".
    elif "news" in command:
        # function to handle news requests.
        fetch_news(speak_fucntion)

    # For commands that don't match predefined patterns, 
    # it calls the ai_process_function to handle them and speaks the response.
    else:
        output = ai_process_function(command)
        speak_fucntion(output)


# fetch_news Function
def fetch_news(speak_function):
    #  Retrieves the API key for the News API from environment variables.
    newsapi_key = os.getenv(NEWSAPI_KEY)
    # Makes an HTTP GET request to the News API to fetch the top headlines for India.
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi_key}")
    # Checks if the request was successful (HTTP 200 OK).
    if response.status_code == 200:
        # Parses the response JSON.
        data = response.json() 
        # Retrieves the list of articles from the JSON response.
        articles = data.get('articles', [])
        #  Iterates over each article and speaks the title.
        for article in articles:
            speak_function(article["title"])
    # Handles the case where the request fails by speaking an error message.
    else:
        speak_function("Sorry, I couldn;t fetch the news..")