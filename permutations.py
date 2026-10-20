# Given an array of A of n elements and a permutation of P, apply P to A

def apply_permutation(perm, A):
     n = len(perm)
     for i in range(n):
         next = i
         while perm[next] >= 0:
             A[i], A[perm[next]] = A[perm[next]], A[i]
             temp = perm[next]
             perm[next] -= n
             next = temp
     # Restore perm — runs ONCE, after every index has been processed
     perm[:] = [a + n for a in perm]
     for i in range(len(A)):
         next = i
         while perm[next] >= 0:
             A[i],A[perm[next]] = A[perm[next]], A[i]
             temp = perm[next]
             perm[next] -= len(perm)
             next = temp
            # Restore perm.
        perm[:] = [a + len(perm) for a in perm]
