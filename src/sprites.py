"""
Sprite generation for the Sonic sight word game.
Creates simple colored sprites when image files are not available.
"""
import pygame


def create_sonic_sprite(width=50, height=50):
    """Create a simple blue circle sprite representing Sonic."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    # Blue circle for Sonic
    pygame.draw.circle(surface, (0, 100, 255), (width // 2, height // 2), min(width, height) // 2)
    # Add white "belly"
    pygame.draw.circle(surface, (200, 220, 255), (width // 2, height // 2 + 5), min(width, height) // 3)
    return surface


def create_ring_sprite(width=30, height=30):
    """Create a golden ring sprite."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    # Golden ring
    pygame.draw.circle(surface, (255, 215, 0), (width // 2, height // 2), width // 2)
    pygame.draw.circle(surface, (0, 0, 0, 0), (width // 2, height // 2), width // 3)
    return surface


def create_background(width, height, color1=(135, 206, 235), color2=(100, 180, 100)):
    """Create a simple gradient background resembling Green Hill Zone."""
    surface = pygame.Surface((width, height))
    # Sky gradient
    for y in range(height // 2):
        color = (
            color1[0] + (color2[0] - color1[0]) * y // (height // 2),
            color1[1] + (color2[1] - color1[1]) * y // (height // 2),
            color1[2] + (color2[2] - color1[2]) * y // (height // 2),
        )
        pygame.draw.line(surface, color, (0, y), (width, y))
    
    # Ground
    ground_color = (50, 150, 50)
    pygame.draw.rect(surface, ground_color, (0, height // 2, width, height // 2))
    
    # Add some simple hills
    for i in range(0, width, 100):
        hill_color = (80, 180, 80)
        points = [(i, height // 2), (i + 50, height // 2 - 30), (i + 100, height // 2)]
        pygame.draw.polygon(surface, hill_color, points)
    
    return surface
