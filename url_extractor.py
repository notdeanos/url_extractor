#!/usr/bin/env python3
#
# Dean Mcdonald <dean@appdome.com> (c) Appdome, Inc 2023.
#
# NO SUPPORT OR WARRANTY
#
# This script reads in any ASCII file and prints all the URLs. Any non-HTTPs will be indicated by an asterisk.
#

import sys
import re
from urllib.parse import urlparse

def extract_urls_from_text(text):
    pattern = r"(http[s]?://\S+)"
    raw_urls = re.findall(pattern, text)
    urls = []
    for url in raw_urls:
        parsed_url = urlparse(url)
        stripped_url = parsed_url.scheme + "://" + parsed_url.netloc
        if "api.mixpanel.com" not in stripped_url:
            urls.append("Non-TLS -> " + stripped_url if stripped_url.startswith("http://") else stripped_url)
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
