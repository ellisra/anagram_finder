#!/usr/bin/evn python

import json

with open("words.txt", "rt", encoding="utf-8") as file:
    _WORDS = file.read().splitlines()

_SORTED_WORDS = ["".join(sorted(word)) for word in _WORDS]


def get_all_indexes(pattern: str) -> list[int]:
    return [idx for idx, word in enumerate(_SORTED_WORDS) if word == pattern]


words_dict = {word: [] for word in _WORDS}


for idx, word in enumerate(_WORDS):
    match_indexes = get_all_indexes("".join(sorted(word)))

    for matched_index in match_indexes:
        if matched_index != idx:
            words_dict[word].append(_WORDS[matched_index])

for key, values in words_dict.items():
    if values == []:
        continue

    print(f"{key}: {', '.join(values)}")

with open("output.json", "wt") as file:
    json.dump(words_dict, file, indent=2)
