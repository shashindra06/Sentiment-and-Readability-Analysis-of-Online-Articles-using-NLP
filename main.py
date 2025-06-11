import os
import re
import pandas as pd
from text_analysis import analyze_text

# Output columns as per Output Data Structure.xlsx
OUTPUT_COLUMNS = [
    'URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
    'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE',
    'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'
]

ARTICLES_DIR = 'articles'
INPUT_XLSX = os.path.join('input', 'Input.xlsx')
OUTPUT_XLSX = os.path.join('output', 'FinalOutput.xlsx')

# Load URL mapping from Input.xlsx
url_map = {}
if os.path.exists(INPUT_XLSX):
    df_input = pd.read_excel(INPUT_XLSX)
    for _, row in df_input.iterrows():
        url_map[str(row['URL_ID'])] = row['URL']

results = []

for filename in os.listdir(ARTICLES_DIR):
    if filename.endswith('.txt'):
        url_id = filename.replace('.txt', '')
        filepath = os.path.join(ARTICLES_DIR, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            # Extract title and body
            title = ''
            body_lines = []
            for i, line in enumerate(lines):
                if line.startswith('Title:'):
                    title = line.replace('Title:', '').strip()
                    body_lines = lines[i+1:]
                    break
            body = ''.join(body_lines).strip()
            # If no title line, treat all as body
            if not title:
                body = ''.join(lines).strip()
        # Compute metrics
        metrics = analyze_text(body)
        # Prepare row for output
        row = {
            'URL_ID': url_id,
            'URL': url_map.get(url_id, ''),
            'POSITIVE SCORE': metrics['Positive Score'],
            'NEGATIVE SCORE': metrics['Negative Score'],
            'POLARITY SCORE': metrics['Polarity Score'],
            'SUBJECTIVITY SCORE': metrics['Subjectivity Score'],
            'AVG SENTENCE LENGTH': metrics['Avg Sentence Length'],
            'PERCENTAGE OF COMPLEX WORDS': metrics['% Complex Words'],
            'FOG INDEX': metrics['Fog Index'],
            'AVG NUMBER OF WORDS PER SENTENCE': metrics['Avg Sentence Length'],
            'COMPLEX WORD COUNT': metrics['Complex Word Count'],
            'WORD COUNT': metrics['Word Count'],
            'SYLLABLE PER WORD': metrics['Syllables per Word'],
            'PERSONAL PRONOUNS': metrics['Personal Pronouns Count'],
            'AVG WORD LENGTH': metrics['Avg Word Length']
        }
        results.append(row)

# Write to Excel
os.makedirs('output', exist_ok=True)
df_out = pd.DataFrame(results, columns=OUTPUT_COLUMNS)
df_out.to_excel(OUTPUT_XLSX, index=False)
print(f"Analysis complete. Results written to {OUTPUT_XLSX}")
