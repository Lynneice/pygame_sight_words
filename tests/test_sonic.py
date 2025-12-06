"""
Unit tests for Sonic character class.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import pygame
from sonic import Sonic
from sprites import create_sonic_sprite


class TestSonic:
    """Test cases for Sonic character."""
    
    @pytest.fixture
    def sonic(self):
        """Create a Sonic instance for testing."""
        pygame.init()
        sprite = create_sonic_sprite()
        return Sonic(100, 400, sprite)
    
    def test_sonic_initialization(self, sonic):
        """Test that Sonic initializes with correct values."""
        assert sonic.rect.x == 100
        assert sonic.rect.y == 400
        assert sonic.ring_count == 0
        assert sonic.speed == sonic.base_speed
        assert sonic.on_ground == False
    
    def test_sonic_collect_ring(self, sonic):
        """Test that collecting rings increases count and speed."""
        initial_speed = sonic.speed
        initial_count = sonic.ring_count
        
        sonic.collect_ring()
        
        assert sonic.ring_count == initial_count + 1
        assert sonic.speed > initial_speed
    
    def test_sonic_lose_rings(self, sonic):
        """Test that losing rings decreases count and speed."""
        # First collect some rings
        for _ in range(5):
            sonic.collect_ring()
        
        initial_speed = sonic.speed
        initial_count = sonic.ring_count
        
        sonic.lose_rings(2)
        
        assert sonic.ring_count == initial_count - 2
        assert sonic.speed < initial_speed
    
    def test_sonic_lose_rings_min_zero(self, sonic):
        """Test that ring count doesn't go below zero."""
        sonic.lose_rings(10)
        assert sonic.ring_count == 0
    
    def test_sonic_speed_cap(self, sonic):
        """Test that speed doesn't exceed max_speed."""
        # Collect many rings
        for _ in range(100):
            sonic.collect_ring()
        
        assert sonic.speed <= sonic.max_speed
    
    def test_sonic_jump(self, sonic):
        """Test that Sonic can jump when on ground."""
        sonic.on_ground = True
        sonic.velocity_y = 0
        
        sonic.jump()
        
        assert sonic.velocity_y < 0
        assert sonic.on_ground == False
    
    def test_sonic_cant_double_jump(self, sonic):
        """Test that Sonic can't jump while in air."""
        sonic.on_ground = False
        sonic.velocity_y = 5
        
        initial_velocity = sonic.velocity_y
        sonic.jump()
        
        assert sonic.velocity_y == initial_velocity
    
    def test_sonic_gravity(self, sonic):
        """Test that gravity affects Sonic."""
        sonic.velocity_y = 0
        ground_level = 500
        
        sonic.update(ground_level)
        
        # After one update, velocity should increase due to gravity
        assert sonic.velocity_y > 0
    
    def test_sonic_ground_collision(self, sonic):
        """Test that Sonic stops at ground level."""
        ground_level = 500
        sonic.rect.y = 600  # Below ground
        sonic.velocity_y = 10
        
        sonic.update(ground_level)
        
        assert sonic.rect.bottom == ground_level
        assert sonic.velocity_y == 0
        assert sonic.on_ground == True
