from itertools import combinations
from itertools import combinations_with_replacement

def calculate_distribution(die_A, die_B):
    #Creates a dictionary with all possible sums of the dice
    sum_distribution = {sum: 0 for sum in range(2, 13)}

    #Populates the dictionary by iterating through all the combinations
    for i in die_A:
        for j in die_B:
            sum_ab = i + j
            sum_distribution[sum_ab] += 1

    return sum_distribution


def undoom_dice(die_A, die_B):
    #Original distribution of the two 6 sided die
    original_distribution = calculate_distribution(die_A, die_B)

    #List that holds all the possible combinationsn of 4 numbers between 2 and 7(inclusive) with no repeats
    new_die_b_possible = list(combinations(range(2, 8), 4))

    #List that holds all the possible combinations of 4 numbers between 1 and 4(inclusive) with repeats
    new_die_a_possible = list(combinations_with_replacement(range(1, 5), 4))

    #Exhaustive search
    for combination_b in new_die_b_possible:
        new_die_b = list(combination_b)
        new_die_b.append(1)
        new_die_b.append(8)

        for combination_a in new_die_a_possible:
            new_die_a = list(combination_a)
            new_die_a.append(1)
            new_die_a.append(4)
            dist = calculate_distribution(new_die_a, new_die_b)

            #If the distribution of this combination of die matches the original distribution, it will return these two die
            if dist == original_distribution:
                    return new_die_a, new_die_b

    return "The program couldn't find a die"



original_die_A = [1, 2, 3, 4, 5, 6]
original_die_B = [1, 2, 3, 4, 5, 6]

new_die_A, new_die_B = undoom_dice(original_die_A, original_die_B)

print("New Die A: ", sorted(new_die_A))
print("New Die B: ", sorted(new_die_B))

print("\nOriginal die distribution:",calculate_distribution(original_die_A, original_die_B))
print("New die distribution:     ",calculate_distribution(new_die_A, new_die_B))