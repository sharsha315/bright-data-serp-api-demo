# Bright Data SERP API Demo

## Introduction
Easily collect search results from major search engines without managing proxies, CAPTCHAs, or parsing. Start in minutes with a single endpoint.

Supported search engines:
- Google
- Bing
- DuckDuckGo
- Yandex
- Baidu
- Yahoo
- Naver

Choose your output format:
- Markdown
- Raw HTML
- Parsed JSON

No need to handle proxies, CAPTCHAs, or manual parsing—Bright Data SERP API does it for you.

## Before You Start
- [Sign in to Bright Data](https://brightdata.com/cp/start)
- [Create a SERP API zone](https://brightdata.com/cp/zones)
- [Get your API key](https://brightdata.com/api-reference/authentication)

This project demonstrates how to use the Bright Data SERP API to fetch Google search results and display them in a Streamlit web application.

## Features
- Streamlit frontend for entering search keywords
- Integration with Bright Data SERP API
- Collects results from multiple search engines
- Supports Markdown, raw HTML, or parsed JSON output
- Uses environment variables for secure API key management

## Prerequisites
- Python 3.7+
- Bright Data account with access to the SERP API

## Setup Instructions
1. **Clone the repository**
	```bash
	git clone https://github.com/sharsha315/bright-data-serp-api-demo.git
	cd bright-data-serp-api-demo
	```

2. **Create and activate a virtual environment (recommended)**
	```bash
	python3 -m venv venv
	source venv/bin/activate
	```

3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```

4. **Configure your Bright Data API key**
	- Copy your API key from Bright Data dashboard.
	- Create a `.env` file in the project root:
	  ```env
	  BRIGHT_DATA_API_KEY=your_api_key_here
	  ```

## Running the App
Start the Streamlit app:
```bash
streamlit run main.py
```

## Usage
1. Enter a search keyword in the text box.
2. Click the **Search** button.
3. The app will fetch and display search results using the Bright Data SERP API.
4. Results can be displayed in raw HTML, parsed JSON, or Markdown (depending on configuration).

## Configuration
- API key is read from `.env` file using `python-dotenv`.
- The request is sent to Bright Data's API endpoint with the required parameters.

## File Structure
- `main.py` — Streamlit app and API integration logic
- `requirements.txt` — Python dependencies
- `.env` — Environment variables (not committed)
- `README.md` — Project documentation

## Troubleshooting
- **400 Client Error**: Ensure your API key is valid, your Bright Data zone is configured for SERP, and the payload matches API requirements.
- **No results**: Check your API key, zone permissions, and endpoint URL.

## License
This project is licensed under the MIT License.