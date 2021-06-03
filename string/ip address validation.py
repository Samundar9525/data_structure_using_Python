def isvalid(ip):
    for i in ip:
        if i.isdigit():
            if int(i)>=0 and int(i)<=255:
                pass
            else:
                return False
            # if len(i)>3:
            #     return False

            if int(i)>=0 and i[0]=='0' and len(i)>1:
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    ip="127.1.85.9"
    ip=ip.split('.')
    if len(ip)>4 :
        print(-1)
    else:
        if(isvalid(ip)):
            print("VALID IP ")
        else:
            print('invalid')