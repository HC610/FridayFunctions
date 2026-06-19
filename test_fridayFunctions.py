import pytest
from fridayfuncTest import (
    is_even,
    get_initials,
    find_longest_word,
    filter_even_numbers,
    count_vowels,
    count_words,
    most_common_item,
    is_palindrome,
    mask_email
)

# 1. is_even
def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False
    assert is_even(0) is True


# 2. get_initials
def test_get_initials():
    assert get_initials("Hassan Ahmed") == "HA"
    assert get_initials("john doe") == "JD"
    assert get_initials("  single ") == "S"


# 3. find_longest_word
def test_find_longest_word():
    assert find_longest_word(["apple", "banana", "kiwi"]) == "banana"
    assert find_longest_word(["a", "ab", "abc"]) == "abc"
    assert find_longest_word([]) == ""


# 4. filter_even_numbers
def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5]) == []
    assert filter_even_numbers([]) == []


# 5. count_vowels
def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("bcdfg") == 0


# 6. count_words
def test_count_words():
    assert count_words("apple banana apple") == {
        "apple": 2,
        "banana": 1
    }

    assert count_words("one one two") == {
        "one": 2,
        "two": 1
    }


# 7. most_common_item
def test_most_common_item():
    assert most_common_item([1, 2, 2, 3]) == 2
    assert most_common_item(["a", "b", "b", "c"]) == "b"
    assert most_common_item([]) is None


# 8. is_palindrome
def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False


# 9. mask_email
def test_mask_email():
    assert mask_email("hassan@example.com") == "h*****@example.com"
    assert mask_email("a@domain.com") == "a@domain.com"