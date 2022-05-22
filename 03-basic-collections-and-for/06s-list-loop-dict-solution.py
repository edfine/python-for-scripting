# Don't look at this until you've attempted a solution yourself.

# Part 1: Lists, Loops, and aggregating

student_ages = [13, 7, 22, 28, 42]
list_sum = 0
for age in student_ages:
    list_sum += age

avg_age = list_sum / len(student_ages)

for age in student_ages:
    if age < avg_age:
        print(f'{age} is less than the avg age of {avg_age}')

## Part 2: Nested Data
dictionary_challenge = {
    'key': 'value',
    'hello': 'world',
    'target': [
        {
            'this_is': 'getting',
            'sort': 'of',
            'tricky': ['Hello Earth', 'Hello Detroit', 'Hello World!']
        },
        {
            'too': 'far'
        }
    ]
}

print(dictionary_challenge['hello']) # prints world
print(dictionary_challenge['target'][1]['too']) # prints far
print(dictionary_challenge['target'][0]['tricky'][2]) # prints Hello World!

# Part 2.2
dictionary_challenge['hello'] = 'friends'
dictionary_challenge['target'][1]['too'] = 'cool'
dictionary_challenge['target'][0]['tricky'][2] = 'So long and thanks for all the fish'

from pprint import pprint
pprint(dictionary_challenge)

# Part 3
words = [
    'apple',
    'soda',
    'car',
    'intrepid',
    'water',
    'buffalo',
    'tepid',
    'enemy',
    'salvo'
]

# Use a list comprehension to generate a list that has the same words, but in all capital letters.
capitalized = [word.upper() for word in words]
print(capitalized)

# Use a list comprehension to generate a list that only has the words which start with a vowel.
vowel_starters = [word for word in words if word[0] in 'aeiou']
print(vowel_starters)

# Use a dictionary comprehension to map the words (as keys) to the length of the word (as values)
lengths = {word: len(word) for word in words}
print(lengths)