"""
Sonic character class for the sight word game.
"""
import pygame


class Sonic(pygame.sprite.Sprite):
    """Sonic character that gains speed by collecting rings."""
    
    def __init__(self, x, y, sprite_surface):
        super().__init__()
        self.image = sprite_surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement and physics
        self.velocity_y = 0
        self.base_speed = 3
        self.speed = self.base_speed
        self.jump_power = -15
        self.gravity = 0.8
        self.on_ground = False
        
        # Game state
        self.ring_count = 0
        self.max_speed = 10
        
    def jump(self):
        """Make Sonic jump if on the ground."""
        if self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False
    
    def update(self, ground_level):
        """Update Sonic's position and physics."""
        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        
        # Check ground collision
        if self.rect.bottom >= ground_level:
            self.rect.bottom = ground_level
            self.velocity_y = 0
            self.on_ground = True
        
        # Keep Sonic on screen horizontally
        if self.rect.left < 0:
            self.rect.left = 0
    
    def collect_ring(self):
        """Increase speed when collecting a ring correctly."""
        self.ring_count += 1
        if self.speed < self.max_speed:
            self.speed = min(self.speed + 0.2, self.max_speed)
    
    def lose_rings(self, amount=1):
        """Decrease speed when losing rings."""
        self.ring_count = max(0, self.ring_count - amount)
        self.speed = max(self.base_speed, self.speed - 0.5)
    
    def get_speed(self):
        """Return current speed."""
        return self.speed
    
    def get_ring_count(self):
        """Return current ring count."""
        return self.ring_count
