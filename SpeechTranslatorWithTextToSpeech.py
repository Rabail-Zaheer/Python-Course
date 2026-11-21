import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os


# Text-to-Speech
def speak(text, language="en"):

    tts = gTTS(text=text, lang=language)

    # Save speech as an audio file
    filename = "translation.mp3"
    tts.save(filename)

    # Play the audio
    playsound.playsound(filename)

    # Delete the audio file after playing
    os.remove(filename)


# Speech-to-Text: Recognize spoken language (English)
def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\n🎤 Please speak now in English...")

        audio = recognizer.listen(source)

    try:

        print("🔄 Recognizing speech...")

        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        print(f"✅ You said: {text}")

        return text

    except sr.UnknownValueError:

        print("❌ Could not understand the audio.")

    except sr.RequestError as e:

        print(f"❌ API Error: {e}")

    return ""


# Translate text using Google Translate
def translate_text(text, target_language="es"):

    translator = Translator()

    translation = translator.translate(
        text,
        dest=target_language
    )

    print(f"🌎 Translated text: {translation.text}")

    return translation.text


# Display language options
def display_language_options():

    print("\n🌎 Available translation languages:")

    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    print("9. Urdu (ur)")

    choice = input(
        "\nPlease select the target language number (1-9): "
    )

    language_dict = {

        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa",
        "9": "ur"

    }

    # Default to Urdu if invalid choice is entered
    return language_dict.get(choice, "ur")


# Main function
def main():

    # Step 1: Select target language
    target_language = display_language_options()

    # Step 2: Get English speech
    original_text = speech_to_text()

    # Continue only if speech was successfully recognized
    if original_text:

        # Step 3: Translate the text
        translated_text = translate_text(
            original_text,
            target_language=target_language
        )

        # Step 4: Speak the translated text
        print("\n🔊 Speaking translation...")

        speak(
            translated_text,
            language=target_language
        )

        print("✅ Translation spoken successfully!")


# Start the program
if __name__ == "__main__":
    main()