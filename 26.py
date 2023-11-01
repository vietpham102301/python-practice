def conver2num(list_nums):
    return ''.join(list_nums)

if __name__ == "__main__":
    str_input = str(input()).strip("[]").split((", "))
    print(conver2num(str_input), end="")