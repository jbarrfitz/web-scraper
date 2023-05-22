import requests
from page_parser import parse


def get_citations_needed_count(url):
    data = parse(url)
    return data[0]


def get_citations_needed_report(url):
    report = "CITATIONS NEEDED REPORT\n\n"
    data = parse(url)
    for entry in data[1]:
        report += f"{entry.text}\n\n"
    return report


print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))
print(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))

