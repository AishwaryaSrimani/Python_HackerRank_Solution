# Q. Kevin and Stuart want to play the 'The Minion Game'.
    # Game Rules
    # Both players are given the same string, s.
    # Both players have to make substrings using the letters of the string s.
    # Stuart has to make words starting with consonants.
    # Kevin has to make words starting with vowels.
    # The game ends when both players have made all possible substrings.
    
def minion_game(string):
    vowels = 'AEIOU'
    s = len(string)
    s_score = 0
    k_score = 0
    for i in range(s):
        if string[i] in vowels:
            k_score += (s - i)
        else:
            s_score += (s - i)
    if s_score > k_score:
        print(f"Stuart {s_score}")
    elif k_score > s_score:
        print(f"Kevin {k_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)