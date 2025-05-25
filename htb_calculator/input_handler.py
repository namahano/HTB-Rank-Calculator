from .colors_config import Colors
from .htb_config import TOTAL_ACTIVE_MACHINES, TOTAL_ACTIVE_CHALLENGES

def get_user_inputs():
    while True:
        try:
            prompt_color = Colors.CYAN
            input_color = Colors.BRIGHT_YELLOW
            reset = Colors.RESET
            error_display_color = Colors.RED

            current_sys_owns = int(input(
                f"{prompt_color}現在のアクティブシステム所有数を入力してください (0-{TOTAL_ACTIVE_MACHINES}): {input_color}{reset}"
            ))
            if not (0 <= current_sys_owns <= TOTAL_ACTIVE_MACHINES):
                raise ValueError(f"システム所有数は0から{TOTAL_ACTIVE_MACHINES}の間でなければなりません。")

            current_user_owns = int(input(
                f"{prompt_color}現在のアクティブユーザー所有数を入力してください (0-{current_sys_owns}): {input_color}{reset}"
            ))
            if not (0 <= current_user_owns <= TOTAL_ACTIVE_MACHINES):
                raise ValueError(f"ユーザー所有数は0から{TOTAL_ACTIVE_MACHINES}の間でなければなりません。")
            if current_user_owns > current_sys_owns:
                raise ValueError("ユーザー所有数はシステム所有数を超えることはできません。")

            current_chall_owns = int(input(
                f"{prompt_color}現在のアクティブチャレンジ所有数を入力してください (0-{TOTAL_ACTIVE_CHALLENGES}): {input_color}{reset}"
            ))
            if not (0 <= current_chall_owns <= TOTAL_ACTIVE_CHALLENGES):
                raise ValueError(f"チャレンジ所有数は0から{TOTAL_ACTIVE_CHALLENGES}の間でなければなりません。")

            return current_sys_owns, current_user_owns, current_chall_owns
        except ValueError as e:
            print(f"{error_display_color}{Colors.BOLD}入力エラー: {e}{Colors.RESET} 再度入力してください。")