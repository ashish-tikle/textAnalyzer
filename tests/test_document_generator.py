import unittest
from unittest.mock import MagicMock
from src.document_generator import DocumentGenerator

class TestDocumentGenerator(unittest.TestCase):
    def setUp(self):
        self.bucket_name = "test_bucket"
        self.analyzer = MagicMock()
        self.document_generator = DocumentGenerator(self.bucket_name)

    def test_fetch_documents_from_storage(self):
        self.document_generator.storage_client.get_bucket = MagicMock(return_value=None)
        documents = self.document_generator.fetch_documents_from_storage()
        self.assertEqual(documents, [])

    def test_process_documents(self):
        self.document_generator.fetch_documents_from_storage = MagicMock(return_value=["Document 1", "Document 2"])
        self.document_generator.process_documents(self.analyzer)
        self.analyzer.count_sentences.assert_called()
        self.analyzer.count_words_per_sentence.assert_called()
        self.analyzer.count_word_occurrences.assert_called()

if __name__ == '__main__':
    unittest.main()
