import os
import re
import subprocess
import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 16000
CHANNELS = 1
MIC_DEVICE = 1
RECORD_SECONDS = 5

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WHISPER_EXE = os.path.join(
    BASE_DIR,
    "whisper",
    "Release",
    "whisper-cli.exe"
)

WHISPER_MODEL = os.path.join(
    BASE_DIR,
    "whisper",
    "models",
    "ggml-tiny.en.bin"
)

AUDIO_FILE = os.path.join(
    BASE_DIR,
    "tests",
    "recording.wav"
)

def listen():
    print("\n🎤 Listening...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        device=MIC_DEVICE
    )

    sd.wait()

    write(AUDIO_FILE, SAMPLE_RATE, audio)

    print("🔄 Processing...")

    result = subprocess.run(
        [
            WHISPER_EXE,
            "-m",
            WHISPER_MODEL,
            "-f",
            AUDIO_FILE
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Whisper error:")
        print(result.stderr)
        return ""

    text_parts = []

    for line in result.stdout.splitlines():
        match = re.search(
            r"\[[0-9:.]+ --> [0-9:.]+\]\s*(.*)",
            line
        )

        if match:
            text = match.group(1).strip()

            if text:
                text_parts.append(text)

    return " ".join(text_parts).strip()