def wordbreak(dict,str,res):
    for i in range(1,len(str)+1):
        prefix=str[0:i]
        if res+prefix+"" in pikt:
            return pikt[res+prefix+""]
        if prefix in dict:
            pikt[res+prefix]=wordbreak(dict,str[i:],res+prefix+" ")
            if i==len(str):
                res+=prefix
                print(res)
    return res


if __name__ == '__main__':
    #dict =  ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    #str ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    dict=["cat", "cats", "and", "sand", "dog" ]
    str="catsanddog"
    pikt={}
    print(wordbreak(dict,str," "))


    # ||
    # ||
    # ||
    # ||
    # ||
    # ||
    # ||
    # ||
    # VV
    #
    #
  #                                          ye optimised version tha but error aa raha hai

    #mp = {}
    #
    # def combine(prev,ne):
    #     for i in range (len(prev)):
    #         prev[i]=prev[i]+" "+ne
    #     return prev
    #
    # def wordbreak(str):
    #     if str in mp:
    #         return mp[str]
    #
    #     res=[]
    #
    #     if str in dict:
    #         res.append(str)
    #
    #     for i in range (1,len(str)):
    #         new=str[i:]
    #
    #         if new in dict:
    #             remain=str[:i]
    #
    #             prev=combine(wordbreak(remain),new)
    #
    #             for j in prev:
    #                 res.append(j)
    #     mp[str]=res
    #
    #     return res