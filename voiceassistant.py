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


# NEW: Get text by typing
def typed_input():
    text = input("\nPlease type your sentence in English: ")
    print(f"✅ You typed: {text}")
    return text


# Translate text using Google Translate API
def translate_text(text, target_language="ur"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text


# Display language options to the user
def display_language_options():
    print("\nAvailable translation languages:")
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


# NEW: Display translation history
def display_history(history):
    print("\n========== TRANSLATION HISTORY ==========")

    if not history:
        print("No translations yet.")
    else:
        for i, item in enumerate(history, start=1):
            print(f"\n{i}. Original: {item['original']}")
            print(f"   Translation: {item['translation']}")


def main():

    # NEW: Create an empty list to store translation history
    history = []

    # Step 1: Select language
    target_language = display_language_options()

    # NEW: Select input method
    print("\nChoose input method:")
    print("1. Speak")
    print("2. Type")

    input_choice = input("Please select 1 or 2: ")

    # NEW: Get input using the selected method
    if input_choice == "1":
        original_text = speech_to_text()

    elif input_choice == "2":
        original_text = typed_input()

    else:
        print("Invalid choice. Using typing as default.")
        original_text = typed_input()

    # Step 3: Translate and display text
    if original_text:

        translated_text = translate_text(
            original_text,
            target_language=target_language
        )
        # NEW: Save translation in history
        history.append({
            "original": original_text,
            "translation": translated_text
        })

    # NEW: Ask whether user wants to see history
    show_history = input("\nWould you like to see your translation history? (y/n): ")

    if show_history.lower() == "y":
        display_history(history)

if __name__ == "__main__":
    main()