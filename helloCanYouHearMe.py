"""
L2: Voice Analysis Lab

Record → Analyze → Compare Two Recordings


============== DEPENDENCY SETUP ==============

CHECK IF INSTALLED:
pip show SpeechRecognition pyaudio numpy matplotlib

INSTALL - WINDOWS:
pip install SpeechRecognition pyaudio numpy matplotlib

INSTALL - macOS:
brew install portaudio
pip install SpeechRecognition pyaudio numpy matplotlib

==============================================
"""

"""
L1: Basic Speech-to-Text

Record → Save → Transcribe → Visualize Waveform
"""
import threading
import sys
import time
import os
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData

# Event used to stop the recording
stop_event = threading.Event()

def wait_for_enter():
    input("\n🎤 Press Enter to stop recording...\n")
    stop_event.set()

def spinner():
    chars = '|/-\\'
    i = 0

    while not stop_event.is_set():
        sys.stdout.write(f'\r🔴 Recording... {chars[i % 4]}')
        sys.stdout.flush()

        i += 1
        time.sleep(0.1)

    print("\r✅ Recording complete!")


def record_audio():
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024
    )

    frames = []

    threading.Thread(
        target=wait_for_enter,
        daemon=True
    ).start()

    # Start the recording animation
    threading.Thread(
        target=spinner,
        daemon=True
    ).start()

    # Keep recording until Enter is pressed
    while not stop_event.is_set():
        frames.append(stream.read(1024))

    # Stop and close the microphone
    stream.stop_stream()
    stream.close()

    width = p.get_sample_size(pyaudio.paInt16)

    p.terminate()

    # Combine all audio chunks into one piece of audio
    return b''.join(frames), 16000, width


def save_audio(data, rate, width, filename="recording.wav"):

    # Find the folder where this Python file is located
    folder = os.path.dirname(os.path.abspath(__file__))

    # Create the complete path for the audio file
    filepath = os.path.join(folder, filename)

    # Save the audio as a WAV file
    with wave.open(filepath, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)

    print(f"💾 Saved: {filepath}")


def transcribe(data, rate, width):
    recognizer = sr.Recognizer()

    # Convert our audio into SpeechRecognition's AudioData format
    audio = AudioData(data, rate, width)

    try:
        # Convert speech into text
        text = recognizer.recognize_google(audio)

        print(f"📝 Transcription: {text}")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")

    except sr.RequestError as e:
        print(f"❌ API Error: {e}")


def plot_waveform(data, rate):

    # Convert audio data into numbers
    samples = np.frombuffer(data, dtype=np.int16)

    # Create the time values for the X-axis
    time_axis = np.linspace(
        0,
        len(samples) / rate,
        len(samples)
    )

    # Create the graph
    plt.figure(figsize=(10, 4))

    plt.plot(
        time_axis,
        samples,
        color='blue'
    )

    plt.title("Your Voice Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    # Display the graph
    plt.show()


def main():

    print("=" * 40)
    print("🎙️  HELLO AI, CAN YOU HEAR ME?")
    print("=" * 40)

    print("\nSpeak into your microphone...")

    audio_data, rate, width = record_audio()
    save_audio(audio_data, rate, width)
    transcribe(audio_data, rate, width)
    plot_waveform(audio_data, rate)

# Start the program
if __name__ == "__main__":
    main()