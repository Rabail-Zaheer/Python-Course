import threading

import sys

import time

import os

import pyaudio

import numpy as np

import matplotlib as plt

import wave

import speech_recognition as sr

from speech_recognition import AudioData

stop_event = threading.Event()

def wait_for_enter():

input("\nPress Enter to stop recording")

stop_event.set()

def spinner():

chars = '|/-\\'

i = 0

while not stop_event:

sys.stdout.wrtie(f'\nRecording... {chars [i % 4]}')

sys.stdout.flush()

i +=1

time.sleep(0.1)

print("\rRecording Completed")

def record_audio():

stop_event.clear()

p = pyaudio.PyAudio()

stream = p.open(

format=pyaudio.paInt16,

channels=1,

rate = 16000,

input=True,

frames_per_buffer=1024

)

frames = []

threading.Thread(

target=wait_for_enter,

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

plt.show()

def compare_recording(data1,rate1,data2,rate2):

sample1 = np.frombuffer(data1,dtype=np.int16)

sample2 = np.frombuffer(data2,dtype=np.int16)

duration1 = len(sample1) / rate1

duration2 = len(sample2) / rate2

volume1 = np.mean(np.abs(sample1))

volume2 = np.mean(np.abs(sample2))

print("\n" + "=" * 40)

print("Recording Compherission")

print("=" * 40)

print(f"Recording 1 Duration {duration1:.2f} seconds")

print(f"Recording 2 Duration {duration2:.2f} seconds")

print(f"Recording 1 average volume {volume1:.2f}")

print(f"Recording 2 average volume {volume2:.2f}")

if duration1 > duration2:

print("Recording 1 is longer")

elif duration2 > duration1:

print("Recording 2 is longer")

else:

print("Both recordings are same")

if volume1 > volume2:

print("Recording 1 is louder")

elif volume2 > volume1:

print("Recording 2 is louder")

else:

print("Both are equal")

def main():

print("=" * 40)

print("🎙️ HELLO AI, CAN YOU HEAR ME?")

print("=" * 40)

print("\nSpeak into your microphone...")

audio_data1, rate1, width1 = record_audio()

save_audio(audio_data1, rate1, width1)

transcribe(audio_data1, rate1, width1)

plot_waveform(audio_data1, rate1)

print("Recording 2")

print("Speak into Your mice")

audio_data2, rate2, width2 = record_audio()

save_audio(audio_data2, rate2, width2)

transcribe(audio_data2, rate2, width2)

plot_waveform(audio_data2, rate2)

compare_recording(

audio_data1,

rate1,

audio_data2,

rate2

)

# Start the program

if __name__ == "__main__":

main()