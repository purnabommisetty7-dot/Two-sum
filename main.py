def find_unique(arr):
    d={}
    for i in range(len(arr)):
        if arr[i]in d:
            d[arr[i]]+=1 
        else:
            d[arr[i]]=1 
    for key,value in d.items():
        if value==1:
            return key
       
arr=list(map(int,input().split()))
print(find_unique(arr))
            
    