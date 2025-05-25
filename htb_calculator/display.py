from .colors_config import Colors

TITLE_COLOR = Colors.BRIGHT_GREEN + Colors.BOLD
HEADER_COLOR = Colors.BRIGHT_CYAN + Colors.BOLD
INFO_COLOR = Colors.YELLOW
RANK_COLOR = Colors.BRIGHT_GREEN
ERROR_COLOR_MAIN = Colors.RED + Colors.BOLD
SUCCESS_COLOR = Colors.GREEN + Colors.BOLD
BAR_COLOR_TABLE = Colors.BRIGHT_BLUE
TEXT_COLOR_DATA = Colors.WHITE
PERC_COLOR_DATA = Colors.BRIGHT_YELLOW
RESET = Colors.RESET

def print_welcome_banner():
    print(f"{TITLE_COLOR} Hack The Box ランクアップ計算機 {RESET}")
    print(f"{HEADER_COLOR}-------------- 設定値 --------------{RESET}")

def print_configuration(total_machines, total_challenges, denominator):
    #print(f"{HEADER_COLOR}設定値:{RESET}")
    print(f"総マシン数        : {INFO_COLOR}{total_machines}{RESET}")
    print(f"総チャレンジ数    : {INFO_COLOR}{total_challenges}{RESET}")
    print(f"所有率計算式の分母: {INFO_COLOR}{denominator:.2f}{RESET}")
    print(f"{HEADER_COLOR}------------------------------------{RESET}\n")

def print_current_status(sys_owns, user_owns, chall_owns, percentage, rank_name):
    print(f"\n{HEADER_COLOR}------------ 現在の状況 ------------{RESET}")
    print(f"現在のシステム所有数   : {INFO_COLOR}{sys_owns}{RESET}")
    print(f"現在のユーザー所有数   : {INFO_COLOR}{user_owns}{RESET}")
    print(f"現在のチャレンジ所有数 : {INFO_COLOR}{chall_owns}{RESET}")
    print(f"現在の所有率           : {INFO_COLOR}{percentage:.2f}%{RESET}")
    print(f"現在のランク (計算結果): {RANK_COLOR}{rank_name}{RESET}")
    print(f"{HEADER_COLOR}------------------------------------{RESET}\n")

def print_target_rank_info(next_rank_name, target_percentage_for_next_rank):
    target_display = f"{target_percentage_for_next_rank}%"
    if next_rank_name == "Omniscient":
        target_display_full = f"{INFO_COLOR}{target_display} (100% 達成){RESET}"
    else:
        target_display_full = f"{INFO_COLOR}>{target_display}{RESET}"
    print(f"{HEADER_COLOR}次の目標ランク: {RANK_COLOR}{next_rank_name}{RESET} (目標所有率: {target_display_full})")

def print_already_max_rank():
    print(f"{SUCCESS_COLOR}おめでとうございます！あなたは既に最高ランク Omniscient です！{RESET}")

def print_no_next_rank_info():
    print(f"{ERROR_COLOR_MAIN}次のランク情報を取得できませんでした。{RESET}")

def print_already_meets_next_rank(next_rank_name):
    print(f"{INFO_COLOR}既に次のランク ({RANK_COLOR}{next_rank_name}{INFO_COLOR}) の所有率条件をほぼ満たしているか、超えています。{RESET}")

def print_combinations_table(combinations, next_rank_name, target_percentage_for_next_rank):
    target_display = f"{target_percentage_for_next_rank}%"
    is_omniscient_target = (next_rank_name == "Omniscient")
    if is_omniscient_target:
        target_display_full = f"{INFO_COLOR}{target_display} (100% 達成){HEADER_COLOR}"
    else:
        target_display_full = f"{INFO_COLOR}>{target_display}{HEADER_COLOR}"

    print(f"\n{HEADER_COLOR}     --- {RANK_COLOR}{next_rank_name}{HEADER_COLOR} ({target_display_full}{HEADER_COLOR}) 達成のための組み合わせ例 ---{RESET}")
    print(f"{BAR_COLOR_TABLE}{Colors.BOLD}|-----------------------------------------------------------------|{RESET}")
    print(f"{BAR_COLOR_TABLE}{Colors.BOLD}| 追加システム | 追加ユーザー | 追加チャレンジ | 結果の所有率 (%) |{RESET}")
    print(f"{BAR_COLOR_TABLE}{Colors.BOLD}|--------------|--------------|----------------|------------------|{RESET}")

    if not combinations:
        message = "表示できる組み合わせは見つかりませんでした。"
        total_width = 12 + 1 + 12 + 1 + 14 + 1 + 16
        print(f"{BAR_COLOR_TABLE}|{INFO_COLOR}{message:^{total_width+4}}{RESET}{BAR_COLOR_TABLE}|{RESET}")
    else:
        for s, u, c, perc in combinations:
            print(f"{BAR_COLOR_TABLE}|{RESET} "
                  f"{TEXT_COLOR_DATA}{s:<12}{RESET} "
                  f"{BAR_COLOR_TABLE}|{RESET} "
                  f"{TEXT_COLOR_DATA}{u:<12}{RESET} "
                  f"{BAR_COLOR_TABLE}|{RESET} "
                  f"{TEXT_COLOR_DATA}{c:<14}{RESET} "
                  f"{BAR_COLOR_TABLE}|{RESET} "
                  f"{PERC_COLOR_DATA}{perc:<16.2f}{RESET} "
                  f"{BAR_COLOR_TABLE}|{RESET}")
    print(f"{BAR_COLOR_TABLE}{Colors.BOLD}|-----------------------------------------------------------------|{RESET}")

def print_no_specific_combinations_after_filtering():
    print(f"{INFO_COLOR}指定された条件で目標を達成する具体的な組み合わせは見つかりませんでした。{RESET}")


def print_no_combinations_found_at_all(next_rank_name, total_machines, total_challenges):
    rank_msg_part = next_rank_name if next_rank_name else '次のランク'
    print(f"{ERROR_COLOR_MAIN}{rank_msg_part} を達成するための組み合わせは見つかりませんでした。{RESET}")
    print(f"{INFO_COLOR}必要な所有数が現在の最大値を超えている可能性があります。{RESET}")
    print(f"(例: システム {total_machines}個、チャレンジ {total_challenges}個すべて所有しても届かない場合)")