class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in matrix:
            if target >= m[0]:
                first = 0
                last = len(m)-1
                while first <= last:
                    n = math.floor( (first+last)/2 )
                    print(n, m[n])

                    if target > m[n]:
                        first = n+1
                    elif target < m[n]:
                        last = n-1
                    else:
                        return True
        return False