import os
from dotenv import load_dotenv
load_dotenv()

from groq import Groq
import groq

# Create the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  
)

def llm(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )
    return chat_completion.choices[0].message.content

def split_text(text, max_chunk_size=1000):
    accumulator = []
    while len(text) > 0:
        accumulator.append(text[:max_chunk_size])
        text = text[max_chunk_size:]
    return accumulator

def summarize_text(text):
    prompt = f'''
    Summarize the following text in 1-3 sentences.

    {text}
    '''
    try:
        output = llm(prompt)
        return output.split('\n')[-1]
    except groq.APIStatusError:
        chunks = split_text(text, 10000)
        print('len(chunks)=', len(chunks))
        accumulator = []
        for i, chunk in enumerate(chunks):
            print('i =', i)
            summary = summarize_text(chunk)
            accumulator.append(summary)
        summarized_text = ' '.join(accumulator)
        summarized_text = summarize_text(summarized_text)
        return summarized_text

def summarize_image_from_url(image_url):
    """
    Uses Groq to summarize an image by passing a message that includes both text and an image URL.
    """
    message = [
        {
            "type": "text",
            "text": "What's in this image?"
        },
        {
            "type": "image_url",
            "image_url": {
                "url": image_url
            }
        }
    ]
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content

# -------------------------
# Main execution
# -------------------------
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog='docsum',
        description='Summarize a local file, webpage URL, or an image URL.'
    )
    parser.add_argument('source', help='Path to a file or URL to summarize')
    args = parser.parse_args()

    # Define image extensions to check against
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')

    # If the source starts with http:// or https://, process it as a URL
    if args.source.lower().startswith('http://') or args.source.lower().startswith('https://'):
        # Check if the URL is likely an image by its extension
        if args.source.lower().endswith(image_extensions):
            print("Processing image URL:", args.source)
            summary = summarize_image_from_url(args.source)
            print("Summary of the image:\n", summary)
        else:
            import requests
            try:
                response = requests.get(args.source)
                encoding = response.encoding if response.encoding else 'utf-8'
                html = response.content.decode(encoding, errors='replace')
            except Exception as e:
                print("Error fetching URL:", e)
                exit(1)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, features="lxml")
            text = soup.get_text()
            print("Summary of the webpage:\n")
            print(summarize_text(text))
    else:
        # Process as a local file
        # Check if it's a local image file based on extension
        if args.source.lower().endswith(image_extensions):
            print("Local image summarization is not supported. Please provide an image URL.")
            exit(1)
        else:
            print("Processing file:", args.source)
            try:
                with open(args.source, 'r', encoding='utf-8', errors='replace') as fin:
                    text = fin.read()
            except Exception as e:
                print("Error reading file:", e)
                exit(1)
            # Optionally, if the file is HTML, strip out HTML tags:
            if args.source.lower().endswith(('.html', '.htm')):
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(text, features="lxml")
                text = soup.get_text()
            print("Summary of the document:\n")
            print(summarize_text(text))
