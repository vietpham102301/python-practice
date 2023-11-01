import ast

str_input = str(input())

list_input = ast.literal_eval(str_input)

is_palindromes = lambda x: x[::-1] == x

result = [x for x in list_input if is_palindromes(x)]

print(result)