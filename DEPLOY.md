# Deploy

GitHub Pages, main branch, root. Static files only, no build step.

## Custom domain (once docenta.io is registered)

1. Add a `CNAME` file containing `docenta.io` to the repo root.
2. At the registrar: `A` records for the apex to GitHub Pages IPs
   (185.199.108.153 / .109 / .110 / .111) and a `CNAME` record
   `www -> skyllc-ai.github.io`.
3. In repo Settings -> Pages: set the custom domain, enable
   "Enforce HTTPS" after the certificate is issued.
4. Update the `og:image` URL in `index.html` to the docenta.io origin.

## Early-access mailbox

The CTA points at `docenta@nios.net`. Create that alias before
announcing the page anywhere.
