from typing import (
   List,
)
Class Solution:
    def Permutation_index(self, A):
        result = 1
        factor = 1
        for i in range(len(A) - 1, -1, -1):
            rank = 0
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    rank += 1
            result += factor * rank
            factor *= len(A) - i
         return result
