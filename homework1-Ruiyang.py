# PPHA 30537
# Spring 2024
# Homework 1

# Ruiyang Shi
# RuiyangShi2020

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

list = ['monkey', 'cat', 'dog', 'lion']

for i in range(len(list)):
    print(f"The value at position {i} is {list[i]}")


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

def is_palindrome(s):
    clean_s = ''.join(c for c in s if c.isalnum()).lower()
    return clean_s == clean_s[::-1]

test_strings = [
    "radar",
    "A man, a plan, a canal, Panama!",
    "Microsoft",
    "This isn't a palindrome"
]

for string in test_strings:
    print(f"The string '{string}' is a palindrome: {is_palindrome(string)}")

# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')

def get_vegetable_choice():
    available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
    
    while available_vegetables:
        choice = input("Please pick a vegetable I have available: ")
        if choice in available_vegetables:
            print(f"You can have the vegetable: {choice}")
            available_vegetables.remove(choice)
        else:
            print(f"{choice} is not a valid choice. Please pick again.")
    
    print("All vegetables have been selected.")

print(get_vegetable_choice())

# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

strings = ["bee", "Butterfly", "Cow", "donkey", "turkey", "Zebra"]
lowercase_strings = [s.lower() for s in strings if not s.lower().startswith(('a', 'b'))]
print(lowercase_strings)

# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

short_names = ['IL', 'IN', 'MI', 'WI']
long_names = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

state_dict = {short: long for short, long in zip(short_names, long_names)}
print(state_dict)

#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def evaluate_sum(a, b):
    total = a + b
    if total > 10:
        return "big"
    elif total == 10:
        return "just right"
    else:
        return "small"
start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]
result_list = [evaluate_sum(a, b) for a, b in start_list]
print(result_list)

# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()

def my_func(a):
    b = 40
    return a + b

x = my_func(10)
print(x)

# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random
  
import random
import string
def generate_password(length=8, special_chars=True, numbers=True):
    if not 8 <= length <= 16:
        return "Password length must be between 8 and 16 characters."
    chars = string.ascii_letters
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
password1 = generate_password()
password2 = generate_password(16)
password3 = generate_password(12, special_chars=False)
password4 = generate_password(10, numbers=False)
password5 = generate_password(14, special_chars=False, numbers=False)

print(password1)
print(password2)
print(password3)
print(password4)
print(password5)
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

import random
class MovieDatabase:
    def __init__(self, creator):
        self.creator = creator
        self.movies = []

    def add_movie(self, name, genre, rating):
        self.movies.append({'name': name, 'genre': genre, 'rating': rating})

    def what_to_watch(self):
        if not self.movies:
            print("No movies in the database yet.")
            return
        movie = random.choice(self.movies)
        print(f"{self.creator} recommends you to watch '{movie['name']}' tonight, "
              f"a {movie['genre']} rated {movie['rating']}/5.")

my_movie_database = MovieDatabase('Lucious')


my_movie_database.add_movie("Wandering Earth", "Science Fiction", 5)
my_movie_database.add_movie("Dragon horse spirit", "Action", 4.5)
my_movie_database.add_movie("I'm not the god of medicine", "Drama", 5)
my_movie_database.add_movie("The devil boy of Nezha comes to the world", "Comedy", 4)
my_movie_database.what_to_watch()