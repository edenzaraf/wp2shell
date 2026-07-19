"""Terminal output formatting"""

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

class Output:
    """Formatted terminal output"""

    @staticmethod
    def success(msg):
        print(f"{Colors.GREEN}[+]{Colors.RESET} {msg}")

    @staticmethod
    def error(msg):
        print(f"{Colors.RED}[-]{Colors.RESET} {msg}")

    @staticmethod
    def info(msg):
        print(f"{Colors.BLUE}[*]{Colors.RESET} {msg}")

    @staticmethod
    def verbose(msg):
        print(f"{Colors.CYAN}[~]{Colors.RESET} {msg}")

    @staticmethod
    def phase(num, name):
        print(f"\n{Colors.YELLOW}=== PHASE {num}: {name} ==={Colors.RESET}")

    @staticmethod
    def blank():
        print()
