"""
Assignment 10 Problems - Regex Questions
Python Version: 3.7.3
"""
import os
import re
from collections import defaultdict
from typing import Dict, List, Tuple


# -----------------------------
# Assignment 10 - RegEx Problems
# -----------------------------

def check_alphanumeric(text: str) -> bool:
    # 1. Check if a string contains only a-z, A-Z and 0-9
    return bool(re.match(r'^[a-zA-Z0-9]+$', text))

def match_a_followed_by_b_zero_or_more(text: str) -> bool:
    # 2. Match a followed by zero or more b's
    return bool(re.fullmatch(r'ab*', text))

def match_a_followed_by_b_one_or_more(text: str) -> bool:
    # 3. Match a followed by one or more b's
    return bool(re.fullmatch(r'ab+', text))

def find_lowercase_underscore(text: str) -> List[str]:
    # 4. Find lowercase sequences joined by underscore
    return re.findall(r'[a-z]+_[a-z]+', text)

def match_word_at_start(text: str) -> bool:
    # 5. Match a word at the beginning of a string
    return bool(re.match(r'^\w+', text))

def find_words_with_z(text: str) -> List[str]:
    # 6. Match words containing 'z'
    return re.findall(r'\b\w*z\w*\b', text)

def remove_leading_zeros(ip: str) -> str:
    # 7. Remove leading zeros from an IP address
    return '.'.join(str(int(octet)) for octet in ip.split('.'))

def search_literals(text: str, words: List[str]) -> Dict[str, bool]:
    # 8. Search for literal strings in a text
    return {word: bool(re.search(re.escape(word), text)) for word in words}

def search_literal_with_position(text: str, word: str) -> Tuple[bool, int]:
    # 9. Search for literal string & return match + position
    match = re.search(re.escape(word), text)
    return (bool(match), match.start()) if match else (False, -1)

def replace_space_comma_dot(text: str) -> str:
    # 10. Replace space, comma, or dot with colon
    return re.sub(r'[ ,.]+', ':', text)

def extract_date_from_url(url: str) -> Tuple[str, str, str]:
    # 11. Extract year, month, date from URL
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)
    return match.groups() if match else ('', '', '')

def find_words_starting_with_a_or_e(text: str) -> List[str]:
    # 12 & 14. Find all words starting with 'a' or 'e'
    return re.findall(r'\b[aeAE]\w*', text)

def remove_multiple_spaces(text: str) -> str:
    # 15. Remove multiple spaces
    return re.sub(r'\s+', ' ', text).strip()

def main():
    print("\n--- Assignment 10 RegEx Tests ---\n")
    print("1:", check_alphanumeric("ABCDEFabcdef123450"), check_alphanumeric("*&%@#!}{"))
    print("2:", [match_a_followed_by_b_zero_or_more(x) for x in ["ab", "abc", "a", "ab", "abb"]])
    print("3:", [match_a_followed_by_b_one_or_more(x) for x in ["ab", "abc", "a", "ab", "abb"]])
    print("4:", find_lowercase_underscore("aab_cbbbc aab_Abbbc Aaab_abbbc"))
    print("5:", match_word_at_start("The quick brown fox jumps"), match_word_at_start(" The quick brown fox jumps"))
    print("6:", find_words_with_z("The quick brown fox jumps over the lazy dog. Python Exercises."))
    print("7:", remove_leading_zeros("216.08.094.196"))
    print("8:", search_literals("The quick brown fox jumps over the lazy dog.", ['fox', 'dog', 'horse']))
    print("9:", search_literal_with_position("The quick brown fox jumps over the lazy dog.", 'fox'))
    print("10:", replace_space_comma_dot("Regular Expressions"), replace_space_comma_dot("Code_Examples"))
    print("11:", extract_date_from_url("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame/"))
    test_str = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added."
    print("12:", find_words_starting_with_a_or_e(test_str))
    print("13:", replace_space_comma_dot('Python Exercises, PHP exercises.'))
    print("14:", find_words_starting_with_a_or_e(test_str))
    print("15:", remove_multiple_spaces('Python      Exercises'))

if __name__ == '__main__':
    main()
