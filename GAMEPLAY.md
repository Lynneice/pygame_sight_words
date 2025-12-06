# Sonic Sight Word Game - Gameplay Guide

## Visual Layout

```
╔════════════════════════════════════════════════════════════════════════════╗
║ Rings: 5                                                SPACE: Jump        ║
║ Speed: 4.2                                              R: Speak word      ║
║                                                         P: Pause            ║
║ ┌────────────────────────────────────────────────────┐ ESC: Quit          ║
║ │      Say the word: "the" (Press R to speak)        │                    ║
║ └────────────────────────────────────────────────────┘                    ║
║                                                                            ║
║    ☁️     ☁️          [the]         ☁️        [and]                      ║
║                         ○                       ○                          ║
║                                                                            ║
║                    🔵 Sonic                                                ║
║                                                                            ║
║          🌲      🌲        🌲            🌲         🌲                     ║
╠════════════════════════════════════════════════════════════════════════════╣
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣
╚════════════════════════════════════════════════════════════════════════════╝
```

## Game Flow

### 1. Starting the Game
```bash
python main.py
```

The game opens with:
- Blue background (sky gradient to green ground)
- Sonic starting at the left side of the screen
- Green hills in the background
- TTS announces: "Welcome to Sonic Sight Word Game!"

### 2. Gameplay Loop

#### When a Ring Appears:
```
Ring floating: [the]
           ○
```
- Ring appears on the right side of the screen
- Ring scrolls left at current game speed
- Ring has a bobbing animation

#### When Sonic Reaches the Ring:
```
Game speaks: "Say the word: the"
Screen shows: "Say the word: the (Press R to speak)"
```

#### Player Response:
1. **Press 'R' key** to activate microphone
2. Screen shows: "Listening... Say the word!"
3. **Speak the word** clearly into microphone
4. Game processes speech input

#### Correct Answer:
```
✓ "Correct! 'the'"
   Rings: 5 → 6
   Speed: 3.8 → 4.0
   Ring disappears
```

#### Incorrect Answer:
```
✗ "Wrong! You said 'they', expected 'the'"
   Rings: 5 → 4
   Speed: 4.0 → 3.5
```

### 3. Game Mechanics

#### Speed System:
```
Base Speed: 3.0
Max Speed:  10.0

Correct reading: +0.2 speed
Incorrect reading: -0.5 speed
```

#### Ring System:
```
Collect ring: +1 ring
Lose rings: -1 ring per mistake
Minimum rings: 0 (can't go negative)
```

### 4. Controls

| Key | Action |
|-----|--------|
| SPACE | Make Sonic jump |
| R | Start recording voice/speak word |
| P | Pause/unpause game |
| ESC | Quit game |

### 5. Sight Words Included

The game includes 50 common sight words:
```
the, and, a, to, said, in, he, I, of, it,
was, you, they, on, she, is, for, at, his, but,
that, with, all, we, can, are, up, had, my, her,
what, there, out, this, have, went, be, like, some, so,
not, then, were, go, little, as, no, or, one, do
```

### 6. Visual Elements

#### Sonic Character:
- Blue circle with lighter center
- Moves with physics (gravity, jumping)
- Position stays relatively fixed horizontally while world scrolls

#### Rings:
- Golden circle with hollow center
- Contain sight word in white text
- Bob up and down while scrolling
- Scroll left at game speed

#### Background:
- Sky: Blue gradient
- Ground: Green with hills
- Parallax scrolling effect

### 7. Example Play Session

```
[Start Game]
Rings: 0, Speed: 3.0

[Ring "the" appears]
TTS: "Say the word: the"
Player presses R, says "the"
✓ Correct!
Rings: 1, Speed: 3.2

[Ring "and" appears]
TTS: "Say the word: and"
Player presses R, says "an"
✗ Wrong! You said "an", expected "and"
Rings: 0, Speed: 2.7 (→ 3.0 base minimum)

[Ring "said" appears]
TTS: "Say the word: said"
Player presses R, says "said"
✓ Correct!
Rings: 1, Speed: 3.2

[Continue playing...]
```

### 8. Tips for Players

1. **Speak Clearly**: Enunciate each word clearly
2. **Quiet Environment**: Reduce background noise
3. **Watch the Speed**: As speed increases, rings come faster
4. **Use Jumping**: Jump over rings if you miss the timing
5. **Practice Makes Perfect**: Replay to improve reading fluency

### 9. Educational Benefits

- **Word Recognition**: Visual identification of sight words
- **Pronunciation**: Speaking words correctly
- **Reading Fluency**: Quick recognition under time pressure
- **Phonetic Awareness**: Matching spoken to written words
- **Confidence Building**: Positive reinforcement through gameplay

### 10. Troubleshooting

**Microphone Not Detected:**
- Check system microphone settings
- Ensure Python has microphone permissions
- Test with: `python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"`

**Words Not Recognized:**
- Speak closer to microphone
- Reduce background noise
- Speak more slowly and clearly
- Check internet connection (uses Google Speech API)

**Game Too Fast:**
- Focus on accuracy over speed
- Speed will decrease with mistakes
- Practice with easier words first

**Game Too Slow:**
- Keep playing to build up speed
- Get more words correct in a row
- Maximum speed is 10.0 (capped)
