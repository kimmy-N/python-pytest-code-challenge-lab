import pytest
from palindrome import longest_palindromic_substring

def test_basic_cases():
    ans1 = longest_palindromic_substring("babad")
    assert ans1 in ["bab", "aba"]
    
    ans2 = longest_palindromic_substring("cbbd")
    assert ans2 == "bb"

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_characters():
    ans = longest_palindromic_substring("ac")
    assert ans in ["a", "c"]
    assert longest_palindromic_substring("aa") == "aa"

def test_entire_string_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_no_palindrome_greater_than_one():
    ans = longest_palindromic_substring("abcdefg")
    assert ans in ["a", "b", "c", "d", "e", "f", "g"]

def test_all_same_characters():
    assert longest_palindromic_substring("zzzzzz") == "zzzzzz"

def test_long_string():
    s = "a" * 1000
    assert longest_palindromic_substring(s) == s

def test_long_string_no_palindrome():
    s = "abcdefghijklmnopqrstuvwxyz" * 38 + "abcdef" 
    ans = longest_palindromic_substring(s)
    assert len(ans) == 1
    assert ans in s
