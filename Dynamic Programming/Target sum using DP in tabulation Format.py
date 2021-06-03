class Solution(object):
    def findTargetSumWays(self, arr, S):
        if len(arr) > 20 or S > 1000:
            return 0

        n = len(arr)

        def add(a):
            temp = 0
            for i in range(len(a)):
                temp = temp + a[i]
            return temp

        def subset(arr, summ, n, t):
            for i in range(1, summ + 1):
                t[0][i] = 0
            for i in range(n + 1):
                t[i][0] = 1

            for i in range(1, n + 1):
                for j in range(summ + 1):
                    if arr[i - 1] > j:
                        t[i][j] = t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            return t[n][summ]

        su = add(arr)
        new_sum = (S + su) // 2
        t = [[0 for i in range(new_sum + 1)] for j in range(n + 1)]
        te = subset(arr, new_sum, n, t)
        if n == 1:
            if arr[0] == S or arr[0] == -S:
                return 1
            else:
                return 0
        else:
            return te

if __name__ == '__main__':
    arr=[1,1,2,3]
    sum=1
    obj=Solution()
    s=obj.findTargetSumWays(arr, sum)
    print(s)
