import pytest
from app import count

def test_count_zeros():
    assert count.count( [0,0,0], 0 ) == 3
