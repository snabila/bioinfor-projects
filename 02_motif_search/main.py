import re
from Bio import SeqIO

def withPackage(filename, pattern):
    for record in SeqIO.parse(filename, "fasta"):
        sequence = record.seq

        motif = re.finditer(pattern, str(sequence))  # Looking for start codons and gene-like patterns
        for match in motif:
            print(match.group(), match.start(), match.end())

def trial(filename, pattern):
    file = open(filename)
    header = file.readline()
    sequence = ""

    for line in file:
        line = line.strip().upper()
        sequence += line

    start = sequence.index(pattern)
    pattern = sequence[start:len(sequence)]

    print(pattern, start, len(sequence))

def main():
    filename = "../resources/JN587815.1.fasta"
    pattern1 = r"ATG[ATGC]{3,}"
    pattern2 = "ATG"

    print("Running...")
    print("=== WITH PACKAGE ===")
    withPackage(filename, pattern1)
    print("=== TRIAL ===")
    trial(filename, pattern2)

if __name__ == "__main__":
    main()