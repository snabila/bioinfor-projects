from Bio import SeqIO

def withPackage(filename):
    for record in SeqIO.parse(filename, "fasta"):
        sequence = record.seq
        a_count = sequence.count("A")
        t_count = sequence.count("T")
        c_count = sequence.count("C")
        g_count = sequence.count("G")
        print(f"A: {a_count}, T: {t_count}, C: {c_count}, G: {g_count}\n")

def trial(filename):
    file = open(filename)
    a_count = t_count = c_count = g_count = 0
    header = file.readline()
    
    for line in file:
        # for char in line:
        #     if char == 'A' : a_count += 1
        #     if char == 'C' : c_count += 1
        #     if char == 'T' : t_count += 1
        #     if char == 'G' : g_count += 1

        line = line.strip().upper()
        a_count += line.count("A")
        c_count += line.count("C")
        t_count += line.count("T")
        g_count += line.count("G")

    print(f"A: {a_count}, T: {t_count}, C: {c_count}, G: {g_count}")

    gc_content = (g_count + c_count) / (a_count + c_count + t_count + g_count) * 100
    print(f"GC Content: {gc_content}")
    


def main():
    filename = "../resources/JN587815.1.fasta"
    print("Running...")
    print("=== WITH PACKAGE ===")
    withPackage(filename)
    print("=== TRIAL ===")
    trial(filename)

if __name__ == "__main__":
    main()