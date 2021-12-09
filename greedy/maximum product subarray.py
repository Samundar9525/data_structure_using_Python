def sol(arr):
     neg=0
     flag=0
     largneg=-999999999
     for i in arr:
         if i<0:
             largneg=max(largneg,i)
             neg+=1
         if i==0:
             flag=1
     res=1
     if (neg==0):# koi negative aur zero nahi hai
         for i in arr:
             if i==0:
                 continue
             res*=i
         return res

     elif(neg%2==0 ):#even no of negative hai aur zero bhi hai
         for i in arr:
             if i==0:
                 continue
             res*=i
         return res

     else:                                  # it means odd no of negative and it handle both zero element too
         arr.remove(largneg)
         for i in arr:
             if i==0:
                 continue
             res*=i
         return res


if __name__ == '__main__':
    arr=[-1, -1, -2, 4, 3 ,0,0,-3]
    # arr=[-1, -5, -2]
    # arr=[1,2,3,4,5,6]
    print(sol(arr))