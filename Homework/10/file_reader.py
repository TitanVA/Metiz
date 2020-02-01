import os


with open('pi_digits.txt') as file_object:
    text = ''
    for line in file_object:
        text += line.strip()
    print(text)
    print(len(text))
    
