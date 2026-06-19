# 1
def is_even(number):
    return number % 2 == 0

print(is_even(7))

# 2
def get_initials (word):
    return word[0]

print(get_initials("Hello"))

# # 3
statement = "Hello my name is Bob."

def find_longest_word():
    words = statement.split()
    longest_word = max(words, key=len)
    return longest_word

print(find_longest_word())

# # 4
def filter_even_numbers():
    numbers = [2, 3, 6, 7]
    return [num for num in numbers if num % 2 == 0]

print(filter_even_numbers())

#  5
def count_vowels():
    word = "hassan"
    count = 0

    for letter in word:
        if letter in "aeiou":
            count += 1

    return count

print(count_vowels())

# # 6
def count_words(sentence):
    words = sentence.split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(count_words("apple banana apple orange banana apple"))

# # 7
def most_common_item(items):
    counts = {}

    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return max(counts, key=counts.get)

print(most_common_item([1, 2, 2, 3, 2, 4, 1]))

# # 8
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))

# # 9
def mask_email(email):
    username, domain = email.split("@")

    masked_username = username[0] + "*" * (len(username) - 1)

    return masked_username + "@" + domain

print(mask_email("hassan@example.com"))
