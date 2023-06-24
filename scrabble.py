
letters = ["A", "B", "C", "D", "E", "F", "G", "H",
"I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
"S", "T", "U", "V", "W", "X", "Y", "Z", " "]


points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]



# Create a point dict 

letter_points = {}

for x in range(27):
    letter_points[letters[x]] = points[x]


    

# Determine score of a word

def score_word(word):

    point_total = 0 

    for ch in word.upper():
        if ch in letter_points:
            point_total += letter_points[ch]    

    return point_total

print(score_word("cat"))





# Create  a dict of a player's word history
p_words = {
    "player1" : ["BLUE", "TENNIS", "EXIT"],
    "wordNerd" : ["EARTH", "EYES", "MACHINE"],
    "Lexi Con" : ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader" : ["ZAP", "COMA", "PERIOD"]
}


# Q10 - Empty Dict to store player's points
player_to_points = {}

 # 
for player, words in p_words.items():
    p_points = 0
    for word in words:
        p_points += score_word(word)
    player_to_points[player] = p_points
    
  
print(player_to_points)


# print(score_word("MACHINE"))
