# WP2Shell - Exploitation Framework

## Status: ✅ COMPLETE

All 7 phases of the exploitation chain are fully functional and tested.

## Completed Phases

1. **Phase 1: Detection** - Timing-based SQLi vulnerability detection via batch API
2. **Phase 2: Post Injection** - Fetches posts and injects oembed cache URLs
3. **Phase 3: Config Extraction** - Extracts database table prefix and admin user ID
4. **Phase 4: User Escalation** - SQL injection gadget chain creates admin user
5. **Phase 5: Authentication** - Authenticates with created credentials via wp-login.php
6. **Phase 6: Plugin Deployment** - Uploads and activates malicious REST API plugin
7. **Phase 7: Interactive Shell** - Interactive webshell with command execution

## Features

- ✅ Full exploitation chain (1-7 phases)
- ✅ State persistence - resume from any phase
- ✅ Timing-based blind SQL injection optimization
- ✅ Plugin concealment - attempts to move webshell to wp-content/plugins.php
- ✅ Error handling and fallback methods
- ✅ Colored progress output
- ✅ Support for WordPress table prefix detection
- ✅ Cache ID extraction with sequential assumption optimization

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Test if target is vulnerable
python3 main.py https://target.com

# Execute command immediately
python3 main.py https://target.com -c "whoami"

# Resume from saved state (automatic)
python3 main.py https://target.com -c "id"
```

## State Files

Exploitation state is saved to `~/{domain}.json` after each phase completes.
This allows resumption of interrupted exploitations.

## Architecture

```
lib/
  ├── api.py          - Batch API request wrapper
  ├── config.py       - SSL configuration
  └── output.py       - Colored terminal output

exploit/
  ├── phases.py       - Phase implementations (1-5)
  ├── core.py         - Plugin deployment & shell (6-7)
  └── state.py        - State persistence

main.py              - Entry point & orchestration
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4

## Targets

Successfully tested against WordPress installations with:
- Custom database table prefixes (wp_, rzb_, etc.)
- Time-delayed SQL injection
- Plugin upload capability
- REST API enabled
