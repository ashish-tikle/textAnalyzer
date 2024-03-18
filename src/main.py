import logging
from text_analyzer import TextAnalyzer
from document_generator import DocumentGenerator

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    setup_logging()

    # Initialize TextAnalyzer
    analyzer = TextAnalyzer()

    # Initialize DocumentGenerator with the name of your Google Cloud Storage bucket
    document_generator = DocumentGenerator(bucket_name="your_bucket_name")

    # Process documents from Google Cloud Storage
    document_generator.process_documents(analyzer)

if __name__ == "__main__":
    main()