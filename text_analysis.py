import os
import re
import nltk
from utils import load_stopwords, load_sentiment_words, count_syllables

# Set NLTK data path to a local directory
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
os.environ['NLTK_DATA'] = nltk_data_dir
os.makedirs(nltk_data_dir, exist_ok=True)

# Download punkt if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_dir)

def regex_sent_tokenize(text):
    # Split on sentence-ending punctuation followed by space or end of string
    return re.split(r'(?<=[.!?])\s+', text.strip())

def regex_word_tokenize(text):
    # Split on word boundaries, ignoring punctuation
    return re.findall(r'\b\w+\b', text)

def analyze_text(text):
    """
    Analyze raw text and return a dictionary of metrics:
    - Positive/Negative Score
    - Polarity/Subjectivity Score
    - Avg Sentence Length, Complex Word Count, % Complex Words
    - Fog Index, Word Count (excluding stopwords), Syllables per word
    - Personal Pronouns Count, Avg Word Length
    """
    # Load resources
    stopwords = load_stopwords()
    positive_words, negative_words = load_sentiment_words()
    
    # Tokenize sentences and words
    sentences = regex_sent_tokenize(text)
    words = regex_word_tokenize(text)
    words_lower = [w.lower() for w in words if w.isalpha()]
    
    # Remove stopwords for word count
    filtered_words = [w for w in words_lower if w not in stopwords]
    word_count = len(filtered_words)
    
    # Sentiment scores
    positive_score = sum(1 for w in words_lower if w in positive_words)
    negative_score = sum(1 for w in words_lower if w in negative_words)
    
    # Polarity and subjectivity
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (word_count + 0.000001)
    
    # Sentence and word stats
    avg_sentence_length = word_count / (len(sentences) + 0.000001)
    
    # Complex words: words with >2 syllables (excluding proper nouns, compound words, and common suffixes)
    def is_complex(word):
        return count_syllables(word) > 2
    complex_words = [w for w in filtered_words if is_complex(w)]
    complex_word_count = len(complex_words)
    percent_complex_words = complex_word_count / (word_count + 0.000001)
    
    # Fog Index
    fog_index = 0.4 * (avg_sentence_length + percent_complex_words * 100)
    
    # Syllables per word
    total_syllables = sum(count_syllables(w) for w in filtered_words)
    syllables_per_word = total_syllables / (word_count + 0.000001)
    
    # Personal pronouns (using regex for common English pronouns)
    pronoun_pattern = re.compile(r'\b(I|we|my|ours|us)\b', re.I)
    personal_pronouns_count = len(pronoun_pattern.findall(text))
    
    # Avg word length
    total_characters = sum(len(w) for w in filtered_words)
    avg_word_length = total_characters / (word_count + 0.000001)
    
    return {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Avg Sentence Length': avg_sentence_length,
        'Complex Word Count': complex_word_count,
        '% Complex Words': percent_complex_words,
        'Fog Index': fog_index,
        'Word Count': word_count,
        'Syllables per Word': syllables_per_word,
        'Personal Pronouns Count': personal_pronouns_count,
        'Avg Word Length': avg_word_length
    }

# Example test
if __name__ == "__main__":
    sample_text = "I am writing this as a test. We hope this works well! The complexity of the sentences should be measured."
    results = analyze_text(sample_text)
    for k, v in results.items():
        print(f"{k}: {v}")
