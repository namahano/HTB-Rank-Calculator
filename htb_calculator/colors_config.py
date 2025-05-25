from colorama import Fore, Back, Style, init

init(autoreset=False)

class Colors:
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT

    # 通常の色
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE

    # 明るい色
    BRIGHT_BLACK = Fore.LIGHTBLACK_EX
    BRIGHT_RED = Fore.LIGHTRED_EX
    BRIGHT_GREEN = Fore.LIGHTGREEN_EX
    BRIGHT_YELLOW = Fore.LIGHTYELLOW_EX
    BRIGHT_BLUE = Fore.LIGHTBLUE_EX
    BRIGHT_MAGENTA = Fore.LIGHTMAGENTA_EX
    BRIGHT_CYAN = Fore.LIGHTCYAN_EX
    BRIGHT_WHITE = Fore.LIGHTWHITE_EX

    # 背景色
    BG_RED = Back.RED
    BG_GREEN = Back.GREEN
    BG_YELLOW = Back.YELLOW
    BG_BLUE = Back.BLUE
    BG_MAGENTA = Back.MAGENTA
    BG_CYAN = Back.CYAN