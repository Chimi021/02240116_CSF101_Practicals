# E1
# Modify the program to count the number of unique words in the text.
# Add a function to find the longest word in the text.
# Implement a feature to count the occurrences of a specific word (case-insensitive).
# Create a function to calculate the percentage of words that are longer than the average word length.

# def read(f):
#     with open (f,'r') as file:
#         return file.read()
# c = read('sample.txt')
# # print (c)
# from collections import Counter
# def most_unique_word(c):
#     c = list
#     unique = []
#     for words in list :
#         word_count= 0
#     for words in unique:
#         word_count += 1
#     return word_count
#     # word = c.lower().split()
#     # return Counter(word).most_common()[0]
# u = most_unique_word(c)
# print("most common word is", u)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
content = read_file('sample.txt')
print(content[:100])
    
def count_lines(content):
        return len(content.split('\n'))
no_lines = count_lines(content)
print("Number of lines =", no_lines)

def count_words(content):
    return len(content.split())
# 
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

#Finding most common words
from collections import Counter
def most_common_word(content):
    words = content.lower().split()
    return Counter(words).most_common(1)[0]
# most_common_word, count = most_common_word(content)
# print(f"The most common word is '{most_common_word}' with {count} occurrences.")


def unique_word(content):
    words = set(content.lower().split()) # set removes duplicates
    return len(words)

def longest_word(content):
    words = content.split()
    return max(words, key=len, default="")

# max(words, key=len, default="")
# max(iterable, key=function, default=value) is used to find the largest element in an iterable.
# words: The list of words.
# key=len: Specifies that the maximum value should be determined based on word length (instead of alphabetic order
# How key=len Works
# Normally, max() compares elements directly (e.g., max([3, 1, 5]) gives 5).
# Here, key=len tells max() to compare word lengths instead of the words themselves
# default="": Ensures that if words is empty (like in an empty file), the function returns an empty string instead of causing an error.
# default="" makes sure that max() returns an empty string instead of crashing

def word_occurrences(content, target_word):
    words = content.lower().split()
    return words.count(target_word.lower())

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words) * 100) if words else 0

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    unique_words = unique_word(content)
    longest = longest_word(content)
    percentage_long = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {unique_words}")
    print(f"Longest word: '{longest}'")
    print(f"Percentage of words longer than average: {percentage_long:.2f}%")

    # Example for specific word occurrences
    target_word = "example"  # Change this word as needed
    occurrences = word_occurrences(content, target_word)
    print(f"Occurrences of '{target_word}': {occurrences}")

# Run the analysis
analyze_text('sample.txt')

# def most_unique_word (c):
#     Unique = []
#     Unique.append(c[0])
#     for i in range (len(c)):
#         for j in range(len(Unique)):
#             if  c[i] == Unique[j]:
#                 pass
#             else:
#                 Unique.append(c[i])
#                 print (Unique[j])

# Unique_words = most_unique_word(c)
# print (Unique_words)




# from collections import Counter
# def longest_word(c):
#     lw = c.lower().split()
#     return Counter(lw)
# l = longest_word
# print (l)


# def average_word_length(c):
#     words = c.split()
#     total_length = sum(len(word) for word in words)
#     return total_length / len(words)

# # Test the function
# avg_length = average_word_length(c)
# print(f"Average word length: {avg_length:.2f} characters")

# def persentage (c):
#     if avg_length > 


