import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from requests import get
import wikipedia
import webbrowser
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User  said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return "none"
    except sr.RequestError:
        speak("Could not request results from Google Speech Recognition service.")
        return "none"
    except Exception as e:
        speak("Say that again please...")
        return "none"

    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Mam, Please tell me how I can help you")


def play_spotify():
    # Authenticate with Spotify
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
            redirect_uri="http://localhost:8888/callback",
            scope="user-read-playback-state,user-modify-playback-state,user-read-currently-playing",
        )
    )

    # Play a specific song or playlist
    sp.start_playback(
        context_uri="spotify:track:3yiEaNgKJWN3gCfHfB8Q1u"
    )  # Use the Spotify URI format


if __name__ == "__main__":
    wish()

    # Listen for a command once
    query = takecommand().lower()
    if query == "none":
        print("No valid command recognized.")
    else:
        # Add your command handling logic here
        if "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                if not ret:
                    speak("Failed to capture image.")
                    break
                cv2.imshow("webcam", img)
                k = cv2.waitKey(1)
                if k == 27:  # ESC key to exit
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            play_spotify()  # Call the function to play music on Spotify

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text  # Corrected URL
            speak(
                f"The IP Address of this computer is {ip}"
            )  # Use f-string to format the output

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            speak("Open YouTube...")
            webbrowser.open("www.youtube.com")

        elif "open spotify" in query:
            speak("Open spotify...")
            webbrowser.open("www.spotify.com")

        elif "open google" in query:
            speak("What should I search on Google?")
            cm = takecommand().lower()  # Get the user's search query
            if cm:  # Check if the command is not empty
                webbrowser.open(
                    f"https://www.google.com/search?q={cm}"
                )  # Open Google with the search term

            else:
                speak("You didn't provide a search term.")


        elif "send message" in query:
            kit.sendwhatmsg("+918528516800", "this is a testing protocol", 1, 26)
