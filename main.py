import speech_recognition as sr
import pyaudio
import playsound
import os
import random
from gtts import gTTS
import time


r = sr.Recognizer()

# opening the text file and pulling out the data into a list to be understood by the program

Trial = open('Trial.txt')
item_list = []
for item in Trial:
    item_list.append(item.lower().rstrip())

capitalized_items = []

for item in item_list:
    capitalized_items.append(item.capitalize())

item_list = capitalized_items

num = 0

for a in item_list:
    num += 1
    if a == '':
        item_list.pop(num)

print(f'----------------MENU----------------\n')
num1 = 0
for listitem in item_list:
    num1 += 1
    print(f' {num1}.{listitem} ')
print('\n\n')


def there_exists_items(item_list):
    for x in item_list:
        if x in voice_data:
            return True


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


orders_list = []


# Creating an orders file with all orders given by voice
def my_order(orders_list):
    fhand2 = open('Orders.txt', 'w')
    fhand2.writelines(orders_list)
    fhand2 = open('Orders.txt')
    content = fhand2.read()
    fhand2.close()
    print(content)


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speaking_assistant(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='en-US, en-CA, en-GB, en-IN')
        except sr.UnknownValueError:
            speaking_assistant('I did not get that, try again')
        except sr.RequestError:
            speaking_assistant('My speech service is down, check your internet connection')
        return voice_data


def speaking_assistant(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



# Creating a function to guess the input based on the number of characters which are similar

def try_to_guess(word):

    word = word.strip()
    word_characters = [*word]  # extracting the characters in the given word
    similar = []



    for item_word in item_list:
        item_word_lower = item_word.lower()
        item_characters = [*item_word_lower]
        points = 0

        # Check for the length of each character's list, both inputted and item_characters and use the bigger one
        # as condition for loop

        if len(word_characters) >= len(item_characters):
            reference_list = word_characters
            reference = len(reference_list)
            other_list = item_characters

        else:
            reference_list = item_characters
            reference = len(reference_list)
            other_list = word_characters

        for character in range(reference):
            # compare each character of each word with the inputted word
            if reference_list[character] in other_list:
                points = points + 1  # points refer to the number of similar characters

            acc = points / reference  # check accuracy

            if acc >= 0.75 and item_word not in similar:
                similar.append((item_word, acc))

    if similar:
        similar = sorted(similar, key=lambda x: x[1], reverse=True)
        best_match, best_accuracy = similar[0]
        return best_match

    return word




def respond(voice_data):
    # Greeting
    if 'hello' in voice_data:
        speaking_assistant('hello, how can I help you?')
    if 'name' in voice_data:
        speaking_assistant('My name is Alexis')

    # Ordering Something
    if there_exists(['I would like to order', 'I want to order', 'Open a new order']):
        ordered_iteml = voice_data.split("order")
        ordered_iteml = [item.strip() for item in ordered_iteml]
        ordered_iteml.pop(0)  #considering there are only 2 items 1. whatever precedes "order" and 2. the order item
        ordered_item = ordered_iteml[0]

        ordered_item = try_to_guess(ordered_item)
        print(ordered_item)
        if ordered_item in item_list:
            speaking_assistant(f'I added {ordered_item} to your order')
            orders_list.append(' ' + ordered_item + '\n')
            my_order(orders_list)
        else:
            speaking_assistant(f'There is no {ordered_item} in the menu')
    if there_exists(['I want to see my orders', 'Open my orders', 'show me my orders']):
        print(orders_list)





time.sleep(0)
speaking_assistant('Speech Service Activated')
speaking_assistant('If you would like to order, ask me saying (I would like to order..) followed by your order :)')
while True:
    voice_data = record_audio()
    respond(voice_data)
    if there_exists(['exit', 'quit', 'end', 'Goodbye Alexis']):
        speaking_assistant('Going offline')
        break
