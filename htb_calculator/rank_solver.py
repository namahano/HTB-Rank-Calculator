import math
from .htb_config import TOTAL_ACTIVE_MACHINES, TOTAL_ACTIVE_CHALLENGES, OWNERSHIP_DENOMINATOR
from .htb_utils import calculate_ownership_percentage

def calculate_needed_values(current_sys_owns, current_user_owns, current_chall_owns, target_percentage_for_next_rank, next_rank_name, epsilon=1e-7):
    if next_rank_name == "Omniscient":
        required_numerator = (target_percentage_for_next_rank / 100.0) * OWNERSHIP_DENOMINATOR
    else:
        required_numerator = ((target_percentage_for_next_rank + epsilon) / 100.0) * OWNERSHIP_DENOMINATOR

    current_numerator_value = current_sys_owns + (current_user_owns / 2.0) + (current_chall_owns / 10.0)
    needed_numerator_increase = required_numerator - current_numerator_value
    return needed_numerator_increase, current_numerator_value


def find_rank_up_combinations(current_sys_owns, current_user_owns, current_chall_owns, needed_numerator_increase, next_rank_name, target_percentage_for_next_rank, epsilon=1e-7):
    
    combinations = []
    for add_sys in range(TOTAL_ACTIVE_MACHINES - current_sys_owns + 1):
        new_total_sys_owns = current_sys_owns + add_sys
        max_add_user = TOTAL_ACTIVE_MACHINES - current_user_owns
        max_add_user = min(max_add_user, new_total_sys_owns - current_user_owns)

        for add_user in range(max_add_user + 1):
            if add_user < 0: continue
            new_total_user_owns = current_user_owns + add_user

            points_from_machines = add_sys * 1.0 + add_user * 0.5
            remaining_points_needed = needed_numerator_increase - points_from_machines

            add_chall = 0
            if remaining_points_needed <= 0:
                add_chall = 0
            else:
                add_chall_float = remaining_points_needed / 0.1
                calc_epsilon = 1e-9
                add_chall = math.ceil(add_chall_float - calc_epsilon)
                if add_chall < 0: add_chall = 0

            if current_chall_owns + add_chall <= TOTAL_ACTIVE_CHALLENGES:
                final_percentage_check = calculate_ownership_percentage(
                    new_total_sys_owns, new_total_user_owns, current_chall_owns + add_chall
                )
                achieved = False

                if next_rank_name == "Omniscient":
                    if math.isclose(final_percentage_check, 100.0, abs_tol=epsilon):
                         achieved = True
                else:
                    if final_percentage_check > target_percentage_for_next_rank + epsilon:
                        achieved = True
                
                if achieved:
                    combinations.append((add_sys, add_user, int(add_chall), final_percentage_check))
    return combinations

def filter_and_sort_combinations(combinations):
    if not combinations:
        return []
    
    sorted_combinations = sorted(combinations, key=lambda x: (x[0] + x[1] + x[2], x[0], x[1], x[2], x[3]))
    
    filtered_combinations = []
    last_key = None
    for s, u, c, perc in sorted_combinations:
        current_key = (s, u, c)
        if last_key != current_key:
            filtered_combinations.append((s, u, c, perc))
            last_key = current_key
    return filtered_combinations