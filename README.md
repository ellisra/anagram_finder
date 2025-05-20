# Anagram Detector
## Problem Statement
Enclosed is a text file named “words”, with each line containing a single word. Your assignment is to develop a compact program that identifies all words in the list that have one or more anagrams.

- Not all words have an anagram
- We are only interested in single-word-anagrams

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once. (https://en.wikipedia.org/wiki/Anagram)

The result set should list, on each line, all the anagrams present in the attached file.
Example:
```
hawser, washer
caudolateral, laterocaudal
berust, stuber
anoetic, aconite, antoeci
sotnia, tinosa
togalike, goatlike
lonicera, acrolein
pannus, unsnap
```
The purpose of this task is to understand how you solve logical problems using programming. What is important to you when you code, and how well you can explain it. It’s preferable to use Python, but you can choose another language if you are more comfortable with it.

During the technical interview you will be asked to present the solution which will form the basis for a part of the conversation.

## Usage
> [!NOTE]
> I used `uv` to manage this project, but as no external dependencies were used it is not necessary for running the script.

1. Clone the repository and enter the directory
```bash
git clone git@github.com:ellisra/anagram_finder.git && cd anagram_finder
```
2. Ensure that `words.txt` is in the root directory of the project
3. Run the script
```bash
python3 detect_anagrams.py
```
The results will be printed to the terminal as well as being saved in a file named `output.json`.

## How it Works
The core of this solution is the use of canonical form to represent words. This way we sort the letters of all words alphabetically, allowing us to easily compare these canonical forms in order to determine if they are anagrams. To provide a better understanding of the solution I will explain the steps taken with a simple sample of words.

### Example
1. We start with a list of words read from `words.txt`, here is a smaller example list:
```python
words = ["bat", "race", "bird", "bride", "arc", "tab", "free", "acre", "care"]
```
2. We then sort their letters alphabetically and create a dictionary with these canonical forms being the keys and their matching words being the values:
```python
anagram_groups = {
    "abt":   ["bat",  "tab"],
    "acer":  ["race", "acre", "care"],
    "bdir":  ["bird"],
    "bdeir": ["bride"],
    "acr":   ["arc"],
    "eefr":  ["free"]
}
```
3. We can then create a new dictionary containing the original words as keys and words which match their canonical form (excluding themselves) as values:
```python
words_dict = {
    "bat":   ["tab"],
    "race":  ["acre", "care"],
    "bird":  [],
    "bride": [],
    "arc":   [],
    "tab":   ["bat"],
    "free":  [],
    "acre":  ["race", "care"],
    "care":  ["race", "acre"],
}
```
