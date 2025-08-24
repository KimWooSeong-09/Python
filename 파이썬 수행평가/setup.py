from setuptools import setup

APP = ['FourBasicOperations.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame', 'playsound'],
    'includes': ['pygame', 'playsound'],
    'codesign_identity': None,
    'codesign_entitlements': None,
}
DATA_FILES = [
    ('MP3', ['MP3/BGM.mp3', 'MP3/correct-6033.mp3', 'MP3/buzzer2-6109.mp3', 'MP3/Congratulation.mp3', '/Users/macbook/Desktop/전공 수업/Python/파이썬 수행평가/MP3/Solving Problem.mp3', '/Users/macbook/Desktop/전공 수업/Python/파이썬 수행평가/MP3/ultimatum-120bpm-orchestra-loop-325053.mp3']),
    ('.', ['game_scores.json'])
]

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
