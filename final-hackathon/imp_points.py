import requests

url = "https://api.worqhat.com/api/ai/v2/pdf-extract"

api_key = "sk-d591ba6b6c814956b45b4d9194c69b8e"

pdf_file_path = input("Enter the PDF file path: ")

headers = {
    'Authorization': f'Bearer {api_key}'
}

files = {
    'file': (pdf_file_path, open(pdf_file_path, 'rb'), 'application/pdf')
}

response = requests.post(url, headers=headers, files=files)

if response.status_code == 200:

    json_response = response.json()

    extracted_content = json_response['content']
    
    with open('extracted_content.txt', 'w', encoding='utf-8') as file:
        file.write(extracted_content)
        
    print("Content has been extracted and saved to 'extracted_content.txt'")
else:
    print(f"Failed to extract content from the PDF. Status code: {response.status_code}")
