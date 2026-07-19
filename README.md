# WP2Shell - WordPress REST API Exploitation Framework

Automated exploitation framework for CVE-2026-63030 (REST API batch endpoint route confusion) and CVE-2026-60137 (SQL injection in WP_Query).

## Features

- **Automated vulnerability detection** via timing-based blind SQL injection
- **Admin user escalation** through batch API endpoint confusion
- **Plugin-based RCE** with persistent webshell deployment
- **State persistence** to resume from any phase
- **Interactive shell** for post-exploitation

## Installation

```bash
cd ~/wp2shell
pip install -r requirements.txt
```

## Usage

```bash
# Test vulnerability
python3 main.py https://target.com

# Full exploitation with command execution
python3 main.py https://target.com -c "whoami"

# Resume from saved state
python3 main.py https://target.com -c "id"  # Automatically resumes from phase 5+
```

## Project Structure

```
wp2shell/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
│
├── lib/                    # Shared utilities
│   ├── __init__.py
│   ├── output.py          # Terminal output formatting
│   ├── api.py             # API request handling
│   └── config.py          # SSL/network config
│
├── exploit/               # Exploitation logic
│   ├── __init__.py
│   ├── state.py           # State persistence
│   ├── core.py            # Main Exploit class
│   ├── phases.py          # Individual phase implementations
│   └── shell.py           # Interactive webshell client
│
└── README.md
```

## How It Works

1. **Phase 1 - Detection**: Timing-based SQLi detection via batch API
2. **Phase 2 - Injection**: Inject seed post with oembed URLs
3. **Phase 3 - Config**: Extract database configuration
4. **Phase 4 - Escalation**: Create admin user via SQL injection
5. **Phase 5 - Auth**: Authenticate with created credentials
6. **Phase 6 - Deployment**: Upload and activate plugin webshell
7. **Phase 7 - Shell**: Interactive command execution

## State File

Progress is automatically saved to `~/<domain>.json`:
```json
{
  "phase": 6,
  "timestamp": "2026-07-19T00:54:00Z",
  "data": {
    "username": "Wordpress-System-User",
    "password": "P_...",
    "webshell_url": "https://target.com/?rest_route=/api/v1/...",
    ...
  }
}
```

Resume automatically by running the script again with the same target.

## Technical Details

### CVE-2026-63030
REST API batch endpoint (`/batch/v1`) route confusion allows unauthenticated SQL injection through `$matches` array desynchronization.

### CVE-2026-60137  
`WP_Query` author__not_in parameter vulnerable to type confusion SQLi.

## Disclaimer

For authorized security testing only. Unauthorized access is illegal.
