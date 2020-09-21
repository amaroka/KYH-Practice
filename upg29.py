from pathlib import Path
import requests
import webbrowser
content = Path("upg29.html").read_text()
r = requests.get("https://api.adviceslip.com/advice")
advice = r.json()
dict = advice["slip"]
value = dict["advice"]

html = content.replace("QUOTE_TEXT", value)
p = Path("goat_quote.html")
p.write_text(html, encoding='utf8')
webbrowser.open("goat_quote.html")


