from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup


DUCKDUCKGO_HTML_URL = "https://duckduckgo.com/html/"
DOCS_DOMAIN = "docs.gl-inet.com"


@dataclass(frozen=True)
class SearchResult:
    title: str
    url: str
    snippet: str


def _build_query(tags: Iterable[str]) -> str:
    tags_query = " ".join(tag.strip() for tag in tags if tag.strip())
    if tags_query:
        return f"site:{DOCS_DOMAIN} {tags_query}"
    return f"site:{DOCS_DOMAIN}"


def search_docs(tags: Iterable[str], limit: int = 10) -> list[SearchResult]:
    query = _build_query(tags)
    params = {"q": query}
    response = requests.get(DUCKDUCKGO_HTML_URL, params=params, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    results: list[SearchResult] = []

    for result in soup.select(".result"):
        link = result.select_one("a.result__a")
        if not link or not link.get("href"):
            continue
        title = link.get_text(strip=True)
        url = link["href"]
        snippet_el = result.select_one("a.result__snippet") or result.select_one("div.result__snippet")
        snippet = snippet_el.get_text(" ", strip=True) if snippet_el else ""
        results.append(SearchResult(title=title, url=url, snippet=snippet))
        if len(results) >= limit:
            break

    return results


def build_fallback_url(tags: Iterable[str]) -> str:
    query = _build_query(tags)
    return f"https://duckduckgo.com/?q={quote_plus(query)}"
