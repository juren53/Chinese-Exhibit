#!/bin/bash

MDFILE="My-recollections-of-the-Chinese-Exhibit-at-the-Neleson-Atkins-1975.md"
HTMLFILE="${MDFILE%.md}.html"
PDFFILE="${MDFILE%.md}.pdf"

DIR="$(cd "$(dirname "$0")" && pwd)"

pandoc "$DIR/$MDFILE" \
  -o "$DIR/$HTMLFILE" \
  --standalone \
  --css="$DIR/pdf-style.css"

google-chrome --headless --disable-gpu \
  --print-to-pdf="$DIR/$PDFFILE" \
  --print-to-pdf-no-header \
  "file://$DIR/$HTMLFILE" 2>&1

echo "PDF written to $PDFFILE"
