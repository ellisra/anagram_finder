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
