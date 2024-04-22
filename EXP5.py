def knapSack(W, wt, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    # Print the full calculation table
    print("Calculation Table:")
    for row in table:
        print(row)

    # Backtrace to find the selected items
    selected_items = []
    i, j = n, W
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            selected_items.append(i - 1)
            j -= wt[i - 1]
        i -= 1

    print("\nSelected Items:")
    for item in selected_items[::-1]:
        print(f"Weight: {wt[item]}, Value: {val[item]}")

    return table[n][W]

print('Enter the profits:')
values = list(map(int, input().split(' ')))
print('Enter the weights:')
weights = list(map(int, input().split(' ')))
C = int(input('Enter the maximum capacity:'))
n = len(weights)
print("\nMaximum Value:", knapSack(C, weights, values))