import re
from Bio import SeqIO

def trial(filename, start_pattern, stop_pattern):
    file = open(filename)
    header = file.readline()
    sequence = ""
    start_index = 0

    for line in file:
        line = line.strip().upper()
        sequence += line

    while (start_index <= len(sequence)):
        # start = sequence.find(start_index, pattern)

        start_match = re.search(start_pattern, sequence[start_index:])
        if not start_match:
            print("No more start codon found")
            break
        start_index += start_match.start()

        stop_match = re.search(stop_pattern, sequence[start_index + 3:])
        if not stop_match:
            print("No more stop codon found")
            break
        stop_index = stop_match.end()

        pattern = sequence[start_index:stop_index + 2]
        print(pattern, start_index, stop_index)

        start_index = stop_index + 2

def main():
    filename = "resources/JN587815.1.fasta"
    pattern1 = r"ATG[ATGC]{3,}"
    pattern2 = r"ATG"
    pattern3 = r"(?:[ATGC]{3})+(?:TAA|TAG|TGA)"


    print("Running...")
    # print("=== WITH PACKAGE ===")
    # withPackage(filename, pattern1)
    print("=== TRIAL ===")
    trial(filename, pattern2, pattern3)
    # trial(filename, pattern1)

if __name__ == "__main__":
    main()