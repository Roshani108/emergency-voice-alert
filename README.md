<<<<<<< HEAD
# 🚨 Emergency Voice Alert System

A **Streamlit-based emergency alert app** that listens for emergency phrases like **"help"**, **"emergency"**, or **"save me"** and instantly:

- Sends an **email** with your **location**
- Captures and saves a short **video & audio recording** as evidence

> 💡 Ideal for personal safety, vulnerable individuals, or quick alerts during dangerous situations.

---

## 🧠 Features

- 🎙️ Real-time **voice recognition** using Google Speech API
- 📍 Automatically detects **your location** using IP
- 📧 Sends **email alerts** to a trusted contact
- 📹 Records **5-second video + audio** once triggered
- 🌐 Simple **Streamlit web interface**
- 🔐 Secure email via **Gmail App Passwords**

---

## 📂 Project Structure

emergency-voice-alert/
├── emergency_app_main.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── .gitignore # Ignore cache, env, media files
├── README.md # This documentation
└── assets/
├── home.png # UI screenshot
├── triggered.png # After trigger screenshot
├── demo.gif # Quick visual demo
└── demo.mp4 # Full demo video

---

## 📦 Required Python Packages

You can install all dependencies at once:

```bash
pip install -r requirements.txt

Or manually:

bash
pip install streamlit
pip install SpeechRecognition
pip install geocoder
pip install pyaudio
pip install opencv-python
🔧 If PyAudio causes issues (especially on Windows), use:

bash
pip install pipwin
pipwin install pyaudio

▶️ How to Run the App
streamlit run emergency_app_main.py
Make sure your microphone and camera are enabled.

🗣️ Trigger Words (Customizable)
help

emergency

save me

i need help

Once one of these is detected:

Location is fetched (city, state, coordinates)

few seconds of video and audio is captured

An email alert is sent to your trusted contact

📧 Email Format (Sent Automatically)
Subject: 🚨 Emergency Voice Alert Triggered

Trigger Word Detected: "help"
Location: New Delhi, Delhi, India
Coordinates: (28.6139, 77.2090)

Please take action immediately.
🔐 Email Setup Instructions
Enable 2-Step Verification on your Gmail account.

Go to: Google App Passwords

Generate an app password and paste it in emergency_app_main.py:
EMAIL_SENDER = 'youremail@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
EMAIL_RECEIVER = 'trustedperson@gmail.com'
📸 Screenshots
Home Screen	Emergency Triggered

🎥 Demo Video
🔗 Watch Full Demo (demo.mp4)

✅ requirements.txt

streamlit
SpeechRecognition
geocoder
pyaudio
opencv-python
💡 Future Improvements
More accurate GPS-based location

SMS alerts via Twilio or Fast2SMS

Continuous background listening

Save captured media to Google Drive or Dropbox

👩‍💻 Developer
Roshani
GitHub: Roshani108

📜 License
MIT License © 2025 Roshani
=======
# emergency-voice-alert
A voice-activated emergency alert app with location and email features.
