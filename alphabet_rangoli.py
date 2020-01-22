# Dev for fun for Spartan Hackers HR competition

def get_radius(size):
    return 2 * size

def print_rangoli(size):
    letters = [chr(ord('a') + i) for i in range(26)]

    out = []

    for row in reversed(range(size)):
        sep = ''.join('-' for i in range(get_radius(row)))
        elapsed = size - row
        data = '-'.join(letters[size - i - 1] for i in range(elapsed))
        out.append(''.join([sep, data, data[:-1][::-1], sep]))

    for i in range(len(out)):
        print(out[i])
    for i in reversed(range(len(out) - 1)):
        print(out[i])

if __name__ == "__main__":
    print_rangoli(26)
