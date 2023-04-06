import requests
from os import getenv
import base64
from threading import Thread
from modules.tts import play_voice
import re
from pathlib import Path

SPEAKERS_INPUT_ID = int(getenv('VOICEMEETER_INPUT_ID'))
APP_INPUT_ID = int(getenv('CABLE_INPUT_ID'))

def request(sentence):
    url = 'https://api.rinna.co.jp/models/cttse/koeiro'
    headers = {'Content-Type': 'application/json'}
    body = {'text': sentence, 'speaker_x': 1.02, 'speaker_y': 2.59, 'style': 'happy'}
    response = requests.post(url, headers=headers, json=body)
    base64_string = re.search('(?<=base64,)\\S+', response.text).group(0).replace('"', '')
    while len(base64_string) % 4 != 0:
        base64_string += '='
    decoded_audio = base64.b64decode(base64_string)
    output_file_path = Path(__file__).resolve().parents[2] / 'src' / 'audio' / 'tts.wav' # Update the output file path
    with open(output_file_path, 'wb') as f:  # Update the file path in the 'open' statement
        f.write(decoded_audio)
    threads = [Thread(target=play_voice, args=[APP_INPUT_ID]), Thread(target=play_voice, args=[SPEAKERS_INPUT_ID])]
    [t.start() for t in threads]
    [t.join() for t in threads]

if __name__ == '__main__':
    while True:
        input_sentence = input('English: ')
        request(input_sentence)
        with open(Path(__file__).resolve().parents[2] / 'src' / 'audio' / 'tts.wav', 'rb') as f:
            play_voice(APP_INPUT_ID, f.read())
