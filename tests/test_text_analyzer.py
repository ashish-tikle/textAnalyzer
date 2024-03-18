import unittest
from src.text_analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def test_count_sentences(self):
        document = "This is a sample sentence. It contains multiple sentences. Each sentence has words."
        analyzer = TextAnalyzer(document)
        self.assertEqual(analyzer.count_sentences(), 3)

    def test_count_words_per_sentence(self):
        document = "This is a sample sentence. It contains multiple sentences. Each sentence has words."
        analyzer = TextAnalyzer(document)
        self.assertEqual(analyzer.count_words_per_sentence(), [5, 4, 3])

    def test_count_word_occurrences(self):
        document = "This is a sample sentence. It contains multiple sentences. Each sentence has words."
        analyzer = TextAnalyzer(document)
        self.assertEqual(analyzer.count_word_occurrences("sentence"), 3)

if __name__ == '__main__':
    unittest.main()