"""
Unit tests for sprite generation module.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import pygame
from sprites import create_sonic_sprite, create_ring_sprite, create_background


class TestSpriteGeneration:
    """Test cases for sprite generation functions."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Initialize pygame before each test."""
        pygame.init()
    
    def test_create_sonic_sprite_default(self):
        """Test creating Sonic sprite with default size."""
        sprite = create_sonic_sprite()
        
        assert sprite is not None
        assert isinstance(sprite, pygame.Surface)
        assert sprite.get_width() == 50
        assert sprite.get_height() == 50
    
    def test_create_sonic_sprite_custom_size(self):
        """Test creating Sonic sprite with custom size."""
        sprite = create_sonic_sprite(width=100, height=80)
        
        assert sprite is not None
        assert sprite.get_width() == 100
        assert sprite.get_height() == 80
    
    def test_create_ring_sprite_default(self):
        """Test creating ring sprite with default size."""
        sprite = create_ring_sprite()
        
        assert sprite is not None
        assert isinstance(sprite, pygame.Surface)
        assert sprite.get_width() == 30
        assert sprite.get_height() == 30
    
    def test_create_ring_sprite_custom_size(self):
        """Test creating ring sprite with custom size."""
        sprite = create_ring_sprite(width=50, height=50)
        
        assert sprite is not None
        assert sprite.get_width() == 50
        assert sprite.get_height() == 50
    
    def test_create_background_default(self):
        """Test creating background with default colors."""
        width, height = 800, 600
        background = create_background(width, height)
        
        assert background is not None
        assert isinstance(background, pygame.Surface)
        assert background.get_width() == width
        assert background.get_height() == height
    
    def test_create_background_custom_colors(self):
        """Test creating background with custom colors."""
        width, height = 640, 480
        color1 = (255, 0, 0)
        color2 = (0, 255, 0)
        background = create_background(width, height, color1, color2)
        
        assert background is not None
        assert background.get_width() == width
        assert background.get_height() == height
    
    def test_sonic_sprite_has_transparency(self):
        """Test that Sonic sprite supports transparency."""
        sprite = create_sonic_sprite()
        
        # Check that surface supports per-pixel alpha
        assert sprite.get_flags() & pygame.SRCALPHA
    
    def test_ring_sprite_has_transparency(self):
        """Test that ring sprite supports transparency."""
        sprite = create_ring_sprite()
        
        # Check that surface supports per-pixel alpha
        assert sprite.get_flags() & pygame.SRCALPHA
