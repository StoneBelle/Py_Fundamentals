### SPLIT ###
# splits the string based on specified separator and returns a list
# default separator is white space
# str.split("[SEPARATOR]")
shopping = "clothes:shoes:toys:makeup:jewelery"

answr1 = shopping.split(":")
print(answr1)


### JOIN ###
# joins all elements in an iterable by using the specified separator and returns a string
# Separator can be a char, space, no space, symbol, num
# ([SEPARATOR]).join(iterable)
n1 = "123" # Iterable
n2 ="aaa" # Separator

answr2 = n2.join(n1) 
print(answr2)


### UPPER ###
# changes all chars in a str to uppercase
sen = "dogs are very cute"

answr3 = sen.upper()
print(answr3)


### LOWER ###
# changes all char in str to lowercase
line = "I LIKE TO PLAY BASKETBALL"

answr4 = line.lower()
print(answr4)


### TITLE ##
# Capitalizes all words in a str
name = "mickey mouse"

answr5 = name.title()
print(answr5)


### REPLACE ###
# replaces a specified str with a different str
# 3 main parameters
# str to replace, replacement str, amount of replacements (optional)
# note: if 3rd param is not called, it will replace all occurences
# str.replace("old str", "new str", "occurences")

poem = "ow ow ow your boat"

answr6 = poem.replace("ow", "row")
print(answr6)


### STRIP ##
# removes the specified space(s)/value/char at the start and end of a str
snack = "fruitsalad tastes good fruit"

answr7 = snack.strip("fruit")
print(answr7)