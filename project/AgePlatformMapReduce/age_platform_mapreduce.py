#!/usr/bin/env python3
import sys
import csv
from collections import defaultdict

def read_input(file):
    for line in file:
        yield line.strip()

def mapper():
    input = read_input(sys.stdin)
    for line in input:
        if line:
            # Skipping the header
            if line.startswith("User_ID"):
                continue
            reader = csv.reader([line])
            for row in reader:
                age = row[1]
                platform = row[3]
                print(f"{age}\t{platform}")

def reducer():
    platform_count = defaultdict(lambda: defaultdict(int))
    input = read_input(sys.stdin)

    for line in input:
        age, platform = line.split('\t')
        platform_count[age][platform] += 1

    for age in platform_count:
        for platform in platform_count[age]:
            print(f"{age}\t{platform}\t{platform_count[age][platform]}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mapper":
        mapper()
    else:
        reducer()
