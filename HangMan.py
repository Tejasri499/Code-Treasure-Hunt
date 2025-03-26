# HANGMAN GAME  OR GUESS THE WORD 
import random 

hangman_art =   {0:("   ",
                    "   ",
                    "   "),

                1: (" o ",
                    "   ",
                    "   "),

                2: (" o ",
                    " | ",
                    "   "),

                3: (" o ",
                    "/| ",
                    "   "),

                4: (" o ",
                    "/|\\",
                    "   "),

                5: (" o ",
                    "/|\\",
                    "/  "),
                    
                6: (" o ",
                    "/|\\",
                    "/ \\")}

words = ("alligator", "ant","ape","badger", "bat", "bear", "bee", "bison", "boar", "buffalo", "butterfly", "camel","cat", "caterpillar", "cattle", "cheetah", "chicken", "chimpanzee", "clam", "cobra", "cockroach","crab", "crane","crocodile", "crow",
        "deer", "dinosaur", "dog", "dolphin", "donkey","eagle", "elephant","falcon", "fish", "flamingo", "fly", "fox", "frog", "giraffe","goat", "goldfish", "goose", "gorilla","grasshopper",
        "hamster", "hare", "hawk","hedgehog","horse", "human", "hummingbird", "hyena","jackal", "jaguar","jellyfish", "kangaroo", "kingfisher", "leopard", "lion","lobster",
        "mongoose", "monkey", "moose", "mosquito", "mouse", "octopus","ostrich","owl", "ox", "oyster", "panda", "panther", "parrot", "penguin", "pig", "pigeon", "polar-bear", "porpoise",
        "rabbit", "raccoon", "rat","red-deer", "red-panda", "reindeer", "rhinoceros","scorpion", "seahorse", "seal", "shark", "sheep", "snail", "snake", "sparrow", "spider","squid", "squirrel","swan", 
        "tiger","turkey", "turtle", "viper", "vulture", "walrus", "wasp" ,"whale", "wildcat", "wolf", "wolverine","worm", "yak", "zebra")


def dispaly_man(wrong_guesses):
    print("*********************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*********************")
        
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    running = True
    while running:
        dispaly_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a Letter: ").lower()
        # EDGE CASES FOR THE INPUT 
        if len(guess) =! 1 or not guess.isalpha():
            print("Invalid")
            continue
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue

        guessed_letter.add(guess) # TO THE GUESSED VALUES 
        # TO FLIP THE LETTER WITH THE EMPTY GAP
        if guess in answer :
            for idx in range(len(answer)) :
                if answer[idx] == guess:
                    hint[idx] = guess
        else :
            wrong_guesses++
        # TO CHECK WHETHER THE PLAYER WON OR LOSE
        if "_" not in hint :
            dispaly_man(wrong_guesses)
            display_answer(answer)
            print("YOU WON!!!")
            running = False
        elif wrong_guesses => len(hangman_art)-1:
            dispaly_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!!")
            running = False





if __name__ == "__main__":
    main()
