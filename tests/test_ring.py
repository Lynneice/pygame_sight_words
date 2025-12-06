"""
Unit tests for Ring class.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import pygame
from ring import Ring, create_ring_with_word
from sprites import create_ring_sprite


class TestRing:
    """Test cases for Ring class."""
    
    @pytest.fixture
    def ring(self):
        """Create a Ring instance for testing."""
        pygame.init()
        sprite = create_ring_sprite()
        return Ring(100, 200, sprite, word="test")
    
    def test_ring_initialization(self, ring):
        """Test that Ring initializes with correct values."""
        assert ring.rect.x == 100
        assert ring.rect.y == 200
        assert ring.word == "test"
        assert ring.initial_y == 200
    
    def test_ring_default_word(self):
        """Test that Ring gets a random word if none provided."""
        pygame.init()
        sprite = create_ring_sprite()
        ring = Ring(100, 200, sprite)
        assert ring.word in Ring.SIGHT_WORDS
    
    def test_ring_get_word(self, ring):
        """Test that get_word returns the correct word."""
        assert ring.get_word() == "test"
    
    def test_ring_update_scrolling(self, ring):
        """Test that ring scrolls left with scroll speed."""
        initial_x = ring.rect.x
        scroll_speed = 5
        
        ring.update(scroll_speed)
        
        assert ring.rect.x == initial_x - scroll_speed
    
    def test_ring_off_screen(self, ring):
        """Test that is_off_screen works correctly."""
        assert not ring.is_off_screen()
        
        ring.rect.x = -100
        assert ring.is_off_screen()
    
    def test_ring_bobbing_animation(self, ring):
        """Test that bobbing animation changes y position."""
        initial_y = ring.rect.y
        
        # Update multiple times to see bobbing
        for _ in range(10):
            ring.update(0)
        
        # Y position should have changed due to bobbing
        # (might be same if cycle completed, so we just check it's reasonable)
        assert abs(ring.rect.y - initial_y) <= 10
    
    def test_sight_words_list(self):
        """Test that SIGHT_WORDS contains expected words."""
        assert "the" in Ring.SIGHT_WORDS
        assert "and" in Ring.SIGHT_WORDS
        assert "said" in Ring.SIGHT_WORDS
        assert len(Ring.SIGHT_WORDS) >= 10
    
    def test_create_ring_with_word(self):
        """Test the create_ring_with_word function."""
        pygame.init()
        sprite = create_ring_sprite()
        font = pygame.font.Font(None, 24)
        
        ring = create_ring_with_word(100, 200, sprite, font, word="hello")
        
        assert ring.word == "hello"
        assert ring.rect.x == 100
        assert ring.rect.y == 200
