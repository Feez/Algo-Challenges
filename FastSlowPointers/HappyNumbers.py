# Happy Number (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/39q3ZWq27jM
#
# Any number will be called a happy number if, after repeatedly replacing it 
# with a number equal to the sum of the square of all of its digits, leads us 
# to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

def get_sum_of_squares(num):
    total = 0
    while num > 0:
        digit = num % 10
        
        total += (digit * digit)

        num //= 10

    return total

def find_happy_number(num):
    slow = num
    fast = num

    while fast != 1:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))

        if slow == fast:
            return False

    return True

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

main()
