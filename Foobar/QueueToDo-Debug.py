#start_index = 0
#line_length = 10

start_index, line_length = [int(x) for x in input().split()]



def get_num_workers(line_length):
    return (line_length * line_length) - 1

end_index = start_index + get_num_workers(line_length)

i = 0
counter = line_length
skips = 0

print(f"Start:       {start_index}")
print(f"Line length: {line_length}")
print(f"Calc End:    {end_index}")
print("=====================================")

trailing_xor = 0

result = [list()]

while (i + start_index) <= end_index:
    if counter == 0:
        result.append(list())
        print(f"Skip {skips}")
        i += skips
        skips += 1
        counter = line_length - skips
        print(f"Allow {counter} more")
        continue
    else:
        counter -= 1
    
    trailing_xor = trailing_xor ^ (i + start_index)
    print(i + start_index)
    result[-1].append(i + start_index)
    i += 1

print("=====================================")
print(f"Result: {trailing_xor}")

for x in result:
    for num in x:
        print(str(num).ljust(4, " "), end="")
    print()
