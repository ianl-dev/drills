def applyPermutation(A, P):
    """
    Given an array A, apply P, a permutation array to change the positioning of the elements
    E.g.
    A = [a,b,c,d]
    P = [2,0,1,3]

    a -> goes to c
    c -> goes to a
    P = [1, 0, 2, 3]

    b -> a
    P = [0, 1, 2, 3]
    """
    for i in range(len(A)):
        while P[i] != i:
            # Swap the elements in A
            A[P[i]], A[i] = A[i], A[P[i]]
            # Swap the elements in P to show you have changed
            P[P[i]], P[i] = P[i], P[P[i]]
            # IMPORTANT TO have the array[permutation first]
    return A

# TEST
a,b,c,d = 'a', 'b', 'c', 'd'
A = [a,b,c,d]
P = [2,0,1,3]
print(applyPermutation(A, P))
