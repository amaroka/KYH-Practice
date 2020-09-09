from pathlib import Path


def main():
    doc = "system.log"
    imp = []
    Key_phrase = ['BEAR', 'X-RAY']
    file = Path(doc).read_text().splitlines()

    for line in file:
        line = line.strip()
        for phrase in Key_phrase:
            if phrase in line:
                imp.append(line)
                break

    print(*imp, sep="\n")

if __name__ == '__main__':
    main()
