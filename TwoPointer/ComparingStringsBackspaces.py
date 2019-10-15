# Comparing Strings containing Backspaces (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/g7pBzR12YPl
# 
# Given two strings containing backspaces (identified by the character ‘#’), 
# check if the two strings are equal.

def backspace_compare(str1, str2):
    right1 = len(str1) - 1
    right2 = len(str2) - 1

    while right1 >= 0 and right2 >= 0:

        skip1 = 0
        while right1 >= 0 and str1[right1] == "#":
            right1 -= 1
            skip1 += 1

        skip2 = 0
        while right2 >= 0 and str2[right2] == "#":
            right2 -= 1
            skip2 += 1

        right1 -= skip1
        right2 -= skip2

        if right1 <= -1:
            if right2 <= -1:
                return True
            return False
        elif right2 <= -1:
            return False

        #print(f"Comparing '{str1[right1]}' and '{str2[right2]}'.")
        if str1[right1] != str2[right2]:
            return False

        right1 -= 1
        right2 -= 1

    return True



print(backspace_compare(str1="xy#z", str2="xzz#"))
print(backspace_compare(str1="xy#z", str2="xyz#"))
print(backspace_compare(str1="xp#", str2="xyz##"))
print(backspace_compare(str1="xywrrmp", str2="xywrrmu#p"))