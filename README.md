# 🧠 Financial News Sentiment Extraction

This project aims to extract structured financial insights from raw HTML news articles. It focuses on identifying relevant stocks, evaluating sentiment, detecting bias, and estimating urgency. The output is useful for automated financial monitoring, alerts, and investment decision support.

---

## ✅ Project Goals

From a raw HTML news article (`news_html_full`), extract the following structured fields:

- `news_id`: Unique identifier for the article
- `news_time`: Date/time of publication (parsed from HTML)
- `news_bias`: Score (0–1) indicating how biased/promotional the content is
- `entities`: A list of `{stock_name, sentiment}` pairs
  - `stock_name` may be inferred from aliases like CEOs, products, etc.
  - `sentiment` is a real number in [-1, 1]
- `urgence`: Score indicating how time-sensitive the news is

---

## 🧠 NLP Pipeline Overview

### 1. HTML Parsing
Extracts:
- Title
- Publication Date (`news_time`)
- Author (if available)
- Main body content

**Tools:** BeautifulSoup, newspaper3k

---

### 2. Named & Indirect Entity Detection
Goal: Identify all company-related mentions (e.g. Tesla, iPhone, Elon Musk).

**Approach:**
- NER using spaCy or Transformers
- Entity linking via custom or external DBs
- Alias resolution for people, products, subsidiaries

**Example Mapping Table:**
| Alias       | Type    | Company     | Ticker |
|-------------|---------|-------------|--------|
| Elon Musk   | Person  | Tesla       | TSLA   |
| iPhone      | Product | Apple       | AAPL   |
| OpenAI      | Org     | Microsoft   | MSFT   |

---

### 3. Aspect-Based Sentiment Analysis (ABSA)
Goal: Extract sentiment for each identified stock/company.

**Output:** Sentiment ∈ [-1, 1] per entity

**Tools:**
- FinBERT, RoBERTa-financial
- LLM prompting (optional)

---

### 4. Bias Detection
Goal: Score how biased/promotional the article is.

**Output:** `news_bias` ∈ [0, 1]  
0 = Neutral/Factual, 1 = Promotional/Artificial

**Techniques:**
- Binary classifier (true news vs ads)
- Rule-based signals (buzzwords, domain trust, etc.)

---

### 5. Urgency Detection
Goal: Flag news that requires immediate attention.

**Examples:**
- Earnings announcements
- Legal cases or resignations
- Breaking events

**Output:** `urgence` ∈ [0, 1] or categories (`low`, `medium`, `high`)

---

## 📦 Project Structure

```
financial_news_sentiment/
│
├── main.py                    # Pipeline entry
├── config.yaml                # Configuration
├── requirements.txt           # Dependencies
├── data/                      # Raw/processed data, mapping table
├── parser/                    # HTML parsing logic
├── entity_linking/            # NER + stock mapping
├── sentiment/                 # Sentiment analysis (ABSA)
├── bias_detection/            # Bias detection model
├── urgency/                   # Urgency classification
├── models/                    # Pretrained/fine-tuned models
└── tests/                     # Unit and integration tests
```

---

## 🚀 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run main pipeline
python main.py
```

---

## 🧪 Tests

Basic tests are included under `/tests/`. You can run them using:

```bash
pytest tests/
```

---

## 📬 Contributions

PRs and improvements are welcome! This is a work-in-progress framework intended to evolve.


