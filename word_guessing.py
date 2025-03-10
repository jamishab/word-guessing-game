import random
# dictionary of categories and words
word_categories = {"Technology": ["computer", "software", "hardware", "internet", "programming", "keyboard", "mouse", "monitor", "printer", "network", "phone", "tablet", "laptop", "watch", "television"],
                   "Car brands": ["ford", "chevrolet", "toyota", "honda", "nissan", "audi", "bmw", "lexus", "mercedes", "kia", "jeep"],
                   "Animals": ["dog", "cat", "bird", "fish", "elephant", "giraffe", "kangaroo", "koala", "penguin", "tiger", "snake", "owl"],
                   "Food": ["cheesedip", "dessert", "bacon", "pancakes", "eggs", "sandwich", "chicken", "pizza", "burger", "chicfila", "nuggets", "tacos", "noodles"],
                   "States": ["arkansas", "alabama", "louisiana", "florida", "texas", "california", "georgia", "nevada", "hawaii", "idaho"],
                   "Clothes": ["shirt", "shorts", "skirt", "shoes", "pants", "cardigan", "sweater", "dress", "undergarments"], 
}

#randomly select a category
category, words = random.choice(list(word_categories.items()))
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 3

guessed_letters = set()  # set to store guessed letters

print(f"Category: {category}")
print(f"The word has {len(word)} letters. First letter: {word[0]}, Last letter: {word[-1]}")

while "_" in guessed and attempts > 0:
    print("Word:", " ".join(guessed))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None yet'}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter! Try a different one.")
        continue # skip the rest of the loop

    # correct guess
    if guess in word:
        guessed_letters.add(guess)  # only store correct guesses
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = letter
    else:
        guessed_letters.add(guess) # store incorrect guesses too
        attempts -= 1
        print(f"Incorrect! You have {attempts} attempts left.")

if "_" not in guessed:
    print("Congrats! You correctly guessed the word:", word)
else:
    print("Game over! Sorry the word was:", word)