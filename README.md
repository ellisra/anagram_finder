# Anagram Detector
## Problem Statement
Enclosed is a text file named “words”, with each line containing a single word. Your assignment is to develop a compact program that identifies all words in the list that have one or more anagrams.

Not all words have an anagram
We are only interested in single-word-anagrams

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

## Plan
- I essentially just need to iterate over the list of words and check if there is more than one instance of that set of characters in the list, if there is then I need to assign those instances to a dictionary
- I think the easiest way to do this would be to use the indexes of the words, i.e. the word "example" at index 22 has matches at index 35 & 24, the words at these indexes would then be added as values to the key of "example"
