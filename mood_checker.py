import random


# Function to read quotes from a file
def read_quotes_from_file(file_path):
    with open(file_path, 'r') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes if quote.strip()]


# Read quotes from files
happy_ok_quotes = read_quotes_from_file('forhappyok.txt')
sad_quotes = read_quotes_from_file('forsaddays.txt')


# Function to get a random quote based on mood
def get_random_quote(mood):
    if mood == "sad":
        return random.choice(sad_quotes)
    else:
        return random.choice(happy_ok_quotes)


def main():
    print("Welcome to a new day!")
    print()

    mood = input("How are you feeling so far? Are you happy, okay, or sad?: ").lower()
    if mood == '':
        print("Have a beautiful day ahead!")
        return

    if mood in ["happy", "okay"]:
        print()
        print("Keep that light within you that shines and emits all colors of the rainbow.")
        quote = get_random_quote(mood)
        print()
        print(f"Just want to share a random quote: {quote}")
        print()
    elif mood == "sad":
        quote = get_random_quote(mood)
        print()
        print(f"It seems you're dealing with a lot at the moment.")
        print(f"Just want to point out: {quote}")
        print()
    else:
        print("Please enter 'happy', 'sad', 'okay' next time.")

    print("Wishing you a fantabulous day!")
    print()


if __name__ == "__main__":
    main()