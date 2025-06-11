# Sentiment and Readability Analysis of Online Articles using NLP

## 🚀 Project Overview
This project demonstrates a complete end-to-end Natural Language Processing (NLP) pipeline for extracting, analyzing, and reporting on the sentiment and readability of online articles. It is designed to showcase practical skills in web scraping, text processing, custom NLP metric computation, and automated reporting using Python.

## 🛠️ What This Project Does
- **Automated Web Scraping:** Extracts article content from a list of URLs provided in an Excel file.
- **Text Preprocessing:** Cleans and prepares raw article text for analysis.
- **Sentiment Analysis:** Calculates positive and negative scores, polarity, and subjectivity using custom word dictionaries.
- **Readability Analysis:** Computes advanced metrics such as Fog Index, average sentence length, complex word count, percentage of complex words, syllables per word, and more.
- **Personal Pronoun Detection:** Counts personal pronouns to assess writing style.
- **Excel Reporting:** Outputs all computed metrics in a structured Excel file for easy review and further analysis.

## 📊 Example Output
The final output is an Excel file (`output/FinalOutput.xlsx`) with the following columns for each article:
- URL_ID
- URL
- POSITIVE SCORE
- NEGATIVE SCORE
- POLARITY SCORE
- SUBJECTIVITY SCORE
- AVG SENTENCE LENGTH
- PERCENTAGE OF COMPLEX WORDS
- FOG INDEX
- AVG NUMBER OF WORDS PER SENTENCE
- COMPLEX WORD COUNT
- WORD COUNT
- SYLLABLE PER WORD
- PERSONAL PRONOUNS
- AVG WORD LENGTH

Each row represents a fully analyzed article, making it easy to compare sentiment and readability across a large dataset.

## 🧑‍💻 Technical Highlights
- **Python (pandas, openpyxl, BeautifulSoup, lxml, regex)**
- Pure Python tokenization (robust to NLTK issues)
- Modular code: `scraper.py`, `text_analysis.py`, `utils.py`, `main.py`
- Custom stopword and sentiment dictionary support
- Designed for extensibility and clarity

## 📂 Project Structure
```
├── articles/         # Extracted article text files
├── input/            # Input Excel and dictionary files
├── output/           # Final Excel output
├── main.py           # Main pipeline script
├── scraper.py        # Article extraction
├── text_analysis.py  # NLP metrics computation
├── utils.py          # Helper functions
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

## ⚡ How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/shashindra06/Sentiment-and-Readability-Analysis-of-Online-Articles-using-NLP.git
   cd Sentiment-and-Readability-Analysis-of-Online-Articles-using-NLP
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Prepare your input:**
   - Place `Input.xlsx` and dictionary files in the `input/` folder.
   - Use `scraper.py` to generate article `.txt` files in the `articles/` folder, or add them manually.
5. **Run the analysis:**
   ```bash
   python main.py
   ```
6. **Check your results:**
   - Output will be in `output/FinalOutput.xlsx`

## 🌟 Why This Project Stands Out
- **End-to-End Automation:** From raw URLs to actionable Excel reports.
- **Custom NLP Metrics:** Goes beyond basic sentiment to include readability and writing style.
- **Portfolio-Ready:** Clean, modular code and professional documentation.
- **Real-World Application:** Useful for content analysis, journalism, research, and more.

## 👤 Author
(https://github.com/shashindra06)

---

**Ready to use, extend, or showcase!** 