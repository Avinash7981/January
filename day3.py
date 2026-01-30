def maxsubarraysum(l,k):
    maxsum = float("-inf")
    cursum=0
    for i in range (k):
        cursum += 0
    for i in range (k,len(l)):
        cursum = cursum+l[i]-l[i-k]
        maxsum=max(maxsum,cursum)
    return maxsum
l = [3,6,4,8,1,2,9,5,7]
k=3
print(maxsubarraysum(l,k))
