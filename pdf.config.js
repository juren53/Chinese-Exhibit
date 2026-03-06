module.exports = {
  css: `
    body {
      font-size: 13pt;
      font-family: Georgia, serif;
      line-height: 1.7;
      max-width: 680px;
      margin: 0 auto;
    }
    h1 { font-size: 20pt; margin-bottom: 4pt; }
    h3 { font-size: 13pt; font-weight: normal; margin-top: 0; }
    p { margin: 0 0 10pt 0; }
    em { font-style: italic; }
  `,
  pdf_options: {
    format: 'Letter',
    margin: {
      top: '1in',
      right: '1in',
      bottom: '1.2in',
      left: '1in',
    },
    displayHeaderFooter: true,
    headerTemplate: `
      <div style="font-size:9pt; font-family:Georgia,serif; width:100%; text-align:center; padding: 0 72pt; color:#555;">
        My Nights at the Museum
      </div>`,
    footerTemplate: `
      <div style="font-size:9pt; font-family:Georgia,serif; width:100%; display:flex; justify-content:space-between; padding: 0 72pt; color:#555;">
        <span class="date"></span>
        <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
      </div>`,
  },
};
