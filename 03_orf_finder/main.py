import re
from Bio import SeqIO

def trial(filename, start_pattern):
    file = open(filename)
    file.readline()
    sequence = ""
    start_index = 0

    for line in file:
        line = line.strip().upper()
        sequence += line

    while (start_index <= len(sequence)):
        start_match = re.search(start_pattern, sequence[start_index:])
        if not start_match:
            print("No more start codon found")
            break
        start_index += start_match.start()

        stop_index = start_index + 6 # ignoring any stop codon immediately after the start codon
        stop_text = ''
        while (stop_index <= len(sequence)):
            if sequence[stop_index:stop_index+3] in ("TAA", "TAG", "TGA"): 
                stop_text = sequence[stop_index:stop_index+3]
                break
            stop_index += 3

        if stop_text == '':
            print("No more stop codon found")
            break

        pattern = sequence[start_index:stop_index + 3]
        print(pattern, start_index, stop_index)

        start_index = stop_index + 4

def main():
    filename = "resources/JN587815.1.fasta"
    pattern2 = r"ATG"

    print("Running...")
    print("=== TRIAL ===")
    trial(filename, pattern2)

if __name__ == "__main__":
    main()