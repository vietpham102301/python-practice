import ast

str_input = str(input())
list_dict_input = ast.literal_eval(str_input)

sorted_result = sorted(list_dict_input, key=lambda x: x['color'])

print(sorted_result, end="")

