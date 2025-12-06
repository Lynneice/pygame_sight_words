"""
Main game class for Sonic Sight Word game.
"""
import pygame
import random
import threading
from sonic import Sonic
from ring import Ring, create_ring_with_word
from sprites import create_sonic_sprite, create_ring_sprite, create_background
from speech_handler import SpeechHandler


class SonicSightWordGame:
    """Main game class handling the game loop and logic."""
    
    def __init__(self, width=800, height=600):
        pygame.init()
        
        # Screen setup
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sonic Sight Word Game")
        
        # Clock for FPS
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        
        # Fonts
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
        # Ground level
        self.ground_level = self.height - 100
        
        # Create background
        self.background = create_background(self.width, self.height)
        self.bg_x = 0
        
        # Create Sonic
        sonic_sprite = create_sonic_sprite()
        self.sonic = Sonic(100, self.ground_level - 50, sonic_sprite)
        
        # Ring sprites group
        self.rings = pygame.sprite.Group()
        self.ring_sprite = create_ring_sprite(40, 40)
        
        # Speech handler
        self.speech_handler = SpeechHandler()
        
        # Game state
        self.running = True
        self.paused = False
        self.current_target_ring = None
        self.listening_for_word = False
        self.message = ""
        self.message_timer = 0
        self.message_color = self.WHITE
        
        # Ring spawning
        self.ring_spawn_timer = 0
        self.ring_spawn_interval = 120  # Frames between ring spawns
        
    def spawn_ring(self):
        """Spawn a new ring with a sight word."""
        x = self.width + 50
        y = random.randint(self.ground_level - 200, self.ground_level - 50)
        ring = create_ring_with_word(x, y, self.ring_sprite, self.font_small)
        self.rings.add(ring)
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.sonic.jump()
                elif event.key == pygame.K_r and self.current_target_ring:
                    # Start listening for word
                    self.start_listening()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
    
    def start_listening(self):
        """Start listening for speech in a separate thread."""
        if not self.listening_for_word and self.current_target_ring:
            self.listening_for_word = True
            self.message = "Listening... Say the word!"
            self.message_color = self.YELLOW
            self.message_timer = 180
            
            # Listen in a separate thread
            def listen_thread():
                spoken_word = self.speech_handler.listen_for_word(timeout=3, phrase_time_limit=3)
                self.process_speech_result(spoken_word)
            
            thread = threading.Thread(target=listen_thread)
            thread.daemon = True
            thread.start()
    
    def process_speech_result(self, spoken_word):
        """Process the result of speech recognition."""
        if self.current_target_ring is None:
            self.listening_for_word = False
            return
        
        target_word = self.current_target_ring.get_word()
        
        if spoken_word is None:
            self.message = "Couldn't hear you. Try again!"
            self.message_color = self.RED
            self.message_timer = 120
        elif self.speech_handler.check_word_match(spoken_word, target_word):
            # Correct!
            self.message = f"Correct! '{target_word}'"
            self.message_color = self.GREEN
            self.message_timer = 120
            self.sonic.collect_ring()
            self.current_target_ring.kill()
            self.current_target_ring = None
        else:
            # Incorrect
            self.message = f"Wrong! You said '{spoken_word}', expected '{target_word}'"
            self.message_color = self.RED
            self.message_timer = 120
            self.sonic.lose_rings(1)
        
        self.listening_for_word = False
    
    def update(self):
        """Update game state."""
        if self.paused:
            return
        
        # Update Sonic
        self.sonic.update(self.ground_level)
        
        # Update background scrolling
        scroll_speed = self.sonic.get_speed()
        self.bg_x -= scroll_speed
        if self.bg_x <= -self.width:
            self.bg_x = 0
        
        # Update rings
        for ring in self.rings:
            ring.update(scroll_speed)
            
            # Remove rings that are off screen
            if ring.is_off_screen():
                ring.kill()
        
        # Check for collision with rings
        if not self.current_target_ring:
            hit_rings = pygame.sprite.spritecollide(self.sonic, self.rings, False)
            if hit_rings:
                self.current_target_ring = hit_rings[0]
                word = self.current_target_ring.get_word()
                self.speech_handler.speak(f"Say the word: {word}")
                self.message = f"Say the word: {word} (Press R to speak)"
                self.message_color = self.WHITE
                self.message_timer = 300
        
        # Spawn new rings
        self.ring_spawn_timer += 1
        if self.ring_spawn_timer >= self.ring_spawn_interval:
            self.spawn_ring()
            self.ring_spawn_timer = 0
        
        # Update message timer
        if self.message_timer > 0:
            self.message_timer -= 1
            if self.message_timer == 0:
                self.message = ""
    
    def draw(self):
        """Draw everything to the screen."""
        # Draw background (with parallax effect)
        self.screen.blit(self.background, (self.bg_x, 0))
        self.screen.blit(self.background, (self.bg_x + self.width, 0))
        
        # Draw ground line
        pygame.draw.line(self.screen, self.BLACK, (0, self.ground_level), 
                        (self.width, self.ground_level), 3)
        
        # Draw rings
        self.rings.draw(self.screen)
        
        # Draw Sonic
        self.screen.blit(self.sonic.image, self.sonic.rect)
        
        # Draw HUD
        self.draw_hud()
        
        # Draw message
        if self.message:
            text_surface = self.font_medium.render(self.message, True, self.message_color)
            text_rect = text_surface.get_rect(center=(self.width // 2, 50))
            # Draw semi-transparent background for text
            bg_rect = text_rect.inflate(20, 10)
            bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
            bg_surface.fill((0, 0, 0, 180))
            self.screen.blit(bg_surface, bg_rect)
            self.screen.blit(text_surface, text_rect)
        
        # Draw pause message
        if self.paused:
            pause_text = self.font_large.render("PAUSED", True, self.WHITE)
            pause_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(pause_text, pause_rect)
        
        pygame.display.flip()
    
    def draw_hud(self):
        """Draw the heads-up display with game stats."""
        # Ring count
        ring_text = self.font_medium.render(f"Rings: {self.sonic.get_ring_count()}", 
                                           True, self.YELLOW)
        self.screen.blit(ring_text, (10, 10))
        
        # Speed
        speed_text = self.font_small.render(f"Speed: {self.sonic.get_speed():.1f}", 
                                           True, self.WHITE)
        self.screen.blit(speed_text, (10, 45))
        
        # Instructions
        instructions = [
            "SPACE: Jump",
            "R: Speak word",
            "P: Pause",
            "ESC: Quit"
        ]
        y_offset = self.height - 100
        for instruction in instructions:
            text = self.font_small.render(instruction, True, self.WHITE)
            self.screen.blit(text, (self.width - 150, y_offset))
            y_offset += 20
    
    def run(self):
        """Main game loop."""
        # Show welcome message
        self.speech_handler.speak("Welcome to Sonic Sight Word Game!")
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()


def main():
    """Entry point for the game."""
    game = SonicSightWordGame()
    game.run()


if __name__ == "__main__":
    main()
