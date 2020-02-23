# Quzdra
Quzdra is a Python program that generates fake words in Russian. It can generate fake words similar to nouns, adjectives or verbs, and save it into txt file. Those fake words could be useful in automated tests, CAPTCHAs, and also scientific research.

## How to use Quzdra
Run ```quzdra.py``` script with specified arguments: part of speech for fake words (```a``` for adjectives, ```n``` for nouns, ```v``` for verbs), maximum fake word length and number of fake words to be generated.

Run the script from the command-line:
```
quzdra.py [part of speech: a|n|v] [length] [quantity]
```
The result will be stored in ```fakewords.txt``` file in the same directory where you saved Quzdra scripts.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
