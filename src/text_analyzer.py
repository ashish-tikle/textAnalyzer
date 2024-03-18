import re
import logging

class TextAnalyzer:
    def __init__(self, document):
        self.document = document

    def count_sentences(self):
        try:
            # Split the document into sentences using regex
            sentences = re.split(r'[.!?]+', self.document)
            # Filter out empty strings
            sentences = [sentence for sentence in sentences if sentence.strip()]
            return len(sentences)
        except Exception as e:
            logging.error("Error occurred while counting sentences: %s", str(e))
            return None

    def count_words_per_sentence(self):
        try:
            # Split the document into sentences
            sentences = re.split(r'[.!?]+', self.document)
            # Initialize an empty list to store word counts per sentence
            word_counts = []
            for sentence in sentences:
                # Split each sentence into words
                words = sentence.split()
                # Append the word count of each sentence to the list
                word_counts.append(len(words))
            return word_counts
        except Exception as e:
            logging.error("Error occurred while counting words per sentence: %s", str(e))
            return None

    def count_word_occurrences(self, target_word):
        try:
            # Count occurrences of the target word in the document
            occurrences = self.document.lower().count(target_word.lower())
            return occurrences
        except Exception as e:
            logging.error("Error occurred while counting word occurrences: %s", str(e))
            return None