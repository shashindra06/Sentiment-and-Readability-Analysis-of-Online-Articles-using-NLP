import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import time

def extract_article_content(url):
    """
    Extract title and body text from a given URL using BeautifulSoup with lxml parser.
    Returns tuple of (title, body_text)
    """
    try:
        # Add headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Use lxml parser as specified
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Extract title
        title = soup.title.string if soup.title else "No Title Found"
        
        # Extract body text - common article content containers
        article_text = ""
        for tag in soup.find_all(['p', 'article', 'div']):
            if tag.get('class') and any(x in str(tag.get('class')).lower() for x in ['content', 'article', 'post', 'story']):
                article_text += tag.get_text() + "\n"
        
        # If no specific article container found, get all paragraph text
        if not article_text:
            article_text = "\n".join([p.get_text() for p in soup.find_all('p')])
            
        return title.strip(), article_text.strip()
        
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return None, None

def save_article(url_id, title, content, output_dir):
    """Save article content to a text file using URL_ID as filename"""
    filepath = os.path.join(output_dir, f"{url_id}.txt")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Title: {title}\n\n")
        f.write(content)
    
    return filepath

def main():
    # Create articles directory if it doesn't exist
    output_dir = 'articles'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read URLs from input/Input.xlsx
    try:
        input_file = os.path.join('input', 'Input.xlsx')
        df = pd.read_excel(input_file)
        
        # Verify required columns exist
        required_columns = ['URL_ID', 'URL']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"Input Excel file must contain columns: {required_columns}")
        
        # Process each URL
        for index, row in df.iterrows():
            url_id = row['URL_ID']
            url = row['URL']
            print(f"Processing URL_ID {url_id}: {url}")
            
            title, content = extract_article_content(url)
            
            if title and content:
                filepath = save_article(url_id, title, content, output_dir)
                print(f"Saved to: {filepath}")
            else:
                print(f"Failed to extract content for URL_ID {url_id}")
            
            # Add delay between requests to be polite
            time.sleep(2)
            
    except Exception as e:
        print(f"Error reading Input.xlsx: {str(e)}")
        return

if __name__ == "__main__":
    main()
