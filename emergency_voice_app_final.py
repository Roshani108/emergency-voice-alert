# 🚨 Emergency Voice Alert App with Location + Email using Streamlit

# ----------------------- IMPORTS -----------------------
import speech_recognition as sr
import geocoder
import smtplib
from email.message import EmailMessage
import streamlit as st
import cv2
from PIL import Image
import datetime
import os

# ----------------------- CONFIG ------------------------
EMAIL_SENDER = '108rosy@gmail.com'          # Your Gmail address
EMAIL_PASSWORD = 'yczw kbgy psmt gjbr'           # Your Gmail app password (not actual password)
EMAIL_RECEIVER = 'iitaspirant457@gmail.com' # Receiver's email (friend/family)

TRIGGER_PHRASES = ["help me", "emergency", "save me", "i need help"]

# ----------------------- FUNCTIONS ---------------------
def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return f"{g.city}, {g.state}, {g.country} ({g.latlng})"
    else:
        return "Location not found"

def send_email_alert(location, recognized_text):
    msg = EmailMessage()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = '🚨 Emergency Voice Alert Triggered'
    msg.set_content(f"Trigger Word Detected: {recognized_text}\nLocation: {location}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

def record_video(duration=5, output_file="emergency_video.avi"):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    start_time = datetime.datetime.now()
    while (datetime.datetime.now() - start_time).seconds < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

    cap.release()
    out.release()

def save_audio(audio_data, filename="emergency_audio.wav"):
    with open(filename, "wb") as f:
        f.write(audio_data.get_wav_data())

# ----------------------- STREAMLIT APP ---------------------
st.set_page_config(page_title="Emergency Voice Alert", page_icon="🚨", layout="centered")

st.markdown("<h1 style='text-align: center; color: red;'>🚨 Emergency Voice Alert App</h1>", unsafe_allow_html=True)
st.markdown("### Speak a phrase like: **'Help me'**, **'Emergency'**, **'I need help'**")
st.markdown("Click the button below to begin voice detection:")

# ----------------------- VOICE RECOGNITION ---------------------
if st.button("🎙️ Start Listening", use_container_width=True):
    with st.spinner("🎧 Listening for trigger phrases... Please speak clearly."):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        st.success(f"🗣️ You said: `{text}`")

        if any(phrase in text for phrase in TRIGGER_PHRASES):
            location = get_location()
            send_email_alert(location, text)
            save_audio(audio, "emergency_audio.wav")
            record_video(duration=5, output_file="emergency_video.avi")
            st.error(f"🚨 Emergency Detected! Alert sent to contact.\n📍 Location: {location}\n🎥 Video and voice recorded.")
        else:
            st.info("✅ No emergency trigger detected.")

    except sr.UnknownValueError:
        st.warning("😕 Sorry, could not understand your voice.")
    except sr.RequestError:
        st.error("❌ Internet or Google Speech API error.")
