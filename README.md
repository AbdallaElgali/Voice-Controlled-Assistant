# Voice-Controlled-Assistant

This Python script implements a voice-controlled assistant that can take orders for items from a predefined menu. The assistant uses speech recognition to understand user commands and responds accordingly.

## Features
- Speech recognition: The assistant uses the SpeechRecognition library to convert speech into text.
- Menu-based ordering: Users can place orders for items from a predefined menu by speaking their commands.
- Item recognition: The assistant recognizes item names from user commands and adds them to the order list.
- Order management: The assistant maintains an order list and displays the current order when requested.
- Voice feedback: The assistant provides voice feedback for user commands and responses using the gTTS library.

## Usage
1. Ensure that you have a working microphone connected to your computer.
2. Run the Python script.
3. The assistant will greet you and wait for your commands.
4. To place an order, say "I would like to order..." followed by the item you want to order.
5. The assistant will recognize the item name, add it to the order list, and provide confirmation.
6. To view your current order, say "I want to see my orders" or "Open my orders."
7. The assistant will display the current order list.
8. To exit the program, say "exit," "quit," "end," or "Goodbye Alexis."

## Requirements
Python 3.x
SpeechRecognition library
PyAudio library
playsound library
gTTS library



