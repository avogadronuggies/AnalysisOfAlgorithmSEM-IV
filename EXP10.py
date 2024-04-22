def prefix_function(P):
    m = len(P)
    π = [0] * m  
    π[0] = 0     
    i = 0        

    for j in range(1, m):
        while i > 0 and P[i] != P[j]:
            i = π[i - 1]  
        if P[i] == P[j]:
            i += 1  
        π[j] = i  

    return π

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    π = prefix_function(P)  
    i = 0                   

    print("Prefix table:")
    print("Index: ", list(range(m)))
    print("Value: ", π)

    print("\nMatching process:")
    for j in range(n):
        print("\nCurrent character in text:", T[j])
        print("Current state of pattern:", P[:i])

        while i > 0 and P[i] != T[j]:
            i = π[i - 1]  
            print(f"Mismatch occurred. Shifting pattern by {i}")

        if P[i] == T[j]:
            print("Character matched:", T[j])
            i += 1

        if i == m:
            print(f"\nPattern occurs with shift {j - m + 1}")
            i = π[i - 1]  

T = input("Enter the text: ")
P = input("Enter the pattern: ")

kmp_matcher(T, P)