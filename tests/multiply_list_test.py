import pytest
from app import multiply_list

def test_multiply():
    assert multiply_list.product([5,5]) == 25
