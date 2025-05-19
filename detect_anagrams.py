#!/usr/bin/evn python

import json
from collections import defaultdict


def get_all_anagrams(words: list[str]):
    """Checks all words in provided list to see if there are any anagrams present

    Args:
        words: List of individual words
    """
    # Create a dictionary of words grouped by their canonical representation
    anagram_groups = defaultdict(list)
    for word in words:
        anagram_groups["".join(sorted(word))].append(word)

    # Create a dictionary of words and their corresponding anagrams
    words_dict = {}
    for word in words:
        words_dict[word] = [
            anagram
            for anagram in anagram_groups["".join(sorted(word))]
            if anagram != word
        ]

    for word, anagrams in words_dict.items():
        if anagrams:
            print(f"{word}: {', '.join(anagrams)}")

    with open("output.json", "wt", encoding="utf-8") as file:
        json.dump(words_dict, file, indent=2)


if __name__ == "__main__":
    with open("words.txt", "rt", encoding="utf-8") as file:
        words = file.read().splitlines()

    get_all_anagrams(words)
