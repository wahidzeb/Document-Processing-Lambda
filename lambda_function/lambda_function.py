import boto3
import requests
import io
import json

def lambda_handler(event, context):
    """
    AWS Lambda handler to download a PDF, extract text using Textract, and log the output.
    """
    pdf_url = "https://arxiv.org/pdf/2206.01062.pdf"

    try:
        # Download the PDF file
        response = requests.get(pdf_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        pdf_bytes = response.content

        # Initialize Textract client
        textract_client = boto3.client('textract')

        # Call Textract to detect text in the document
        textract_response = textract_client.detect_document_text(
            Document={'Bytes': pdf_bytes}
        )

        # Extract and print the text
        extracted_text = ""
        for item in textract_response["Blocks"]:
            if item["BlockType"] == "LINE":
                extracted_text += item["Text"] + "\n"

        print(extracted_text)

        return {
            'statusCode': 200,
            'body': json.dumps('Text extraction successful!')
        }

    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error downloading PDF: {e}')
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'An error occurred: {e}')
        }