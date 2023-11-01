# def rearrange(list_nums):
#     result_list = []
#     first = 10000000
#     for i in range(len(list_nums)):
#         if list_nums[i] < first:
#             result_list.append(list_nums[i])
#             first = list_nums[i]
#         # result_list.append(list_nums[i])
#         for j in range(i+1, len(list_nums) - 1):
#             if list_nums[j] > list_nums[i]:
#                 result_list.append(list_nums[j])
#                 break;

visited = []



def find_appropriate_number(left, right, list_nums):
    for i in range(list_nums):
        if list_nums[i] > left and list_nums[i] > right and visited == 0:
            visited[i] = 1
            return i

def rearrange(list_nums):
    for i in range(len(list_nums)):
        if i+1 % 2 == 0:
            


if __name__ == "__main__":
    input_str = str(input())
    processed_input = input_str.strip("[]").split(", ")
    for i in range(len(processed_input)):
        visited.append(0)



