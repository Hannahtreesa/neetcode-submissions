class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''res=set()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet=tuple(sorted([nums[i], nums[j], nums[k]]))
             
                        res.add(triplet)
        return [list(t) for t in res] '''

        nums.sort()
        res= set()
        for i in range(0, len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left= i+1
            right= len(nums)-1
            while left<right:
                total= nums[i]+ nums[left] +nums[right]
                
                if total==0:
                    res.add(tuple([nums[i], nums[left], nums[right]]))
                    left +=1
                    right-=1

                elif total<0:
                    left +=1
                else: 
                    right -=1
        return [list(t) for t in res]

        