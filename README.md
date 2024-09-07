# HTTP Headers

HTTP Headers is a Python package designed to retrieve and display HTTP response headers from specified web domains. This utility is ideal for web developers, security analysts, and IT professionals who need to inspect the headers sent by web servers for security audits, compliance checks, and debugging purposes.

## Features

- **Simple Interface**: Prompt-based input for domain names, making it user-friendly.
- **Automatic Formatting**: Prepends necessary protocols and formats output for easy readability.
- **Error Handling**: Robust error management for unreachable domains or network issues.
- **Logging Capability**: Outputs are saved into `HTTPHeaders.log` for historical analysis.

## Prerequisites

Before you run the HTTP Headers package, ensure you have the following:
- Python 3.x installed on your machine
- `requests` module installed, which can be done via pip:

```
pip install requests
