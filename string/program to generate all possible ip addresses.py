#note ye logic tabhi kaam karega jab mere ko kam se sam   8 no ka ip address diya ho kyunki ye dynamicaly work nahi
#kar raha hai iske liye hard code karna padega

def isvalid(ip):
    for i in ip:
        if i.isdigit():
            if int(i)>=0 and int(i)<=255:
                pass
            else:
                return False
            if len(i)>3:
                return False

            if i[0]=='0' and len(i)>1:
                return False
        else:
            return False
    return True
if __name__ == '__main__':
    str="19216818192"
    n=len(str)

    ans=[]
    A="";B="";C="";D=""
    for i in range(1,n):
        A=str[:i]
        for j in range(i,i+4):
            B=str[i:j]
            for k in range(j,j+4):
                C=str[j:k]
                for l in range (k,k+4):
                    D=str[k:n]
                    te=A+"."+B+"."+C+"."+D
                    uip=te
                    te=te.split(".")
                    # print(te)
                    if (isvalid(te)):
                        if uip not in ans:
                            ans.append(uip)
                    else:
                            break
    if len(ans)==0:
        print("No such ip comination exit karta hai")
    else:
        print("ee ba tohar ip :- \n",ans)


