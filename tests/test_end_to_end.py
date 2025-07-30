"""Integration test running the simple NLP pipeline."""

from parser import parse_html
from entity_linking import load_mapping_table, link_entities, detect_entities
from sentiment import analyze_sentiment_by_entity
from bias_detection import detect_bias
from urgency import detect_urgency


def test_pipeline():
    html = """
    <html>
      <head><title>Tesla surges after strong earnings</title></head>
      <body>
        <p>Tesla CEO Elon Musk announced that profits are up.</p>
        <p>This positive result pushed the stock higher.</p>
        <time datetime="2024-01-01">Jan 1, 2024</time>
      </body>
    </html>
    """

    doc = parse_html(html)
    mapping = load_mapping_table("data/mapping_table.csv")
    entities = detect_entities(doc["text"], mapping["Alias/Name"].tolist())
    linked = link_entities(entities, mapping)
    sentiments = analyze_sentiment_by_entity(doc["text"], linked.keys())
    bias_score = detect_bias(doc["text"])
    urgency_score = detect_urgency(doc["text"])

    assert linked.get("Elon Musk") == "TSLA"
    assert isinstance(sentiments.get("Elon Musk"), float)
    assert 0.0 <= bias_score <= 1.0
    assert 0.0 <= urgency_score <= 1.0
