import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')

class Djur:
    def __init__(self, name,carnivore,wiki_url):
        self.wiki_url = wiki_url
        self.carnivore = carnivore
        self.name = name
    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vegetarian"
    def get_html_table_row(self, html):
        html += f'<tr><td><a href="{d.wiki_url}">{d.name}</td><td>{cell_2}</td></tr>\n'
        return html
if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    jaguar = Djur('Jaguar', True, 'https://sv.wikipedia.org/wiki/Jaguar')
    giraff = Djur('Giraff', False, 'https://sv.wikipedia.org/wiki/Giraff')
    panda = Djur('Jättepanda', False, 'https://sv.wikipedia.org/wiki/J%C3%A4ttepanda')
    djur.append(zebra)
    djur.append(tiger)
    djur.append(jaguar)
    djur.append(giraff)
    djur.append(panda)
    html = '<html><table>'
    for d in djur:
        cell_2 = d.carnivore_or_vegetarian()
        html = d.get_html_table_row(html)

    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))