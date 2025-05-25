from .htb_config import OWNERSHIP_DENOMINATOR, RANK_THRESHOLDS, RANK_ORDERED_LIST


def calculate_ownership_percentage(sys_owns, user_owns, chall_owns):
    if OWNERSHIP_DENOMINATOR == 0:
        return 0.0
    numerator = sys_owns + (user_owns / 2) + (chall_owns / 10)
    return (numerator / OWNERSHIP_DENOMINATOR) * 100

def get_current_rank_by_percentage(percentage):
    if percentage == 100.0:
        return "Omniscient"
    sorted_ranks_desc = sorted(RANK_THRESHOLDS.items(), key=lambda item: item[1], reverse=True)

    for rank_name, threshold in sorted_ranks_desc:
        if rank_name == "Omniscient":
            continue
        if rank_name == "Noob":
            continue
        if percentage > threshold:
            return rank_name
    return "Noob"

def get_next_rank_details(current_rank_name):
    if current_rank_name == "Omniscient":
        return None, None

    for i, (name, threshold) in enumerate(RANK_ORDERED_LIST):
        if name == current_rank_name:
            if i + 1 < len(RANK_ORDERED_LIST):
                next_rank_name, next_rank_threshold = RANK_ORDERED_LIST[i+1]
                return next_rank_name, next_rank_threshold
            else:
                return None, None
    return None, None