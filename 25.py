def gen_combination(k, a_set):
    index_set = [0]
    result_set = []
    for i in range(1, k+1):
        index_set.append(i)
    while True:
        temp_list = []
        for i in range(1, k+1):
            # print(index_set[i], sep=", ",end="")
            temp_list.append(a_set[index_set[i]])
        result_set.append(temp_list)
        i = k
        while index_set[i] == len(a_set) - 1 - k + i and i > 0:
            i -= 1
        if i == 0:
            break
        else:
            index_set[i] += 1
            for j in range(i+1, k+1):
                index_set[j] = index_set[i] - i + j
    return result_set


if __name__ == "__main__":
    input_data = str(input())

    input_list = input_data.strip("[]").split(", ")
    input_list = [int(x) for x in input_list]
    # print(input_list)
    format_input_list = [0]
    format_input_list.extend(input_list)

    result = []
    for i in range(1, len(input_list)+1):
        result.extend(gen_combination(i, format_input_list))

    str_result = "["+str(result).strip("[]")+"]"
    print(str_result, end="")

