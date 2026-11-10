# waayer.org

> [!IMPORTANT]  
> Repo is being archived due to the root domain no longer being used due to bots hammering and scraping it then the subdomains that they find from the root domain

This is the source code for the website at [waayer.org](https://waayer.org)

everyone is allowed to use this code/repurpose it for their website

## Setup

### Requirements
- Python 3
- A web server (e.g. [Caddy](https://caddyserver.com/))
- API keys for the services you want stats from (Jellyfin, Seerr, Immich, Tracearr)

### 1. Clone and install
```bash
git clone https://github.com/waayer/waayer.org
cd waayer.org
python3 -m pip install -r requirements.txt
```

### 2. Configure your services
```bash
cp example.env .env
```
Open `.env` and fill in the URL and API key for each service. Any service that
isn't reachable will just show "Error" on the site.

### 3. Generate the stats
Run this **from the project root** (the output path is relative):
```bash
python3 app.py
```
This creates `website/stats.json`. To keep stats fresh, run it on a schedule, e.g. every 5 minutes with cron:
```bash
*/5 * * * * cd /path/to/waayer.org && python3 app.py
```

### 4. Serve the site
Point your web server at the `website/` folder, **not** the project root, otherwise your `.env` will be exposed.

Caddy example:
```
yourdomain.com {
    root * /path/to/waayer.org/website
    file_server
}
```

Quick local test:
```bash
python3 -m http.server 8080 -d website
```
Then open http://localhost:8080.

### Optional: Sonarr
Sonarr support is commented out in `app.py` and requires Sonarr v5 (beta).

### NOTICE: coderabbit is only for reviewing pull requests and small edits/changes i do not use it for coding i code stuff myself