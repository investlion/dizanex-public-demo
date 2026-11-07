# Public Demo Security Checklist

- [ ] Publish only the generated `public_demo_package.zip` contents or a clean copy of this folder.
- [ ] Confirm `.env`, `.env.*`, API keys, Telegram tokens, credentials, and private certificates are absent.
- [ ] Confirm production `.db`, `.sqlite`, WAL/SHM files, logs, heartbeat files, and backups are absent.
- [ ] Confirm no `app/`, `run_scanner.py`, `scripts/`, production settings, or proprietary engine modules are included.
- [ ] Keep `requirements.txt` limited to the Streamlit UI dependency set.
- [ ] Review the generated archive file list before submitting it to Codester or publishing a repository.
- [ ] Leave sample labels visible on every page and do not describe sample records as live.
- [ ] Do not add public database access, trading actions, Telegram delivery, or credential entry fields.
- [ ] Do not publish or upload until the owner explicitly approves the destination and release.
