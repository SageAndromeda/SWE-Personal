# with open("words.txt", "r") as f:
#     words = f.readlines()

# words = [w.strip() for w in words]

words = [  # Find only 5 letter words. Line curetousy of Stack Exchange
    word.rstrip("\n") for word in open("words.txt", "r") if len(word.rstrip("\n")) == 5
]  # https://stackoverflow.com/questions/57165720/python-code-should-only-output-5-character-long-words

print(len(words))
print(words[0:5])
exit(0)


def guess_word(game_state):
    return "steal"


if __name__ == "__main__":
    while True:
        state = input("Game state? ")
        guess = guess_word(state)
        print("You should try '" + guess + "'.")
