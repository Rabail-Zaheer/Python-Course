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
    stop_event.clear()

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

    threading.Thread(
        target=spinner,
        daemon=True
    ).start()

    while not stop_event.is_set():
        frames.append(stream.read(1024))

    stream.stop_stream()
    stream.close()

    width = p.get_sample_size(pyaudio.paInt16)

    p.terminate()

    return b''.join(frames), 16000, width


def save_audio(data, rate, width, filename="recording.wav"):

    folder = os.path.dirname(os.path.abspath(__file__))

    filepath = os.path.join(folder, filename)

    with wave.open(filepath, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)

    print(f"💾 Saved: {filepath}")


def transcribe(data, rate, width):
    recognizer = sr.Recognizer()

    audio = AudioData(data, rate, width)

    try:
        text = recognizer.recognize_google(audio)

        print(f"📝 Transcription: {text}")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")

    except sr.RequestError as e:
        print(f"❌ API Error: {e}")


def plot_waveform(data, rate):

    samples = np.frombuffer(data, dtype=np.int16)

    time_axis = np.linspace(
        0,
        len(samples) / rate,
        len(samples)
    )

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

    plt.show()


def compare_recordings(data1, rate1, data2, rate2):

    samples1 = np.frombuffer(data1, dtype=np.int16)
    samples2 = np.frombuffer(data2, dtype=np.int16)

    duration1 = len(samples1) / rate1
    duration2 = len(samples2) / rate2

    volume1 = np.mean(np.abs(samples1))
    volume2 = np.mean(np.abs(samples2))

    print("\n" + "=" * 40)
    print("🎙️  RECORDING COMPARISON")
    print("=" * 40)

    print(f"Recording 1 Duration: {duration1:.2f} seconds")
    print(f"Recording 2 Duration: {duration2:.2f} seconds")

    print(f"Recording 1 Average Volume: {volume1:.2f}")
    print(f"Recording 2 Average Volume: {volume2:.2f}")

    if duration1 > duration2:
        print("⏱️ Recording 1 is longer.")
    elif duration2 > duration1:
        print("⏱️ Recording 2 is longer.")
    else:
        print("⏱️ Both recordings have the same duration.")

    if volume1 > volume2:
        print("🔊 Recording 1 is louder.")
    elif volume2 > volume1:
        print("🔊 Recording 2 is louder.")
    else:
        print("🔊 Both recordings have similar volume.")


def main():

    print("=" * 40)
    print("🎙️  HELLO AI, CAN YOU HEAR ME?")
    print("=" * 40)

    print("\n🎤 Recording 1")
    print("Speak into your microphone...")

    audio_data1, rate1, width1 = record_audio()
    save_audio(audio_data1, rate1, width1, "recording1.wav")
    transcribe(audio_data1, rate1, width1)
    plot_waveform(audio_data1, rate1)

    print("\n🎤 Recording 2")
    print("Speak into your microphone...")

    audio_data2, rate2, width2 = record_audio()
    save_audio(audio_data2, rate2, width2, "recording2.wav")
    transcribe(audio_data2, rate2, width2)
    plot_waveform(audio_data2, rate2)

    compare_recordings(
        audio_data1,
        rate1,
        audio_data2,
        rate2
    )


# Start the program
if __name__ == "__main__":
    main()