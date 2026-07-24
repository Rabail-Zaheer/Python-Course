secret = 27
attempts = 5
count = 0

print("Welcome to the Number Guessing Game!")
print("Guess the secret number between 1 and 50.")

while count < attempts:
    guess = int(input("Enter your guess: "))
    count = count + 1

    if guess == secret:
        print("🎉 Congratulations! You guessed the correct number.")
        break

    else:
        # Find the difference without using abs()
        if guess > secret:
            difference = guess - secret
        else:
            difference = secret - guess

        # Hint system
        if difference <= 3:
            print("🔥 Hot")
        elif difference <= 7:
            print("🌡 Warm")
        else:
            print("🥶 Ice Cold")

        # Show remaining hearts
        print("Remaining Lives: ", end="")
        for i in range(attempts - count):
            print("❤️", end="")
        print()

if count == attempts and guess != secret:
    print("❌ You lost!")
    print("The secret number was", secret)