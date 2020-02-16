import sys
from generate import *


def check_args():
    msg = "usage: quzdra.py [part of speech: a|n|v] [word max length] [number of words]"
    if len(sys.argv) != 4:
        print("Invalid number or arguments" + '\n' + msg)
        return False
    elif not isinstance(sys.argv[1], str) or sys.argv[1] not in ("a", "A", "n", "N", "v", "V"):
        print("Invalid value for part of speech" + '\n' + msg)
        return False
    elif not sys.argv[2].isdigit():
        print("Invalid value for word length: use an integer" + '\n' + msg)
        return False
    elif not sys.argv[3].isdigit():
        print("Invalid value for word quantity: use an integer" + '\n' + msg)
        return False
    else:
        return True


if check_args():
    _, pos, length, total = sys.argv
    write_list(generate_list(pos, int(length), int(total)))

