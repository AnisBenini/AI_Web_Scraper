# AI Web Scraper

A lightweight AI-powered web scraper built with **Streamlit**, **Selenium**, and **Ollama (LLaMA 3.2 1B)** for dynamic content parsing. This tool extracts, cleans, and analyzes website content effortlessly.

##### --> i just need to fix the capatcha of some websites | trying to use a larger LLM
---

## 🚀 Features
- **Dynamic Web Scraping:** Handles JavaScript-rendered content.
- **AI-Powered Parsing:** Extracts specific data using LLaMA 3.2.
- **Clean UI:** Simple Streamlit interface.
- **Content Cleaning:** Removes scripts and unwanted HTML noise.

---

## ⚙️ Installation
```bash
git clone https://github.com/AnisBenini/ai_web_scraper.git
cd ai_web_scraper
pip install -r requirements.txt
```

---

## 🖥️ Usage
```bash
streamlit run main.py
```

1. **Enter the website URL** you want to scrape.
2. Click **"Scrape Site"** to fetch and clean the DOM content.
3. Provide a **description** of what you want to parse.
4. Click **"Parse Content"** to get AI-processed results.

---

## 📦 Project Structure
```
ai-web-scraper/
├── main.py          # Streamlit UI
├── chromedriver
├── scrap.py         # Web scraping logic (Selenium, BeautifulSoup)
├── parse.py         # AI parsing with Ollama (LLaMA 3.2)
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

---

## 🧪 Requirements
- **Python 3.8+**
- **ChromeDriver** (Ensure it's compatible with your browser version)

---

## ⚡ Troubleshooting
- **CAPTCHA Issues?** Try using stealth mode with `undetected-chromedriver`.
- **Parsing Errors?** Verify the `parse_description` input is clear and concise.

---

## 🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first.

---

```bash
# Happy Scraping! 🚀
```

