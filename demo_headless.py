#!/usr/bin/env python3
"""
Headless demo of game components for testing without display.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import pygame
from sonic import Sonic
from ring import Ring, create_ring_with_word
from sprites import create_sonic_sprite, create_ring_sprite
from speech_handler import SpeechHandler

# Initialize pygame in headless mode
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.init()

def demo_game_components():
    """Demonstrate game components without opening a window."""
    print("=" * 60)
    print("Sonic Sight Word Game - Component Demo")
    print("=" * 60)
    
    # Create sprites
    print("\n1. Creating Sonic sprite...")
    sonic_sprite = create_sonic_sprite()
    sonic = Sonic(100, 400, sonic_sprite)
    print(f"   ✓ Sonic created at position ({sonic.rect.x}, {sonic.rect.y})")
    print(f"   ✓ Initial speed: {sonic.speed}")
    print(f"   ✓ Initial rings: {sonic.ring_count}")
    
    # Test Sonic mechanics
    print("\n2. Testing Sonic mechanics...")
    sonic.collect_ring()
    print(f"   ✓ Collected 1 ring - Rings: {sonic.ring_count}, Speed: {sonic.speed:.1f}")
    
    for _ in range(5):
        sonic.collect_ring()
    print(f"   ✓ Collected 5 more rings - Rings: {sonic.ring_count}, Speed: {sonic.speed:.1f}")
    
    sonic.lose_rings(2)
    print(f"   ✓ Lost 2 rings - Rings: {sonic.ring_count}, Speed: {sonic.speed:.1f}")
    
    # Create rings
    print("\n3. Creating rings with sight words...")
    ring_sprite = create_ring_sprite()
    font = pygame.font.Font(None, 24)
    
    words = ["the", "and", "said", "cat", "dog"]
    rings = []
    for i, word in enumerate(words):
        ring = create_ring_with_word(100 + i * 80, 300, ring_sprite, font, word)
        rings.append(ring)
        print(f"   ✓ Ring {i+1}: '{ring.get_word()}'")
    
    # Test speech handler
    print("\n4. Testing Speech Handler...")
    try:
        handler = SpeechHandler()
        print("   ✓ SpeechHandler initialized")
        
        # Test word matching
        test_cases = [
            ("hello", "hello", True),
            ("HELLO", "hello", True),
            ("hello", "goodbye", False),
        ]
        
        print("   Testing word matching:")
        for spoken, target, expected in test_cases:
            result = handler.check_word_match(spoken, target)
            status = "✓" if result == expected else "✗"
            print(f"      {status} '{spoken}' vs '{target}': {result}")
        
    except Exception as e:
        print(f"   ⚠ SpeechHandler initialization skipped: {e}")
    
    # Test ring scrolling
    print("\n5. Testing ring scrolling...")
    test_ring = rings[0]
    initial_x = test_ring.rect.x
    test_ring.update(5)
    print(f"   ✓ Ring moved from x={initial_x} to x={test_ring.rect.x}")
    
    # Game statistics
    print("\n" + "=" * 60)
    print("Game Statistics:")
    print("=" * 60)
    print(f"  Total sight words available: {len(Ring.SIGHT_WORDS)}")
    print(f"  Sample words: {', '.join(Ring.SIGHT_WORDS[:10])}")
    print(f"  Sonic speed range: {sonic.base_speed} - {sonic.max_speed}")
    print(f"  Jump power: {abs(sonic.jump_power)}")
    print(f"  Gravity: {sonic.gravity}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully! ✓")
    print("=" * 60)
    print("\nTo play the actual game, run: python main.py")
    print("Note: Requires display, microphone, and speakers")


if __name__ == "__main__":
    demo_game_components()
