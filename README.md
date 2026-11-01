🧬 DNA Sequence Analyzer

A beginner friendly Bioinformatics project built with Python to perform basic DNA sequence analysis.

Author: Wasif Khan
Field: Bioinformatics and Computational Biology
Language: Python
Project Status: Initial version

📌 Overview

DNA contains four primary nucleotide bases: Adenine (A), Thymine (T), Guanine (G), and Cytosine (C).

This project uses Python to analyze a DNA sequence and calculate basic sequence properties. It demonstrates how programming can be applied to biological data.

The project is designed as a learning exercise in Python programming and introductory Bioinformatics.

✨ Features

- Sequence Length: Calculates the total number of nucleotides.
- Nucleotide Counting: Counts A, T, G, and C individually.
- GC Content: Calculates the percentage of guanine and cytosine.
- AT Content: Calculates the percentage of adenine and thymine.
- Complementary DNA: Generates the complementary sequence.
- Input Validation: Detects empty sequences and invalid characters.

🛠️ Technologies Used

- Python 3
- Python built-in functions and string methods
- Basic Bioinformatics concepts

No external Python libraries are required.

🚀 Getting Started

Prerequisites

Install Python 3 on your computer.

Installation

Clone this repository:

git clone https://github.com/wasifkhan-bioinfo/dna-sequence-analyzer.git

Navigate to the project directory:

cd dna-sequence-analyzer

Run the Program

Execute the following command:

python dna_analyzer.py

Depending on your system, you may need to use "python3" or "py" instead of "python".

🧪 Example

Input

ATGC

Output

=== DNA SEQUENCE ANALYSIS ===
DNA Sequence: ATGC
Sequence Length: 4
A (Adenine): 1
T (Thymine): 1
G (Guanine): 1
C (Cytosine): 1
GC Content: 50.00%
AT Content: 50.00%
Complementary DNA: TACG

🧠 Biological Concepts

1. Nucleotide Composition

DNA sequences consist of nucleotide bases. Counting these bases provides a basic description of sequence composition.

2. GC Content

GC content is the percentage of nucleotides that are guanine or cytosine.

Formula:

GC Content = ((G + C) / Total Sequence Length) × 100

3. AT Content

AT content is the percentage of nucleotides that are adenine or thymine.

Formula:

AT Content = ((A + T) / Total Sequence Length) × 100

For a valid sequence containing only A, T, G, and C, GC content and AT content sum to 100%.

4. Complementary DNA

DNA bases pair according to the following rules:

- A pairs with T.
- T pairs with A.
- G pairs with C.
- C pairs with G.

For example:

Original sequence: "ATGC"

Complementary sequence: "TACG"

The program generates the complementary sequence in the same orientation as the input. It does not reverse the sequence to produce the reverse complement.

⚠️ Limitations

- The current version accepts only A, T, G, and C.
- It does not support FASTA files.
- It does not identify genes or predict biological functions.
- It does not perform sequence alignment.
- It does not determine whether a sequence is associated with a particular disease or organism.

🔮 Future Improvements

Potential extensions include:

- Reading DNA sequences from FASTA files.
- Generating reverse-complement sequences.
- Transcribing DNA into RNA.
- Translating coding sequences into amino acid sequences.
- Visualizing nucleotide composition.
- Adding automated tests for sequence analysis functions.

These are planned improvements, not features of the current version.

🎓 Learning Objectives

This project provides practical experience with:

- Python functions and conditional statements.
- String processing and nucleotide counting.
- Basic mathematical calculations.
- Input validation.
- Applying programming concepts to biological data.
- Documenting a reproducible programming project.

👨‍🔬 About the Author

I am a Microbiology graduate pursuing Bioinformatics, with an interest in computational biology, microbial genomics, and biological sequence analysis.

I am developing my programming and analytical skills through practical projects that connect biological sciences with computational methods.

📄 License

No license has been specified yet. All rights are reserved by default unless a license is added.

---

Learning Bioinformatics, one sequence at a time. 🧬