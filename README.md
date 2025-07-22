# Voice-Controlled Virtual Assistant (Jarvis)

This project is a **Voice-Controlled Virtual Assistant (Jarvis)** built using Python, which can perform basic system operations, search the web, control Spotify, and more using voice commands.

## Features

✅ Voice recognition using `speech_recognition`  
✅ Text-to-speech responses using `pyttsx3`  
✅ Greets based on the time of the day  
✅ Opens system applications like Notepad, Command Prompt, Camera  
✅ Fetches public IP address  
✅ Searches Wikipedia and reads summaries aloud  
✅ Plays music using Spotify API  
✅ Opens websites like YouTube, Google, Spotify  
✅ Sends WhatsApp messages using `pywhatkit`  

## Tech Stack

- Python 3.x
- [pyttsx3](https://pypi.org/project/pyttsx3/) for TTS
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) for voice recognition
- [Spotipy](https://spotipy.readthedocs.io/) for Spotify control
- [Requests](https://pypi.org/project/requests/) for IP fetching
- [Wikipedia](https://pypi.org/project/wikipedia/) for Wikipedia summaries
- [OpenCV](https://opencv.org/) for camera access
- [pywhatkit](https://pypi.org/project/pywhatkit/) for WhatsApp automation

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/voice-controlled-virtual-assistant.git
    cd voice-controlled-virtual-assistant
    ```

2. **Install dependencies:**
    ```bash
    pip install pyttsx3 SpeechRecognition opencv-python spotipy requests wikipedia pywhatkit
    ```

3. **Spotify Setup:**
   - Create a Spotify Developer application [here](https://developer.spotify.com/dashboard/).
   - Replace:
     ```python
     client_id="YOUR_CLIENT_ID",
     client_secret="YOUR_CLIENT_SECRET",
     ```
     in the script with your credentials.

4. **Run the assistant:**
    ```bash
    python assistant.py
    ```

5. **Usage:**
   - The assistant will greet you based on the time.
   - Speak commands such as:
     - "open notepad"
     - "open command prompt"
     - "open camera"
     - "play music"
     - "ip address"
     - "wikipedia [topic]"
     - "open youtube"
     - "open google"
     - "send message" (requires your device to be logged into WhatsApp Web)

## Notes

- Ensure your microphone is working and accessible.
- Requires stable internet for voice recognition and online functionalities.
- For WhatsApp automation, your computer will open a browser window for sending messages.
- For continuous command listening, modify the `__main__` loop.

