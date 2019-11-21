import pytest
from app import anti_vowel

def test_text():
    assert anti_vowel.anti_vowel("thing") == "thng"

def test_text():
    assert anti_vowel.anti_vowel("bob") == "bb"
