import sys

from convert import str_to_float
def command_line():
    output_list = []
    for n in sys.argv:
        if str_to_float(n) is None:
            pass
        else:
            output_list.append(str_to_float(n))
    return output_list
if __name__ == '__main__':
    print(command_line())