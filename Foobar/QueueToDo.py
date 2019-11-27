# f(b)   = ( 0 ^ 1 ^ 2 ^ 3 ^ 4 .. ^ (a-1) ) ^ (a ^ a+1 ^ a+2 .. ^ b)
# f(b)   = f(a-1) ^ (a ^ a+1 ^ a+2 .. ^ b)
# f(b)   = f(a-1) ^ n
# n      = f(b) ^ f(a-1)

def get_val(a):
    return (a, 1, a + 1, 0)[a % 4]

def xor(a, b):
    return get_val(b - 1) ^ get_val(a - 1)

def solution(start_index, line_length):
    trailing_xor = 0
    curr_line_start = start_index

    for counter in reversed(range(1, line_length + 1)):
        trailing_xor ^= xor(curr_line_start, curr_line_start + counter)
        curr_line_start += line_length

    return trailing_xor

if __name__ == "__main__":
    #print(solution(0, 3))
    #print(solution(17, 4))
    print(solution(200000, 25000))
    #print(solution(2000000000,10**4))
