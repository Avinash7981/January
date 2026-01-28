# l=[4,5,6,2,9,4,5,6]
# #. 0,1,2,3,4,5,6,7
# #p=[4,9,15,17,26,30,35,41]
# quiries = [(0,4),(0,7),(1,7),(3,7)]
# n = len(l)
# prefix = [0]*n
# prefix[0]=l[0]
# for i in range(1,n):
#     prefix[i]=prefix[i-1]+l[i]
# for i,j in quiries:
#     if i == 0:
#         print(prefix[j])
#     else:
#         print(prefix[j]-prefix[i-1])        




#Palindrome


def palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
s="malayalam"
print(palindrome(s))    