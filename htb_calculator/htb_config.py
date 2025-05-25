TOTAL_ACTIVE_MACHINES = 20
TOTAL_ACTIVE_CHALLENGES = 166

RANK_THRESHOLDS = {
    "Noob": 0.0,
    "Script Kiddie": 5.0,
    "Hacker": 20.0,
    "Pro Hacker": 45.0,
    "Elite Hacker": 70.0,
    "Guru": 90.0,
    "Omniscient": 100.0
}

RANK_ORDERED_LIST = sorted(RANK_THRESHOLDS.items(), key=lambda item: item[1])

OWNERSHIP_DENOMINATOR = (TOTAL_ACTIVE_MACHINES + (TOTAL_ACTIVE_MACHINES / 2) + (TOTAL_ACTIVE_CHALLENGES / 10))