import numpy as np

print(np.char.add(['hello', 'hi'], ['world', 'there']))  # ['helloworld' 'hithere']

print(np.char.multiply('hello', 3))  # hellohellohello

print(np.char.center(' hello ', 20, fillchar='-'))  # ----------hello----------
print(np.char.capitalize('hello world'))  # Hello world
print(np.char.title('hello world'))  # Hello World
print(np.char.lower('HELLO WORLD'))  # hello world
print(np.char.upper('hello world'))  # HELLO WORLD
print(np.char.split('hello world'))  # ['hello', 'world']
print(np.char.splitlines('hello\nworld'))  # ['hello', 'world']

# This uses the np.char.strip() function to remove the character 'h' from the beginning and end of each string in the array ['hello', 'hey', 'how', 'who'].
print(np.char.strip(['hello', 'hey', 'how', 'who', 'blah'], 'h'))  
