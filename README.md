# My Nights at the Museum

**Recollections of the Exhibition of Archaeological Finds of the People's Republic of China,
Nelson Gallery-Atkins Museum, 1975**

*A personal memoir essay by Jim U'Ren*

---

In the spring of 1975, a landmark exhibition of ancient Chinese artifacts traveled to Kansas City, drawing enormous crowds to the Nelson Gallery-Atkins Museum. This essay recounts working the graveyard shift as part of the after-hours crew — restoring the galleries each night before the next day's visitors arrived — and what it meant to be a young man with a dry brush and a red carpet to protect.

## Read the essay

- **Full version (with archival photos, audio, and video):**
  https://juren53.github.io/Chinese-Exhibit/

- **Kansas City Star guest commentary (shorter version):**
  https://www.kansascity.com/opinion/readers-opinion/guest-commentary/article315521111.html

## Repository contents

| File | Description |
|------|-------------|
| `My-recollections-of-the-Chinese-Exhibit-at-the-Nelson-Atkins-1975.md` | Essay source — edit this file |
| `docs/index.html` | Generated HTML (do not edit directly) |
| `docs/style.css` | Web stylesheet |
| `My-recollections-of-the-Chinese-Exhibit-at-the-Nelson-Atkins-1975.pdf` | PDF version |
| `My-recollections-of-the-Chinese-Exhibit-at-the-Nelson-Atkins-1975-KC-Star.md` | Shorter KC Star version |
| `make-html.sh` | Regenerates `docs/index.html` from the MD file |
| `make-pdf.sh` | Regenerates the PDF |
| `build-html.py` | HTML assembly script (edit for archival section changes) |

## Building

```bash
bash make-html.sh   # regenerate docs/index.html
bash make-pdf.sh    # regenerate PDF
```

Requires [pandoc](https://pandoc.org/) and a headless Chrome/Chromium installation.

## Archival materials

Photos, audio, and video are hosted on the Internet Archive under the identifier
`chinese-exhibit-nelson-atkins-1975`. The archival section of the web page streams
video directly from the Internet Archive (files are too large for GitHub).
