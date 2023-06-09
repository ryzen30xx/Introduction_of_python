#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'get_rank' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. FLOAT english
#  2. FLOAT math
#  3. FLOAT literature
#

def get_rank(english, math, literature):
    # return rank based on the average of 3 grades
    addition = english + math + literature; multication = addition / 3
    
    if  multication <= 4.0: return "failed"
    elif 4 < multication < 6.5: return "pass"
    elif multication >= 6.5 and multication < 8: return "merit"
    elif 8 < multication <= 10: return "dictinction"
    elif multication > 10 or multication == 5.0: return "invalid grade"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # DO NOT CHANGE IN HERE

    english = float(input().strip())

    math = float(input().strip())

    literature = float(input().strip())

    rank = get_rank(english, math, literature)

    fptr.write(rank + '\n')

    fptr.close()
