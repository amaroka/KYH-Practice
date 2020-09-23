import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')

class Djur:
    def __init__(self, name,carnivore,wiki_url):
        self.wiki_url = wiki_url
        self.carnivore = carnivore
        self.name = name
#
#
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
        cell_2 = 'Vegetarian'
        if d.carnivore:
           cell_2 = 'Köttätare'
        html += f'<tr><td><a href="{d.wiki_url}">{d.name}</td><td>{cell_2}</td></tr>\n'
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))