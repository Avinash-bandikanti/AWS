numbers = []
words = []

# Input loop for numbers
while True:
    try:
        num_input = input("Enter a number (0 to stop): ")
        if num_input == '0':
            break

        num = float(num_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Input loop for words
while True:
    word_input = input("Enter a word (END to stop): ")
    if word_input == 'END':
        break
    words.append(word_input)

# Sort and print numbers
numbers.sort()
print("Ascending order of numbers:", numbers)
numbers.sort(reverse=True)
print("Descending order of numbers:", numbers)

# Sort and print words
words.sort()
print("Ascending order of words:", words)
words.sort(reverse=True)
print("Descending order of words:", words)
