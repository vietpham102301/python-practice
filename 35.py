str_input = str(input()).strip("[]").split(", ")

sorted_list = sorted(str_input, key=lambda x: (int(x) < 0, int(x)))

result = [int(x) for x in sorted_list]

print(result)
