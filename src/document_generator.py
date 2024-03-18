import logging
# from google.cloud import storage

class DocumentGenerator:
    # def __init__(self, bucket_name):
    #     self.bucket_name = bucket_name
    #     self.storage_client = storage.Client()

    # def fetch_documents_from_storage(self):
    #     try:
    #         bucket = self.storage_client.get_bucket(self.bucket_name)
    #         blobs = bucket.list_blobs()
    #         documents = []
    #         for blob in blobs:
    #             if blob.name.endswith('.txt'):  # Process only text files
    #                 document = blob.download_as_string().decode('utf-8')
    #                 documents.append(document)
    #         return documents
    #     except Exception as e:
    #         logging.error("Error occurred while fetching documents from storage: %s", str(e))
    #         return []

    def process_documents(self, analyzer):
        documents = self.fetch_documents_from_storage()
        if not documents:
            logging.warning("No documents found in the storage bucket.")
            return

        for document in documents:
            num_sentences = analyzer.count_sentences(document)
            word_counts = analyzer.count_words_per_sentence(document)
            word_occurrences = analyzer.count_word_occurrences(document, target_word="sentence")

            logging.info("Analysis for document:")
            logging.info("Number of sentences: %s", num_sentences)
            logging.info("Number of words in each sentence: %s", word_counts)
            logging.info("Number of occurrences of the word 'sentence': %s", word_occurrences)
