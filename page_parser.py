import requests
from bs4 import BeautifulSoup


def parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    citations = soup.find_all(title="Wikipedia:Citation needed")
    citation_context = set()
    citation_num = len(citations)
    for citation in citations:
        citation_num += 1
        citation_context.add(citation.parent.parent.parent)
    return [citation_num, citation_context]
