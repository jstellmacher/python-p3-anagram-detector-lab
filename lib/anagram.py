# jai's code

class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
        
    def match(self, word_list):
        match_word_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_word_list.append(word)
                
        return match_word_list







# list1 = ['enlists', 'google', 'inlets', 'banana']

# def Anagram():

#     listen = Anagram("listen")
#     listen.match(['enlists', 'google', 'inlets', 'banana'])
# # => ['inlets']

# ['enlists', 'google', 'inlets', 'banana'] == []

# if list1 == []


# [letter for letter in "hello"]
# ["h", "e", "l", "l", "o"]











# Hints:

# How will you determine if one word is an anagram for another?

# You'll need to iterate over the list of words that the match() method
# takes as an argument. You will compare each word of that list to the word
# that the Anagram class is initialized with.

# To determine one word is an anagram of another word, try determining if they are
# composed of the same letters. You can use a list interpretation on a string to
# get a list of its individual letters: