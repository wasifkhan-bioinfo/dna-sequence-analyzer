
import unittest
from dna_analyzer import analyze_dna


class TestDNAAnalyzer(unittest.TestCase):

    def test_sequence_length(self):
        sequence = "ATGC"
        self.assertEqual(len(sequence), 4)

    def test_nucleotide_count(self):
        sequence = "AATTGGCC"
        self.assertEqual(sequence.count("A"), 2)
        self.assertEqual(sequence.count("T"), 2)
        self.assertEqual(sequence.count("G"), 2)
        self.assertEqual(sequence.count("C"), 2)

    def test_gc_content(self):
        sequence = "GGCCATAT"
        gc_content = (
            (sequence.count("G") + sequence.count("C"))
            / len(sequence)
        ) * 100

        self.assertEqual(gc_content, 50.0)

    def test_complement(self):
        sequence = "ATGC"
        complement = sequence.translate(
            str.maketrans("ATGC", "TACG")
        )
        self.assertEqual(complement, "TACG")

    def test_reverse_complement(self):
        sequence = "ATGC"
        complement = sequence.translate(
            str.maketrans("ATGC", "TACG")
        )
        reverse_complement = complement[::-1]

        self.assertEqual(reverse_complement, "GCAT")


if __name__ == "__main__":
    unittest.main()

