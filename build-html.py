#!/usr/bin/env python3
"""
Build docs/index.html from the essay Markdown file.
The MD file is the single source of truth for essay text and the timestamp.
"""

import subprocess
import re
from pathlib import Path

MD  = "My-recollections-of-the-Chinese-Exhibit-at-the-Neleson-Atkins-1975.md"
OUT = "docs/index.html"

# ── Read source ──────────────────────────────────────────────────────────────
text = Path(MD).read_text()

# Extract "Last updated" timestamp from MD
ts_match = re.search(r'Last updated: ([\d-]+ · [\d:]+)', text)
timestamp = ts_match.group(1) if ts_match else ""

# ── Extract essay body ───────────────────────────────────────────────────────
# Keep lines between the opening header block and the first --- separator.
# Skip: # headings, ### headings, "by Jim..." byline, date line (YYYY-MM-DD),
#        and the *Last updated* line.
lines = text.split('\n')
body_lines = []
in_body = False
for line in lines:
    if re.match(r'^---', line):           # stop at separator
        break
    if re.match(r'^#{1,6}\s', line):      # skip headings
        continue
    if re.match(r'^by ', line, re.I):     # skip byline
        continue
    if re.match(r'^\d{4}-\d{2}-\d{2}', line):  # skip date line
        continue
    if re.match(r'^\*Last updated', line):      # skip timestamp line
        continue
    if not in_body and line.strip() == '':      # skip leading blank lines
        continue
    in_body = True
    body_lines.append(line)

body_md = '\n'.join(body_lines).rstrip()

# ── Convert essay body to HTML via pandoc ────────────────────────────────────
result = subprocess.run(
    ['pandoc', '--from', 'markdown+smart', '--to', 'html'],
    input=body_md, capture_output=True, text=True, check=True
)
body_html = result.stdout.strip()

# Indent every line by two spaces to match the rest of the HTML
body_html = '\n'.join(
    ('  ' + line) if line else ''
    for line in body_html.split('\n')
)

# ── Assemble full HTML ───────────────────────────────────────────────────────
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Nights at the Museum</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">

  <h1>My Nights at the Museum</h1>
  <p class="subtitle">Recollections of the Exhibition of Archaeological Finds of the People&#39;s Republic of China, Nelson Gallery-Atkins Museum, 1975</p>
  <p class="byline">by Jim U&#39;Ren &nbsp;&middot;&nbsp; March 07, 2026</p>

{body_html}

  <p class="timestamp"><em>Last updated: {timestamp}</em></p>

  <hr>

  <div class="archival">
    <h2>Archival Materials</h2>

    <div class="gallery">
      <figure>
        <img src="The-Exhibit-Poster.png" alt="Official exhibit poster featuring the Galloping Horse">
        <figcaption>Official exhibit poster featuring the Galloping Horse, April 20&ndash;June 7, 1975</figcaption>
      </figure>
      <figure>
        <img src="The-Prancing-Horse.jpg" alt="Cover of the exhibit program">
        <figcaption>Cover of the exhibit program, <em>The Exhibition of Archaeological Finds of the People&#39;s Republic of China</em></figcaption>
      </figure>
      <figure>
        <img src="Lines-at-the-Museum.jpg" alt="Crowds queued outside the Nelson Gallery-Atkins Museum">
        <figcaption>Crowds queued outside the Nelson Gallery-Atkins Museum beneath the exhibit banner</figcaption>
      </figure>
      <figure>
        <img src="Crowds-at-the-Museum.jpg" alt="Packed galleries inside the museum">
        <figcaption>Inside the packed galleries with American and Chinese flags and calligraphy banners</figcaption>
      </figure>
      <figure>
        <img src="Map-of-the-Exhibit.jpg" alt="Newspaper floor plan of the exhibition maze">
        <figcaption>Newspaper floor plan of the exhibition maze &mdash; &ldquo;entrance-to-exit view of the exhibition maze&rdquo;</figcaption>
      </figure>
      <figure>
        <img src="A-Chime-of-Bronze-Bells.png" alt="Exhibit catalog page featuring Western Zhou Dynasty bronze bells">
        <figcaption>Exhibit catalog page featuring the Western Zhou Dynasty bronze bells</figcaption>
      </figure>
      <figure>
        <img src="Galloping-Horse.jpg" alt="The Galloping Horse, Han Dynasty bronze">
        <figcaption>The Galloping Horse &mdash; Han Dynasty bronze, the centerpiece of the exhibit</figcaption>
      </figure>
      <figure>
        <img src="Chinese-Curator-w-Galloping-Horse.png" alt="Curator handling the Galloping Horse">
        <figcaption>A curator positions the Galloping Horse. Photo: Wang Yuguo / Xinhua News Agency</figcaption>
      </figure>
    </div>

    <div class="audio-section">
      <h3>The Bronze Bells</h3>
      <audio controls>
        <source src="Chinese_Bells.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
      <p>Audio recording of Chinese bells similar to what was played at the Exhibit [courtesy of the Smithsonian Museum]</p>
    </div>

    <div class="video-section">
      <h3>Exhibit Footage</h3>
      <video controls>
        <source src="https://archive.org/download/chinese-exhibit-nelson-atkins-1975/VIDEO_Chinese-Exhibit-at-the-Nelson-Atkins-1975.mp4" type="video/mp4">
        Your browser does not support the video element.
      </video>
      <p>Video footage of visitors at the exhibit, including a delegation from Denver Museum of Nature and Science. [video courtesy of Denver Museum of Nature and Science and PBS station KRMA, Denver, CO]</p>
    </div>

  </div>

  <div class="acknowledgments">
    <h2>Acknowledgments</h2>
    <p>The author wishes to thank Tara Laver, Senior Archivist at the Nelson-Atkins Museum of Art, and all the staff archivists who provided archival materials for this piece.</p>
  </div>

</div>
</body>
</html>
'''

Path(OUT).write_text(html)
print(f"HTML written to {OUT}")
