from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import asyncio
import pygame
import io
import sys


def capture_speech():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")

        try:
            # Adjust for ambient noise for better accuracy
            recognizer.adjust_for_ambient_noise(source)

            # Capture the audio input from the user
            audio = recognizer.listen(source, timeout=5)

            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio, language="en-US")

            # Output the transcribed text
            print("EN: " + text)
            return text

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Error: Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None


def translate_text(text, target_language="pt"):
    translator = Translator()

    try:
        # Translate the text to the target language (Portuguese by default)
        translated_text = translator.translate(text, dest=target_language)

        # Output the translated text
        print(f"{target_language.upper()}: {translated_text.text}")
        return translated_text.text

    except Exception as e:
        print(f"Translation Error: {e}")
        return None


def text_to_speech(text, lang="pt"):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue


def choose_target_language():
    language_mapping = {
            "english": "en",
            "portuguese": "pt",
            "spanish": "es",
            "french": "fr",
            "italian": "it",
            "german": "de",
            "russian": "ru",
            "chinese": "zh-cn",
            "japanese": "ja"
        }

    while True:
        language_input = capture_speech()
        if language_input:
            language_input = language_input.lower()
        if language_input in language_mapping:
            return language_mapping[language_input]
        else:
            text_to_speech("Invalid language choice. Please try again.", lang="en")


async def recognize_and_translate(activation_phrase="start translation", termination_phrase="stop translation", quit_phrase="quit program"):
    # State variable to track translation mode
    translation_active = False

    while True:
        if not translation_active:
            # Capture speech until "start translation" is heard
            text = capture_speech()
            if text and activation_phrase in text.lower():
                translation_active = True
                print("Translation activated")
                text_to_speech("Choose the target language", lang="en")

                # Prompt the user to choose the target language
                target_language = choose_target_language()
                text_to_speech("Translation started", lang="en")
            elif text and quit_phrase in text.lower():
                print("Quitting the program...")
                text_to_speech("bye bye!", lang="en")
                sys.exit()

        else:
            # Capture speech continuously and translate until "stop translation" is heard
            text = capture_speech()
            if text and termination_phrase in text.lower():
                translation_active = False
                print("Translation end")
                text_to_speech("Translation end", lang="en")
            elif text and quit_phrase in text.lower():
                print("Quitting the program...")
                text_to_speech("bye bye!", lang="en")
                sys.exit()
            else:
                translated_result = await asyncio.to_thread(translate_text, text, target_language)
                if translated_result:
                    text_to_speech(translated_result, lang=target_language)


def main():
    # Start the translation process in a new event loop
    asyncio.run(recognize_and_translate())


if __name__ == "__main__":
    main()
