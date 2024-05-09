import PIL
import cv2
from scipy.io.wavfile import write
import wavio as wv
import sounddevice as sd

def get_photo():
    result = False
    ttl = 0
    while not result and ttl < 100:
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        result, image = cam.read()
        ttl += 1
    if not result:
        return None
    return image


def get_voice():
    freq = 44100
    duration = 5
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()
    return bytes(recording)
