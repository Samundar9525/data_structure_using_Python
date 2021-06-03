class Solution:
    def minDiffernce(self, arr, n):

        def add(arr):
            # ya phir direct inbuit sum fun ka use kar sakte ho
            temp = 0
            for i in range(n):
                temp = temp + arr[i]
            return temp

        def subset(arr, sum, n, t):
            for i in range(1, (rng + 1)):
                t[0][i] = False
            for j in range(n + 1):
                t[j][0] = True
            for i in range(1,n + 1):
                for j in range(sum + 1):
                    if (arr[i - 1] > j):
                        t[i][j] = t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]

        rng = add(arr)
        t = [[False for i in range(rng + 1)] for j in range(n + 1)]
        subset(arr, rng, n, t)

        if n == 1:
            m = arr[0]
        else:
            m = 9999999

        for i in range(1, rng // 2 + 1):
            if t[n][i] == True:
                m = min(m, rng - (2 * i))
        return m

if __name__ == '__main__':
    arr = [1,6,11,5]
    N=len(arr)
    ob = Solution()
    ans = ob.minDiffernce(arr, N)
    print(ans)

