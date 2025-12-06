# Development Guide

## Project Structure

```
pygame_sight_words/
├── README.md              # User-facing documentation
├── GAMEPLAY.md           # Detailed gameplay guide
├── DEVELOPMENT.md        # This file - developer documentation
├── LICENSE               # License information
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore patterns
│
├── main.py              # Game launcher
├── demo_headless.py     # Headless demo for CI/testing
│
├── src/                 # Source code
│   ├── __init__.py
│   ├── game.py          # Main game class and loop
│   ├── sonic.py         # Sonic character with physics
│   ├── ring.py          # Ring class with sight words
│   ├── speech_handler.py # STT/TTS functionality
│   └── sprites.py       # Sprite generation utilities
│
├── tests/               # Unit tests
│   ├── __init__.py
│   ├── test_sonic.py    # Tests for Sonic character
│   ├── test_ring.py     # Tests for Ring class
│   ├── test_speech_handler.py # Tests for speech features
│   └── test_sprites.py  # Tests for sprite generation
│
└── assets/              # Game assets (currently empty)
    ├── images/          # Image files (sprites, backgrounds)
    └── sounds/          # Sound effects
```

## Architecture

### Game Loop (game.py)
The main game follows a standard game loop pattern:
1. **Event Handling** - Process keyboard input, window events
2. **Update** - Update game state, physics, collisions
3. **Draw** - Render all visual elements
4. **Clock Tick** - Maintain 60 FPS

### Physics System (sonic.py)
- Gravity-based physics with vertical velocity
- Ground collision detection
- Jump mechanics (only when on ground)
- Speed management system

### Speech Recognition (speech_handler.py)
- **TTS**: Uses `pyttsx3` for text-to-speech
- **STT**: Uses `SpeechRecognition` with Google's API
- Runs in separate threads to avoid blocking game loop
- Handles errors gracefully (no crash on missing microphone)

### Sprite System (sprites.py)
- Procedurally generated sprites (no image files required)
- Supports custom sizes and colors
- Uses per-pixel alpha for transparency

## Testing

### Running Tests
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_sonic.py

# Run specific test
pytest tests/test_sonic.py::TestSonic::test_sonic_jump

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Test Coverage
- **test_sonic.py**: 9 tests covering physics, speed, jumping
- **test_ring.py**: 8 tests covering rings, scrolling, words
- **test_speech_handler.py**: 9 tests (skipped without audio hardware)
- **test_sprites.py**: 8 tests covering sprite generation
- **Total**: 25 passing tests, 9 skipped (audio-dependent)

### Test Philosophy
- Unit tests focus on individual components
- Integration tests would require display/audio hardware
- Tests use fixtures for reusable test setup
- Audio tests are skipped gracefully when hardware unavailable

## Code Style

### Python Conventions
- Follow PEP 8 style guide
- Use docstrings for all classes and public methods
- Type hints are optional but encouraged
- Class names: PascalCase (e.g., `SonicSightWordGame`)
- Function names: snake_case (e.g., `collect_ring()`)
- Constants: UPPER_SNAKE_CASE (e.g., `SIGHT_WORDS`)

### Pygame Conventions
- Always call `pygame.init()` before creating surfaces
- Use sprite groups for efficient rendering
- Use `pygame.time.Clock` to control FPS
- Clean up with `pygame.quit()` when done

### Threading
- Use daemon threads for non-critical background tasks
- Speech operations run in threads to avoid blocking
- Main game loop remains single-threaded

## Dependencies

### Core Dependencies
```
pygame>=2.5.0           # Game engine
SpeechRecognition>=3.10.0  # Speech-to-text
pyttsx3>=2.90          # Text-to-speech
PyAudio>=0.2.13        # Audio capture (optional)
```

### Development Dependencies
```
pytest>=7.4.0          # Testing framework
```

### System Dependencies
On Linux, you may need:
```bash
sudo apt-get install python3-pyaudio portaudio19-dev
```

## Adding Features

### Adding New Sight Words
Edit `src/ring.py`:
```python
SIGHT_WORDS = [
    "the", "and", "a",  # Add new words here
    # ...
]
```

### Adding Custom Sprites
1. Place image in `assets/images/`
2. Load in `src/sprites.py`:
```python
def load_sprite(filename):
    path = os.path.join('assets', 'images', filename)
    return pygame.image.load(path)
```

### Adding Sound Effects
1. Place sound in `assets/sounds/`
2. Load and play in game:
```python
sound = pygame.mixer.Sound('assets/sounds/jump.wav')
sound.play()
```

### Adding New Game Mechanics
1. Add logic to appropriate class (Sonic, Ring, Game)
2. Write unit tests in `tests/`
3. Update documentation

## Performance Considerations

### Frame Rate
- Game targets 60 FPS
- Speech recognition runs in background threads
- Scrolling speed affects visual smoothness
- Test on target hardware to ensure 60 FPS maintained

### Memory Usage
- Sprite surfaces are created once and reused
- Background is pre-rendered for efficiency
- Ring sprites are created dynamically but cached

### Speech Recognition
- Uses Google's API (requires internet)
- Adds slight delay for recognition
- Threaded to avoid blocking game
- Falls back gracefully on errors

## Debugging

### Common Issues

**Game Won't Start:**
```python
# Check pygame initialization
import pygame
pygame.init()
print(pygame.get_sdl_version())
```

**No Audio Output:**
```python
# Test TTS
import pyttsx3
engine = pyttsx3.init()
engine.say("test")
engine.runAndWait()
```

**Microphone Not Working:**
```python
# List microphones
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
```

**Tests Failing:**
```bash
# Run with verbose output to see errors
pytest tests/ -v -s
```

### Debugging in Game
1. Enable debug prints in game.py
2. Use pygame's debugging features
3. Check console for error messages
4. Test components individually with demo_headless.py

## Contributing

### Before Submitting Changes
1. Run all tests: `pytest tests/`
2. Check code style: `python -m py_compile src/*.py`
3. Update documentation if needed
4. Test game manually if possible

### Adding Tests
- Write tests for new features
- Follow existing test patterns
- Use fixtures for common setup
- Skip tests that require hardware gracefully

## Future Enhancements

### Short Term
- [ ] Add actual Sonic sprites
- [ ] Add sound effects
- [ ] Add multiple difficulty levels
- [ ] Save high scores

### Long Term
- [ ] Multiple characters
- [ ] Power-ups and obstacles
- [ ] Multiplayer mode
- [ ] Level progression system
- [ ] Custom word lists
- [ ] Online leaderboards

## License
See LICENSE file for details.
