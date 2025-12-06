"""
Ring class with sight words for the game.
"""
import pygame
import random


class Ring(pygame.sprite.Sprite):
    """Ring with a sight word that Sonic can collect."""
    
    # Common sight words for early readers
    SIGHT_WORDS = [
        "the", "and", "a", "to", "said", "in", "he", "I", "of", "it",
        "was", "you", "they", "on", "she", "is", "for", "at", "his", "but",
        "that", "with", "all", "we", "can", "are", "up", "had", "my", "her",
        "what", "there", "out", "this", "have", "went", "be", "like", "some", "so",
        "not", "then", "were", "go", "little", "as", "no", "or", "one", "do"
    ]
    
    def __init__(self, x, y, sprite_surface, word=None):
        super().__init__()
        self.image = sprite_surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Assign a sight word
        self.word = word if word else random.choice(self.SIGHT_WORDS)
        
        # Animation properties
        self.bob_offset = 0
        self.bob_speed = 0.1
        self.initial_y = y
        
    def update(self, scroll_speed):
        """Update ring position (scrolling and bobbing animation)."""
        # Move left with the scrolling background
        self.rect.x -= scroll_speed
        
        # Bobbing animation
        self.bob_offset += self.bob_speed
        self.rect.y = self.initial_y + int(5 * pygame.math.Vector2(0, 1).rotate(self.bob_offset * 10).y)
    
    def get_word(self):
        """Return the sight word for this ring."""
        return self.word
    
    def is_off_screen(self):
        """Check if ring has scrolled off the left side of the screen."""
        return self.rect.right < 0


def create_ring_with_word(x, y, sprite_surface, font, word=None):
    """Create a ring sprite with text rendered on it."""
    ring = Ring(x, y, sprite_surface, word)
    
    # Create a surface with the word rendered
    text_surface = font.render(ring.word, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(ring.rect.width // 2, ring.rect.height // 2))
    
    # Composite the text onto the ring
    ring_with_text = ring.image.copy()
    ring_with_text.blit(text_surface, text_rect)
    ring.image = ring_with_text
    
    return ring
