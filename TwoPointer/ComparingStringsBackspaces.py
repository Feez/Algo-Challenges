# Comparing Strings containing Backspaces (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/g7pBzR12YPl
# 
# Given two strings containing backspaces (identified by the character ‘#’), 
# check if the two strings are equal.

def backspace_compare(str1, str2):
    right1 = len(str1) - 1
    right2 = len(str2) - 1

    while right1 >= 0 or right2 >= 0:
        
        if str1[right1] == '#':
            skip = 2
            while skip > 0 and right1 >= 0:
                right1 -= 1
                if str1[right1] == '#':
                    skip += 1
                else:
                    skip -= 1
                    
        if str2[right2] == '#':
            skip = 2
            while skip > 0 and right2 >= 0:
                right2 -= 1
                if str2[right2] == '#':
                    skip += 1
                else:
                    skip -= 1
                    
        if right1 == -1 and right2 == -1:
            return True
            
        #print(f"Comparing '{str1[right1]}' and '{str2[right2]}'.")
        if str1[right1] != str2[right2]:
            return False

        right1 -= 1
        right2 -= 1

    return True

print(backspace_compare(str1="xy#z", str2="xzz#"))          # True
print(backspace_compare(str1="xy#z", str2="xyz#"))          # False
print(backspace_compare(str1="xp#", str2="xyz##"))          # True
print(backspace_compare(str1="xywrrmp", str2="xywrrmu#p"))  # True
print(backspace_compare(str1="ab##", str2="c#d#"))          # True
print(backspace_compare(str1="bxj##tw", str2="bxj###tw"))   # False