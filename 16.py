
if __name__ == "__main__":
    str_input = str(input())
    found = False
    for index, element in enumerate(str_input):
        for index1, i in enumerate(str_input):
            find_one = False
            for index2, j in enumerate(str_input):
                if (int(element) == int(i) + int(j)) and (int(i) != 0 and int(j) !=0) and index1 != index2:
                    print(f"{element}, {index}")
                    find_one = True
                    found = True
                    break
            if find_one:
                break

    if not found:
        print("0, -1")