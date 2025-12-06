# Sonic Sight Word Game

A fun educational game inspired by Sonic the Hedgehog and Green Hill Zone, where players learn sight words through speech recognition!

## Game Overview

Help Sonic collect rings by reading sight words correctly! Sonic gains speed as he collects more rings, but loses rings and slows down when words are read incorrectly.

### Features

- **Classic Sonic Gameplay**: Side-scrolling platformer with jumping mechanics
- **Educational**: Teaches common sight words for early readers
- **Speech Recognition**: Uses STT (Speech-To-Text) to detect spoken words
- **Text-to-Speech**: TTS announces words that need to be read
- **Progressive Difficulty**: Sonic's speed increases with successful collections
- **Green Hill Zone Theme**: Inspired by the classic Sonic level

## Requirements

- Python 3.7+
- Microphone for speech recognition
- Speakers/headphones for audio output

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lynneice/pygame_sight_words.git
cd pygame_sight_words
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note**: On Linux, you may need to install additional audio dependencies:
```bash
# For Ubuntu/Debian
sudo apt-get install python3-pyaudio portaudio19-dev

# For Fedora
sudo dnf install python3-pyaudio portaudio-devel
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. **Controls**:
   - **SPACE**: Make Sonic jump
   - **R**: Start speaking/record your voice
   - **P**: Pause the game
   - **ESC**: Quit the game

3. **Gameplay**:
   - Sonic runs automatically and rings appear with sight words
   - When Sonic reaches a ring, the word will be announced
   - Press **R** and say the word out loud
   - If correct, Sonic collects the ring and gains speed
   - If incorrect, Sonic loses rings and slows down

## Game Mechanics

- **Ring Collection**: Correct word reading = +1 ring, +0.2 speed
- **Ring Loss**: Incorrect reading = -1 ring, -0.5 speed
- **Speed Range**: 3.0 (base) to 10.0 (maximum)
- **Sight Words**: 50 common words for early readers

## Testing

Run the test suite:
```bash
pytest tests/
```

Run specific test files:
```bash
pytest tests/test_sonic.py
pytest tests/test_ring.py
pytest tests/test_speech_handler.py
```

## Project Structure

```
pygame_sight_words/
├── main.py                 # Game launcher
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── src/                   # Source code
│   ├── game.py           # Main game class and loop
│   ├── sonic.py          # Sonic character class
│   ├── ring.py           # Ring class with sight words
│   ├── speech_handler.py # Speech recognition and TTS
│   └── sprites.py        # Sprite generation
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── test_sonic.py
│   ├── test_ring.py
│   └── test_speech_handler.py
└── assets/                # Game assets (images, sounds)
    ├── images/
    └── sounds/
```

## Troubleshooting

### Microphone Not Working
- Ensure your microphone is properly connected and selected as the default input device
- Check microphone permissions for Python
- Test your microphone with other applications first

### Speech Recognition Errors
- The game uses Google's speech recognition API, which requires an internet connection
- Speak clearly and close to the microphone
- Reduce background noise

### Audio Issues
- Ensure speakers/headphones are connected
- Check system audio settings
- Verify pyttsx3 is working: `python -c "import pyttsx3; e=pyttsx3.init(); e.say('test'); e.runAndWait()"`

## Educational Value

This game helps children:
- Practice sight word recognition
- Improve reading fluency
- Develop phonetic awareness
- Build confidence in reading aloud
- Associate fun gameplay with learning

## Future Enhancements

- [ ] Add more sight word lists (beginner, intermediate, advanced)
- [ ] Include actual Sonic sprites and animations
- [ ] Add sound effects for jumps, ring collection, etc.
- [ ] Implement multiple levels with different backgrounds
- [ ] Add high score tracking
- [ ] Include power-ups and obstacles
- [ ] Multiplayer mode

## Credits

Inspired by Sonic the Hedgehog by SEGA.
Built with Pygame, SpeechRecognition, and pyttsx3.

## License

See LICENSE file for details.
