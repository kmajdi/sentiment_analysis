"""Simple HTML parsing utilities."""

from __future__ import annotations

from bs4 import BeautifulSoup

from utils import clean_text


def parse_html(html: str) -> dict:
    """Extract title, publication date and cleaned text from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string.strip() if soup.title else ""

    # Try to find a publication date
    date_tag = soup.find("time")
    if date_tag and date_tag.has_attr("datetime"):
        published = date_tag["datetime"]
    elif date_tag:
        published = date_tag.get_text(strip=True)
    else:
        published = ""

    body_text = " ".join(p.get_text(separator=" ", strip=True) for p in soup.find_all("p"))

    return {
        "title": clean_text(title),
        "date": published,
        "text": clean_text(body_text),
    }


__all__ = ["parse_html"]
