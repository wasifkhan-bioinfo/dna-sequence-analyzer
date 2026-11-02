DNA Sequence Analyzer

Author: Wasif Khan
Field: Bioinformatics
Programming Language: Python

About the Project

DNA Sequence Analyzer is a beginner-level bioinformatics project developed using Python. It performs basic analysis and transformations of DNA sequences.

This project is part of my learning journey in MS Bioinformatics.

Features

- Accepts DNA sequences through manual input.
- Reads DNA sequences from a FASTA file.
- Validates DNA sequences using the bases A, T, G, and C.
- Calculates DNA sequence length.
- Counts nucleotides (A, T, G, C).
- Calculates GC content and AT content.
- Generates complementary DNA.
- Generates reverse complementary DNA.
- Converts DNA sequences into RNA.
- Includes automated tests to check the main functions.

Technologies Used

- Python 3
- Pydroid 3
- GitHub
- Python "unittest" module

Project Files

- "dna_analyzer.py": Main program for DNA sequence analysis.
- "sample.fasta": Example DNA sequence in FASTA format.
- "test_dna_analyzer.py": Automated tests for the program.

How to Run

1. Download or clone this repository.
2. Keep the project files in the same folder.
3. Run "dna_analyzer.py" using Python.
4. Choose option "1" to enter a DNA sequence manually.
5. Choose option "2" to read a sequence from a FASTA file.
6. For option 2, enter "sample.fasta" when prompted.

Example FASTA File

>Sample_DNA_Sequence
ATGCGCTAGCTAGCTA

Running Automated Tests

Make sure Python is installed and you are in the project folder. Run:

python -m unittest test_dna_analyzer.py

The test suite contains eight tests covering sequence length, nucleotide counts, GC content, DNA complement, reverse complement, RNA transcription, invalid sequences, and empty sequences.

Learning Objectives

Through this project, I am learning:

- Python programming for bioinformatics.
- DNA sequence analysis.
- Nucleotide composition.
- GC content calculation.
- DNA sequence transformations.
- FASTA file handling.
- Basic software testing.

Future Improvements

- Support multiple sequences in a FASTA file.
- Add DNA-to-protein translation.
- Improve error handling for invalid FASTA files.

Project Status

Status: Beginner Bioinformatics Project
Developed by: Wasif Khan