dict = ['i', 'love','samsung', 'sam', 'sung']
str = 'ilovesamsung'

# dict = [
#     "self", "th", "is", "famous", "Word",
#     "break", "b", "r", "e", "a", "k", "br",
#     "bre", "brea", "ak", "problem"
# ]

# # input String
# str = "Wordbreakproblem"

def fun(str,res):
    for i in range (len(str)+1):
        sub= str[0:i]
        if (sub in dict):
            fun(str[i:], res + sub + " ")
            if (i==len(str)):
                res+=sub
                print(res)
                return True

if __name__ == '__main__':
    fun(str," ")