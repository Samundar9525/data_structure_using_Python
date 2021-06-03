
def isAnBn(str):
    n = len(str)
    print(n)
    for i in range(n):
        if (str[i] != 'X'):
            break
    print(i)
    if ((i +1)*2 != n):
        return False
    for j in range(i, n-1):
        if (str[j] != 'Y'):
            return False
    print(j)
    return True
if __name__ == "__main__":
    str = "XXXYYYYYYYY"
    print("Yes") if isAnBn(str) else print("No")
