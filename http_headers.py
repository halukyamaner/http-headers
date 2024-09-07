"""
Library: HTTP Headers
Author: Haluk YAMANER
Email: haluk@halukyamaner.com
Web: https://www.halukyamaner.com
Version: 1.0

Description:
    HTTP Headers is a simple Python library that retrieves and displays HTTP response headers from a specified 
    web domain. It is an essential tool for web developers and security analysts, providing insights into 
    the headers that web servers send, which are crucial for security, compliance, and debugging purposes.

Usage:
    The script is run from the command line. Upon execution, users are prompted to enter a web domain 
    (without http/https), and the script prepends the necessary protocols to make a secure HTTP request. 
    It then fetches and displays the headers in a clear, readable format.

Requirements:
    Python 3.x
    Modules: requests

Features:
    - Simple and intuitive user interface that asks for domain input and displays HTTP headers.
    - Automatically formats and prints the response headers for easy analysis.
    - Includes error handling for unreachable domains or network issues.
    - Provides detailed information about each header, aiding in educational and troubleshooting efforts.
"""
import requests

# Ask the user for the domain without http/https
domain = input("Please enter the website domain (without http:// or https://): ")

# Automatically prepend https:// to the domain
url = f"https://{domain}"

try:
    # Make a request to the URL
    response = requests.get(url)

    # Print the headers in a human-readable format
    print("\nHTTP Response Headers:\n")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
except requests.exceptions.RequestException as e:
    print(f"Failed to reach {url}. Error: {e}")
