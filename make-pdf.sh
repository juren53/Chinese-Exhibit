#!/bin/bash

MDFILE="My-recollections-of-the-Chinese-Exhibit-at-the-Neleson-Atkins-1975.md"
HTMLFILE="${MDFILE%.md}.html"
PDFFILE="${MDFILE%.md}.pdf"

DIR="$(cd "$(dirname "$0")" && pwd)"

pandoc "$DIR/$MDFILE" \
  -o "$DIR/$HTMLFILE" \
  --standalone \
  --css=/dev/stdin <<'EOF'
body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 20px;
  line-height: 1.7;
  max-width: 780px;
  margin: 40px auto;
  padding: 0 40px;
  color: #222;
}
header#title-block-header { display: none; }
h1 { font-size: 2em; }
h3 { font-size: 1.1em; font-weight: normal; color: #444; }
p { margin: 1em 0; }
em { font-style: italic; }
EOF

google-chrome --headless --disable-gpu \
  --print-to-pdf="$DIR/$PDFFILE" \
  --print-to-pdf-no-header \
  "file://$DIR/$HTMLFILE" 2>&1

echo "PDF written to $PDFFILE"
