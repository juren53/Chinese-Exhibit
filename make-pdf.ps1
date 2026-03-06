# make-pdf.ps1 — Generate PDF from Markdown using Pandoc and Chrome
# Requirements: pandoc, Google Chrome, Ubuntu font installed on Windows

$DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$MDFILE = "My-recollections-of-the-Chinese-Exhibit-at-the-Neleson-Atkins-1975.md"
$HTMLFILE = $MDFILE -replace '\.md$', '.html'
$PDFFILE  = $MDFILE -replace '\.md$', '.pdf'
$CSSFILE  = "pdf-style-windows.css"

# Generate a Windows-compatible CSS file
@"
@font-face {
  font-family: 'Ubuntu';
  src: url('file:///C:/Windows/Fonts/Ubuntu-R.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Ubuntu';
  src: url('file:///C:/Windows/Fonts/Ubuntu-B.ttf') format('truetype');
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'Ubuntu';
  src: url('file:///C:/Windows/Fonts/Ubuntu-RI.ttf') format('truetype');
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: 'Ubuntu';
  src: url('file:///C:/Windows/Fonts/Ubuntu-BI.ttf') format('truetype');
  font-weight: bold;
  font-style: italic;
}

body {
  font-family: 'Ubuntu', sans-serif;
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
"@ | Set-Content "$DIR\$CSSFILE" -Encoding UTF8

# Generate HTML from Markdown
pandoc "$DIR\$MDFILE" `
  -o "$DIR\$HTMLFILE" `
  --standalone `
  --css="$DIR\$CSSFILE"

# Find Chrome
$ChromePaths = @(
  "$env:PROGRAMFILES\Google\Chrome\Application\chrome.exe",
  "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe",
  "${env:PROGRAMFILES(x86)}\Google\Chrome\Application\chrome.exe"
)
$Chrome = $ChromePaths | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $Chrome) {
  Write-Error "Google Chrome not found. Please install Chrome and try again."
  exit 1
}

# Convert HTML to PDF
& $Chrome --headless --disable-gpu `
  "--print-to-pdf=$DIR\$PDFFILE" `
  --print-to-pdf-no-header `
  "file:///$DIR\$HTMLFILE" 2>&1

Write-Host "PDF written to $PDFFILE"
