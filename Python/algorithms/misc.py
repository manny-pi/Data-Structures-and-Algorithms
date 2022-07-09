
def rotate(A, n=1):
    """ Returns a copy of A, with its elements shifted n units to the right"""
    A = list(A)

    while n > 0:
        a = A[0]
        i = 0
        while i < len(A):
            t = A[(i + 1) % len(A)]
            A[(i + 1) % len(A)] = a
            a = t

            i += 1

        n -= 1

    return A


def reverse(A):
    B = []
    i = len(A) - 1
    while i >= 0:
        B.append(A[i])
        i -= 1

    return B


def swapElements(A, i, j):
    A = list(A)
    if i == j:
        return A
    else:
        t = A[i]
        A[i] = A[j]
        A[j] = t

    return A


def permutations(A):
    P = []              # Array to store configurations
    n = len(A) - 1      # Store the index of the last element
    R = list(A)

    i = 0
    while i <= n:
        P.append(R)     # Store configuration
        j = 0
        T = []
        while j <= n:

            # Swap trailing elements
            if j == 0:
                T = swapElements(R, n, n - 1)
                P.append(T)

            # Rotate array
            else:
                T = rotate(T)
                P.append(T)

            j += 1

        R = (rotate(R))  # Shift array one unit right
        i += 1

    R = reverse(R)
    P.append(R)

    j = 0
    while j < n:
        T = rotate(T)
        P.append(T)

        j += 1

    return P


# Execute permutation algorithm
ls = ['A', 'B', 'C', 'D', 'E']
result = permutations(ls)
for l in range(0, len(result)):
    print(l+1, ": ", result[l])

