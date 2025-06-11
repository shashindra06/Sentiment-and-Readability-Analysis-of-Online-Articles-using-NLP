import os
import re

def read_file_with_encoding(filepath):
    """
    Try to read a file with different encodings.
    Returns the content as a list of lines.
    """
    encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read().splitlines()
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"Error reading {filepath} with {encoding}: {str(e)}")
            continue
    
    raise UnicodeDecodeError(f"Could not read {filepath} with any of the attempted encodings")

def load_stopwords():
    """
    Load all stopwords from text files in 'input/' directory that start with 'StopWords'.
    Returns a set of unique stopwords.
    """
    stopwords = set()
    input_dir = 'input'
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory '{input_dir}' not found")
    
    # Find all StopWords files
    stopword_files = [f for f in os.listdir(input_dir) if f.startswith('StopWords') and f.endswith('.txt')]
    
    if not stopword_files:
        raise FileNotFoundError("No StopWords files found in input directory")
    
    # Load stopwords from each file
    for filename in stopword_files:
        filepath = os.path.join(input_dir, filename)
        try:
            words = read_file_with_encoding(filepath)
            stopwords.update(word.strip().lower() for word in words if word.strip())
        except Exception as e:
            print(f"Error reading {filename}: {str(e)}")
    
    return stopwords

def load_sentiment_words():
    """
    Load positive and negative words from their respective files.
    Returns tuple of (positive_words, negative_words) as sets.
    """
    input_dir = 'input'
    positive_file = os.path.join(input_dir, 'positive-words.txt')
    negative_file = os.path.join(input_dir, 'negative-words.txt')
    
    positive_words = set()
    negative_words = set()
    
    # Load positive words
    try:
        words = read_file_with_encoding(positive_file)
        positive_words = set(word.strip().lower() for word in words if word.strip())
    except Exception as e:
        print(f"Error reading positive words file: {str(e)}")
    
    # Load negative words
    try:
        words = read_file_with_encoding(negative_file)
        negative_words = set(word.strip().lower() for word in words if word.strip())
    except Exception as e:
        print(f"Error reading negative words file: {str(e)}")
    
    return positive_words, negative_words

def count_syllables(word):
    """
    Count the number of syllables in a word.
    Uses a simple algorithm based on vowel groups.
    Returns the syllable count as an integer.
    """
    word = word.lower()
    
    # Handle special cases
    if word.endswith('e'):
        word = word[:-1]
    
    # Count vowel groups
    vowel_groups = re.findall(r'[aeiouy]+', word)
    
    # Handle special cases for 'y'
    if word.startswith('y'):
        vowel_groups = vowel_groups[1:]
    
    # Ensure at least one syllable
    return max(1, len(vowel_groups))

def test_utils():
    """
    Test function to verify the utility functions are working correctly.
    """
    try:
        # Test stopwords loading
        stopwords = load_stopwords()
        print(f"Loaded {len(stopwords)} stopwords")
        
        # Test sentiment words loading
        positive_words, negative_words = load_sentiment_words()
        print(f"Loaded {len(positive_words)} positive words and {len(negative_words)} negative words")
        
        # Test syllable counting
        test_words = ['hello', 'world', 'beautiful', 'the', 'a', 'eye', 'bye']
        for word in test_words:
            syllables = count_syllables(word)
            print(f"Word: {word}, Syllables: {syllables}")
            
    except Exception as e:
        print(f"Error in testing: {str(e)}")

if __name__ == "__main__":
    test_utils()
