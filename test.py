import os
from dotenv import load_dotenv
load_dotenv()

from groq import Groq
import groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  
)

def llm(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                #content is propmt
                "content":text,
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
            print('i=', i)
            summary = summarize_text(chunk)
            accumulator.append(summary)
        summarized_text = ' '.join(accumulator)
        summarized_text = summarize_text(summarized_text)
        # print('summarized_text=', summarized_text)
        return summarized_text


#default groq model has context window size for 8192 tokens/around 4000 words
#need to strip uncessary contents of html

#import requests
#requests.get(args.filename)
'''
with open(args.filename,'r')as fin:
    text = fin.read()
    print(summarize_text(text))
'''

'''
import fulltext
fulltext.get(args.filename, None)
print(summarize_text(text))
'''

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog='docsum',
        description='summarize the input document',
        )
    parser.add_argument('source',help='Path to the file or URL to summarize')
    args = parser.parse_args()

    if args.source.lower().startswith('https://'):
        import requests
        try:
            response = requests.get(args.source)
            encoding = response.encoding if response.encoding else 'utf-8'
            html = response.content.decode(encoding, errors='replace')
        except Exception as e:
            print("Error fetching URL:",e)
            exit(1)
        '''
        print('filename=',args.filename)
        with open(args.filename,'r', encoding='utf-8') as fin:
        text = fin.read()
        print(summarize_text(text))
        '''
        # one way to solve the problem of too much text for the context window
        # is to remove the "unnecessary" text;
        # for html files, that is the html tags
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, features="lxml")
        text = soup.get_text()
        print("Summary of the webpage:\n")
        print(summarize_text(text))
    else:
        print("Processing file:", agrs.source)
        try:
            with open(args.source,'r',encoding='utf-8',errors='replace')as fin:
                text = fin.read()
        except Exception as e:
            print("Error reading file:", e)
            exit(1)
        if args.source.lower().endswith('.html')or args.source.lower().endswith('.htm'):
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(text, features="lxml")
            text = soup.get_text()
    print("Summary of the document:\n")
    print(summarize_text(text))
    """        
    with open(args.filename, 'r') as fin:
        html = fin.read()
        soup = BeautifulSoup(html, features="lxml")
        text = soup.text
        #print('text=', text)
        print(summarize_text(text))
    """

#print(chat_completion.choices[0].message.content)