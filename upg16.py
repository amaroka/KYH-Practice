import pathlib

p = pathlib.Path('system.log')
content = p.read_text()


def main():
    doc = "system.log"
    imp = []
    Key_phrase = ['BEAR', 'X-RAY']

    with open(doc) as f:
        f = f.readlines()

    for line in f:
        line = line.strip()
        for phrase in Key_phrase:
            if phrase in line:
                imp.append(line)
                break

    print(*imp, sep="\n")

if __name__ == '__main__':
    main()
