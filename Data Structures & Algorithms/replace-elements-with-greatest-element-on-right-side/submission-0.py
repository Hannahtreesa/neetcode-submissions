class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num=arr[-1]
        ans=[0]*len(arr)
        ans[len(arr)-1]= -1
        for i in range(len(arr)-2,-1,-1):
            ans[i]=max_num
            max_num= max(max_num, arr[i])
        return ans
        