
# DNA Sequence Analyzer
# Author: Wasif Khan
# Project: Beginner Bioinformatics

def read_fasta(filename):
    """Read a single DNA sequence from a FASTA file."""

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if not lines or not lines[0].startswith(">"):
            print("Error: Invalid FASTA file. Header must start with >")
            return None

        sequence = ""

        for line in lines[1:]:
            sequence += line.strip()

        if not sequence:
            print("Error: No DNA sequence found in FASTA file.")
            return None

        return sequence.upper()

    except FileNotFoundError:
        print("Error: FASTA file not found.")
        return None


def analyze_dna(sequence):

    sequence = sequence.upper().strip()

    if not sequence:
        print("Error: Empty DNA sequence.")
        return

    valid_bases = set("ATGC")

    if not all(base in valid_bases for base in sequence):
        print("Error: Invalid DNA sequence.")
        print("Use only A, T, G, and C.")
        return

    length = len(sequence)

    count_a = sequence.count("A")
    count_t = sequence.count("T")
    count_g = sequence.count("G")
    count_c = sequence.count("C")

    gc_content = ((count_g + count_c) / length) * 100
    at_content = ((count_a + count_t) / length) * 100

    complement_table = str.maketrans("ATGC", "TACG")
    complement = sequence.translate(complement_table)

    reverse_complement = complement[::-1]

    rna_sequence = sequence.replace("T", "U")

    print("\n===== DNA SEQUENCE ANALYSIS =====")
    print("Original DNA:", sequence)
    print("Sequence Length:", length)

    print("\nNucleotide Counts:")
    print("A (Adenine):", count_a)
    print("T (Thymine):", count_t)
    print("G (Guanine):", count_g)
    print("C (Cytosine):", count_c)

    print("\nSequence Composition:")
    print(f"GC Content: {gc_content:.2f}%")
    print(f"AT Content: {at_content:.2f}%")

    print("\nSequence Transformations:")
    print("Complementary DNA:", complement)
    print("Reverse Complement:", reverse_complement)
    print("RNA Sequence:", rna_sequence)

    print("\n===== ANALYSIS COMPLETE =====")


# Main program
print("DNA SEQUENCE ANALYZER")
print("1. Enter DNA sequence manually")
print("2. Read DNA sequence from FASTA file")

choice = input("Choose option (1 or 2): ")

if choice == "1":
    dna = input("Enter DNA sequence: ")
    analyze_dna(dna)

elif choice == "2":
    filename = input("Enter FASTA filename: ")
    dna = read_fasta(filename)

    if dna is not None:
        analyze_dna(dna)

else:
    print("Invalid choice. Please select 1 or 2.")
