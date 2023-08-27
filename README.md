# Speech-To-Speech Translation Tool

This project implements a Speech-To-Speech Translation tool that allows users to speak in one language, have their speech recognized, translated into another language, and optionally output as audio. The tool uses speech recognition and translation APIs, enabling real-time communication across different languages.

## Features

- Real-time speech recognition using Google Web Speech API.
- Language translation using Google Translate API.
- Optional text-to-speech conversion using gTTS and Pygame libraries.
- User-friendly interface with voice prompts and responses.

## Requirements

- Python 3.x
- Libraries: `googletrans`, `speech_recognition`, `gtts`, `pygame`

## Usage

1. Install the required libraries using the following command:

	```bash
	pip install googletrans SpeechRecognition gtts pygame
	```

2. Run the script:

	```bash
	python sps.py
	```

3. Follow the voice prompts:

	Say "start translation" to activate translation mode.
	Choose the target language by speaking the language name (e.g., "english", "spanish").
	Start speaking in the source language to get real-time translations.
	Say "stop translation" to end translation mode.
	Say "quit program" to exit the tool.

## Notes

- Ensure you have an active internet connection to use Google Web Speech and Translate APIs.

- Language choices: English, Portuguese, Spanish, French, Italian, German, Russian, Chinese, Japanese.

- The tool supports continuous translation until "stop translation" is heard.
Translated text can be output as audio using text-to-speech conversion.