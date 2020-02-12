import sys
from generate import *

pos = sys.argv[1]
length = sys.argv[2]
total = sys.argv[3]
write_list(generate_list(pos, int(length), int(total)))
