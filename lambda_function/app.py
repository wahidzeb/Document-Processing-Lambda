import json
from docling.document_converter import DocumentConverter

def lambda_handler(event, context):
    """
    AWS Lambda handler to process a PDF from a URL using DocLing.
    """
    source_url = "https://arxiv.org/pdf/2206.01062.pdf"  # Corrected URL

    try:
        # Initialize DocumentConverter
        converter = DocumentConverter()

        # Convert the document from the URL
        doc_result = converter.convert(source_url)

        # Extract the text
        text_content = doc_result.document.export_to_text()

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Document processed successfully!',
                'text': text_content
            })
        }

    except Exception as e:
        print(f"Error processing document: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error processing document',
                'error': str(e)
            })
        }