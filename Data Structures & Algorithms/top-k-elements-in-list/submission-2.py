class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        scorecard = {}

        for num in nums:
            if num in scorecard:
                scorecard[num] += 1

            else:
                scorecard[num] = 1

        boxes = [[]for i in range(len(nums)+1)]
        for num,count in scorecard.items():
            boxes[count].append(num)

        result = []
        for i in range(len(boxes)-1,0,-1):
            for num in boxes[i]:
                result.append(num)
                if len(result) == k:
                    return result
 