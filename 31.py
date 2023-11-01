def validate_phone(tmp_str):
    if tmp_str[0] != '0':
        return False
    if tmp_str[1:].isnumeric():
        return True
    return False


if __name__ == "__main__":
    a_number = '02836229888'
    print(validate_phone(a_number))

