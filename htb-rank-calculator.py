import math

from htb_calculator import htb_config
from htb_calculator import htb_utils
from htb_calculator import input_handler as input_handler
from htb_calculator import display as display
from htb_calculator import rank_solver as rank_solver

def run_calculator():
    display.print_welcome_banner()
    display.print_configuration(htb_config.TOTAL_ACTIVE_MACHINES, htb_config.TOTAL_ACTIVE_CHALLENGES, htb_config.OWNERSHIP_DENOMINATOR)

    current_sys_owns, current_user_owns, current_chall_owns = input_handler.get_user_inputs()

    current_percentage = htb_utils.calculate_ownership_percentage(current_sys_owns, current_user_owns, current_chall_owns)
    current_rank_name = htb_utils.get_current_rank_by_percentage(current_percentage)

    display.print_current_status(current_sys_owns, current_user_owns, current_chall_owns, current_percentage, current_rank_name)

    next_rank_name, target_percentage_for_next_rank = htb_utils.get_next_rank_details(current_rank_name)

    if not next_rank_name:
        if current_rank_name == "Omniscient":
            display.print_already_max_rank()
        else:
            display.print_no_next_rank_info()
        return

    display.print_target_rank_info(next_rank_name, target_percentage_for_next_rank)

    epsilon = 1e-7
    needed_numerator_increase, current_numerator_value = rank_solver.calculate_needed_values(current_sys_owns, current_user_owns, current_chall_owns, target_percentage_for_next_rank, next_rank_name, epsilon)
    
    if needed_numerator_increase <= 0:
        if not (next_rank_name == "Omniscient" and math.isclose(current_percentage, 100.0, abs_tol=epsilon)):
            display.print_already_meets_next_rank(next_rank_name)
    
    raw_combinations = rank_solver.find_rank_up_combinations(current_sys_owns, current_user_owns, current_chall_owns, needed_numerator_increase, next_rank_name, target_percentage_for_next_rank, epsilon)

    if raw_combinations:
        filtered_combinations = rank_solver.filter_and_sort_combinations(raw_combinations)
        display.print_combinations_table(filtered_combinations, next_rank_name, target_percentage_for_next_rank)
        if not filtered_combinations:
            pass
            
    else:
        display.print_no_combinations_found_at_all(next_rank_name, htb_config.TOTAL_ACTIVE_MACHINES, htb_config.TOTAL_ACTIVE_CHALLENGES)

if __name__ == "__main__":
    run_calculator()