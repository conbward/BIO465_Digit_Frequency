import pandas as pd

infile = 'scratch.txt'

with open(infile) as inf:
    lines = "["
    for line in inf:
        line= line.strip()
        l = f"'{line}',"
        lines += l

    lines = lines[:-1] + "]"
    print(lines)

