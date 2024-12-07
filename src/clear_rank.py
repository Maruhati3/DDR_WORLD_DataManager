from enum import IntEnum

class ranks(IntEnum):
    D = 0
    D_plus = 550000
    C_minus = 590000
    C = 600000
    C_plus = 650000
    B_minus = 690000
    B = 700000
    B_plus = 750000
    A_minus = 790000
    A = 800000
    A_plus = 850000
    AA_minus = 890000
    AA = 900000
    AA_plus = 950000
    AAA = 990000

rank_name = ["D", "D_plus", "C_minus", "C", "C_plus", "B_minus", "B", "B_plus", "A_minus", "A", "A_plus", "AA_minus", "AA", "AA_plus", "AAA"]


def clear_rank(score):
    for i, rank in enumerate(ranks):
        print(f"{i}: {rank}\n")
        if rank <= score:
            return rank_name[len(rank_name) - i]