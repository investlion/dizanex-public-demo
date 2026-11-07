# DizaNEX Codester Public Demo

This folder is a standalone Streamlit preview package. It contains a small set of static, illustrative records to demonstrate the dashboard layout, filters, signal table, rejection view, and charts.

Every page is labeled **DEMO DATA — NOT LIVE**. The app has no scanner integration, database access, exchange connection, API credentials, Telegram delivery, or order execution. Missing signal levels display as a dash; the demo does not fill them in.

## Run locally

Requires Python 3.10 or newer.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit. No `.env` file or production configuration is needed.

## Streamlit hosting preparation

For a public preview, publish only the contents of this folder in a separate public demo repository after approval. In Streamlit Community Cloud, select that repository, use `app.py` as the entry point, and install `requirements.txt`. The app is also suitable for another Streamlit host that installs this requirements file.

This package has not been deployed or uploaded. Do not add the private DizaNEX repository, production database, scanner logs, credentials, or runtime heartbeat to the public repository. Keep the demo static; do not add a connection to production services.

## Files

- `app.py` — responsive Streamlit UI and page navigation
- `demo_data.py` — static sample market, signal, and rejection records
- `requirements.txt` — Streamlit only
- `.streamlit/config.toml` — dark theme, minimal toolbar, hidden error detail, and disabled usage statistics
- `SECURITY_CHECKLIST.md` — release checks

The package is built from an explicit file allowlist with `build_package.py`; engine modules and repository-level files are not included.
