import requests
from bs4 import BeautifulSoup


def parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    citations = soup.select("a[href='https://en.wikipedia.org/wiki/Wikipedia:Citation_needed']")
    citation_context = {}
    citation_num = 0
    for citation in citations:
        citation_num += 1
        citation_context.add(citation.parent)
    return [citation_num, citation_context]
