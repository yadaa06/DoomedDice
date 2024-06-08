def total_combinations(die_A, die_B):
    #Calculates total number of combinations are possible
    #For a 6 sided die it is just 6 * 6 but I am representing it by iterating through every combination
    sum = 0
    for i in die_A:
        for j in die_B:
            sum += 1

    print(f"The total number of combinations: {sum}\n")
    return sum

def distribution(die_A, die_B):
    distribution = {sum_value: 0 for sum_value in range(2, 13)}

    for i in die_A:
        for j in die_B:
            sum_ab = i + j
            distribution[sum_ab] += 1
    
    for sum_value, frequency in sorted(distribution.items()):
        print(f"Sum: {sum_value}, Frequency: {frequency}")
    print()

    return distribution
    
def probability(distribution, combinations):
    for sum_value, frequency in sorted(distribution.items()):
        probability = frequency / combinations
        print(f"P(Sum = {sum_value}) = {probability:.4f}")
    print()


A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 6]

comb = total_combinations(A, B)
dist = distribution(A, B)
probability(dist, comb)