"""
Speech recognition and text-to-speech handler for the sight word game.
"""
import speech_recognition as sr
import pyttsx3
import threading


class SpeechHandler:
    """Handles speech recognition (STT) and text-to-speech (TTS)."""
    
    def __init__(self):
        # Initialize recognizer for STT
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Initialize TTS engine
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)  # Speed of speech
        self.tts_engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
        
        # State
        self.listening = False
        self.last_recognized_text = None
        
    def speak(self, text):
        """Use text-to-speech to say the given text."""
        def _speak():
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        
        # Run in a separate thread to avoid blocking the game
        thread = threading.Thread(target=_speak)
        thread.daemon = True
        thread.start()
    
    def listen_for_word(self, timeout=3, phrase_time_limit=3):
        """
        Listen for speech input and return recognized text.
        Returns None if nothing is recognized or an error occurs.
        """
        if self.listening:
            return None
        
        self.listening = True
        recognized_text = None
        
        try:
            with self.microphone as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen for audio
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                
                # Recognize speech using Google's speech recognition
                recognized_text = self.recognizer.recognize_google(audio).lower()
                self.last_recognized_text = recognized_text
                
        except sr.WaitTimeoutError:
            # No speech detected within timeout
            pass
        except sr.UnknownValueError:
            # Speech was unintelligible
            pass
        except sr.RequestError as e:
            # API error
            print(f"Speech recognition error: {e}")
        except Exception as e:
            # Other errors (e.g., no microphone)
            print(f"Microphone error: {e}")
        finally:
            self.listening = False
        
        return recognized_text
    
    def is_listening(self):
        """Return whether currently listening for speech."""
        return self.listening
    
    def get_last_recognized(self):
        """Return the last recognized text."""
        return self.last_recognized_text
    
    def check_word_match(self, spoken_word, target_word):
        """
        Check if the spoken word matches the target word.
        Returns True if they match (case-insensitive).
        """
        if spoken_word is None or target_word is None:
            return False
        
        return spoken_word.lower().strip() == target_word.lower().strip()
