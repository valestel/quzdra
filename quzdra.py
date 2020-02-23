import sys
from generate import write_list, generate_list


def check_args():
    msg = "usage: quzdra.py [part of speech: a|n|v] [word max length] [number of words]"
    letter = sys.argv[1]
    maxlength = sys.argv[2]
    number = sys.argv[3]
    if len(sys.argv) != 4:
        print("Invalid number or arguments \n%s" % msg)
        sys.exit(1)
    elif not isinstance(letter, str) or letter not in ("a", "A", "n", "N", "v", "V"):
        print("Invalid value for part of speech \n%s" % msg)
        sys.exit(1)
    elif not maxlength.isdigit():
        print("Invalid value for word length: use an integer \n%s" % msg)
        sys.exit(1)
    elif not number.isdigit():
        print("Invalid value for word quantity: use an integer \n%s" % msg)
        sys.exit(1)
    else:
        return True


if __name__ == '__main__':
    if check_args():
        _, pos, length, total = sys.argv
        write_list(generate_list(pos, int(length), int(total)))
