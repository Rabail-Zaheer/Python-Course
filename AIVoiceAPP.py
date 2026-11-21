import speech_recognition as sr
from googletrans import Translator


# Speech-to-Text: Recognize spoken language (English)
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nPlease speak now in English...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return ""


# Translate text using Google Translate API
def translate_text(text, target_language="ur"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f" Translated text: {translation.text}")
    return translation.text


# Display language options to the user
def display_language_options():
    print("\n Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    print("9. Urdu (ur)")

    choice = input("Please select the target language number (1-9): ")
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
    
    # Default to Urdu ('ur') if invalid input is given
    return language_dict.get(choice, "ur")


# Main function
def main():
    # Step 1: Select language
    target_language = display_language_options()
    
    # Step 2: Listen to speech and convert to text
    original_text = speech_to_text()
    
    # Step 3: Translate and display text
    if original_text:
        translate_text(original_text, target_language=target_language)


if __name__ == "__main__":
    main()