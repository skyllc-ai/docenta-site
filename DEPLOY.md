# Deploy

The page is served by Cloudflare Workers assets on the docenta.ai zone:
static files, no build step, no script. From this directory:

    npx wrangler deploy

That uploads `index.html` and `assets/` (everything `.assetsignore` does
not exclude) and binds the custom domains `docenta.ai` and
`www.docenta.ai`; Cloudflare creates the DNS records and the
certificates on first deploy. The wrangler login is the docenta
Cloudflare account (the same one the license worker deploys with).

Verify: `dig +short docenta.ai` answers with Cloudflare addresses and
`curl -s https://docenta.ai/ | grep '<title>'` prints the page title.

The older GitHub Pages copy (main branch, root; reachable as
https://uffs.io/docenta-site/ because the organization's Pages domain is
uffs.io) stays until it is switched off in the repository settings.
