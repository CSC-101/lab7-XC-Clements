from convert import str_to_float


def gather_numbers() -> list[float]:
    output = []
    continue_flag = True
    while continue_flag:
        user_input = input("Enter a number, or 'done'")
        if user_input == 'done':
            continue_flag = False
        elif str_to_float(user_input) == None:
            pass
        else:
            output.append(str_to_float(user_input))
    return output

if __name__ == '__main__':
    print(gather_numbers())
