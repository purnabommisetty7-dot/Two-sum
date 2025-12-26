def twosum(nums,target):
    n=len(nums)
    d={}
    for i in range (n):
        diff=target-nums[i]
        if diff in d:
            return[d[diff],i]
        else:
            d[nums[i]]=i
nums=list(map(int,input().split()))
target =int(input())
print(twosum(nums,target))