# DNA Sequence Analyzer
# Author: Wasif Khan
# Purpose: Basic DNA sequence analysis

def analyze_dna(sequence):
    sequence = sequence.upper().strip()

    # Valid DNA nucleotides
    valid_bases = set("ATGC")

    if not sequence:
        print("Error: Please enter a DNA sequence.")
        return

    if not all(base in valid_bases for base in sequence):
        print("Error: Invalid DNA sequence.")
        print("Please use only A, T, G, and C.")
        return

    # Count nucleotides
    length = len(sequence)
    count_a = sequence.count("A")
    count_t = sequence.count("T")
    count_g = sequence.count("G")
    count_c = sequence.count("C")

    # Calculate nucleotide percentages
    gc_content = ((count_g + count_c) / length) * 100
    at_content = ((count_a + count_t) / length) * 100

    # Generate complementary sequence
    complement_table = str.maketrans("ATGC", "TACG")
    complement = sequence.translate(complement_table)

reverse_complement = complement[::-1]

        
         # Display results
    print("\n=== DNA SEQUENCE ANALYSIS ===")
    print("DNA Sequence:", sequence)
    print("Sequence Length:", length)
    print("A (Adenine):", count_a)
    print("T (Thymine):", count_t)
    print("G (Guanine):", count_g)
    print("C (Cytosine):", count_c)
    print(f"GC Content: {gc_content:.2f}%")
    print(f"AT Content: {at_content:.2f}%")
    print("Complementary DNA:", complement)
    print("Reverse Complement:", reverse_complement)


dna = input("Enter a DNA sequence: ")
analyze_dna(dna)
