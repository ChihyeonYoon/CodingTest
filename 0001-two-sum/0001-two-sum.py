class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    answer.append(i)
                    answer.append(j)
                    return answer
 