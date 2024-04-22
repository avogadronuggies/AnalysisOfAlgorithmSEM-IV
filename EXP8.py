def sum_of_subsets(s, k, r, target_sum, weights, solution):
    # Print the current subset being considered
    print("Current subset:", solution)
   
    # Check if the current sum equals the target sum
    if s == target_sum:
        # If yes, print the solution subset in fixed tuple format
        print("Solution found:", solution_to_fixed_tuple(solution, weights))
   
    # If the current sum is less than the target sum and there are more elements to consider
    elif k < len(weights) and s + weights[k] <= target_sum:
        # Explore the left child: include the current element in the subset
        sum_of_subsets(s + weights[k], k + 1, r - weights[k], target_sum, weights, solution + [weights[k]])
   
    # If the current sum plus the remaining elements' weights is greater than or equal to the target sum,
    # and there are more elements to consider
    if k < len(weights) and s + r - weights[k] >= target_sum and k + 1 < len(weights) and s + weights[k + 1] <= target_sum:
        # Explore the right child: exclude the current element from the subset
        sum_of_subsets(s, k + 1, r - weights[k], target_sum, weights, solution)


def solution_to_fixed_tuple(solution, weights):
    fixed_tuple = []
    for weight in weights:
        if weight in solution:
            fixed_tuple.append(1)
        else:
            fixed_tuple.append(0)
    return tuple(fixed_tuple)

def main():
    n = int(input("Enter the number of elements: "))
    weights = []
    for i in range(n):
        weight = int(input("Enter weight {}: ".format(i + 1)))
        weights.append(weight)
    target_sum = int(input("Enter the target sum: "))

    total_sum = sum(weights)
    solution = []
   
    print("\nStep by step iteration:")
    sum_of_subsets(0, 0, total_sum, target_sum, weights, solution)

if __name__ == "__main__":
    main()
