from itertools import combinations
from itertools import combinations_with_replacement

def calculate_distribution(die_A, die_B):
    sum_distribution = {sum: 0 for sum in range(2, 13)}
    
    total_combinations = len(die_A) * len(die_B)

    for i in die_A:
        for j in die_B:
            sum_ab = i + j
            sum_distribution[sum_ab] += 1

    return sum_distribution


def undoom_dice(die_A, die_B):
    original_distribution = calculate_distribution(die_A, die_B)

    new_die_b_possible = list(combinations(range(2, 8), 4))
    new_die_a_possible = list(combinations_with_replacement(range(1, 5), 4))

    for combination_b in new_die_b_possible:
        new_die_b = list(combination_b)
        new_die_b.append(1)
        new_die_b.append(8)

        for combination_a in new_die_a_possible:
            new_die_a = list(combination_a)
            new_die_a.append(1)
            new_die_a.append(4)
            dist = calculate_distribution(new_die_a, new_die_b)

            if dist == original_distribution:
                    return new_die_a, new_die_b

    return "This didn't work this time"



original_die_A = [1, 2, 3, 4, 5, 6]
original_die_B = [1, 2, 3, 4, 5, 6]

new_die_A, new_die_B = undoom_dice(original_die_A, original_die_B)

print("New Die A: ", sorted(new_die_A))
print("New Die B: ", sorted(new_die_B))

print("\nOriginal Distribution:",calculate_distribution(original_die_A, original_die_B))
print("New Distribution:     ",calculate_distribution(new_die_A, new_die_B))