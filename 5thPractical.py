def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))
no_lines = count_lines(content)
print("Number of lines =", no_lines)

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

#Finding most common words
from collections import Counter
def most_common_word(content):
    words = content.lower().split()
    return Counter(words).most_common(1)[0]
most_common_word, count = most_common_word(content)
print(f"The most common word is '{most_common_word}' with {count} occurrences.")

#5
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

#6
# def analyze_text(filename):
#     content = read_file(filename)
#     num_lines = count_lines (content)
#     num_words = count_words(content)
#     common_word, count = most_common_word(content)
#     avg_length = average_word_length(content)
    
#     print(f"File: {filename}")
#     print(f"Number of lines: {num_lines}")
#     print(f"Number of words: {num_words}")
#     print(f"Most common word: '{common_word}' (appears {count} times)")
#     print(f"Average word length: {avg_length:.2f} characters")

# # Run the analysis
# analyze_text('sample.txt')
