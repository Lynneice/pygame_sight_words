"""
Unit tests for SpeechHandler class.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from speech_handler import SpeechHandler


class TestSpeechHandler:
    """Test cases for SpeechHandler."""
    
    @pytest.fixture
    def handler(self):
        """Create a SpeechHandler instance for testing."""
        # Note: This will initialize TTS but not require microphone access
        try:
            return SpeechHandler()
        except Exception as e:
            pytest.skip(f"SpeechHandler initialization failed: {e}")
    
    def test_handler_initialization(self, handler):
        """Test that SpeechHandler initializes correctly."""
        assert handler is not None
        assert handler.recognizer is not None
        assert handler.tts_engine is not None
        assert handler.listening == False
        assert handler.last_recognized_text is None
    
    def test_check_word_match_exact(self, handler):
        """Test that exact matches work."""
        assert handler.check_word_match("hello", "hello") == True
    
    def test_check_word_match_case_insensitive(self, handler):
        """Test that matching is case-insensitive."""
        assert handler.check_word_match("Hello", "hello") == True
        assert handler.check_word_match("HELLO", "hello") == True
        assert handler.check_word_match("hello", "HELLO") == True
    
    def test_check_word_match_whitespace(self, handler):
        """Test that extra whitespace is handled."""
        assert handler.check_word_match("  hello  ", "hello") == True
        assert handler.check_word_match("hello", "  hello  ") == True
    
    def test_check_word_match_different(self, handler):
        """Test that different words don't match."""
        assert handler.check_word_match("hello", "goodbye") == False
        assert handler.check_word_match("cat", "dog") == False
    
    def test_check_word_match_none(self, handler):
        """Test that None values are handled correctly."""
        assert handler.check_word_match(None, "hello") == False
        assert handler.check_word_match("hello", None) == False
        assert handler.check_word_match(None, None) == False
    
    def test_is_listening_initial(self, handler):
        """Test that is_listening returns correct initial state."""
        assert handler.is_listening() == False
    
    def test_get_last_recognized_initial(self, handler):
        """Test that get_last_recognized returns None initially."""
        assert handler.get_last_recognized() is None
    
    def test_speak_does_not_crash(self, handler):
        """Test that speak method doesn't crash (runs async)."""
        # This just tests it doesn't crash, not that audio plays
        try:
            handler.speak("test")
            # Give it a moment to start the thread
            import time
            time.sleep(0.1)
        except Exception as e:
            pytest.fail(f"speak() raised exception: {e}")
    
    # Note: We don't test listen_for_word with actual microphone
    # as that would require hardware and user interaction
    # Those would be integration tests run manually
