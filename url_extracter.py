#!/usr/bin/env python3
#
#
# Dean Mcdonald <dean@appdome.com> (c) Appdome, Inc 2023.
#
# NO SUPPORT OR WARRANTY
#

import sys
import re
from urllib.parse import urlparse

def extract_urls_from_text(text):
    pattern = r"(http[s]?://\S+)"
    raw_urls = re.findall(pattern, text)
    urls = [urlparse(url).scheme + "://" + urlparse(url).netloc for url in raw_urls]
    urls = ["* " + url if url.startswith("http://") else url for url in urls]
    return urls


def filter_non_http_urls(text):
    urls = extract_urls_from_text(text)
    filtered_urls = set()

    for url in urls:
        filtered_urls.add(url)

    return "\n".join(sorted(filtered_urls))

# Check if the file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the log file path as an argument.")
    sys.exit(1)

# Retrieve the log file path from the command-line arguments
file_path = sys.argv[1]

# Read the input text file
try:
    with open(file_path, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)

# Filter out non-http URLs
filtered_text = filter_non_http_urls(text)

# Print the filtered text
print(filtered_text)
