from os import getenv
from pathlib import Path
from dotenv import load_dotenv
import soundfile as sf
import sounddevice as sd
from pynput.keyboard import Controller
from .logger import logger

load_dotenv()

TTS_WAV_PATH = Path(__file__).resolve(
).parent.parent / 'audio' / r'tts.wav'

# Keyboard
INGAME_PUSH_TO_TALK_KEY = getenv('INGAME_PUSH_TO_TALK_KEY')
keyboard = Controller()

# Audio devices
CABLE_INPUT_ID = int(getenv('CABLE_INPUT_ID'))


def play_voice(device_id):
    data, fs = sf.read(TTS_WAV_PATH, dtype='float32')

    if INGAME_PUSH_TO_TALK_KEY:
        keyboard.press(INGAME_PUSH_TO_TALK_KEY)

    logger.info("speaking now..")
    sd.play(data, fs, device=device_id, blocking=True)
    # sd.wait()
    logger.info("finished speaking")

    if INGAME_PUSH_TO_TALK_KEY:
        keyboard.release(INGAME_PUSH_TO_TALK_KEY)

