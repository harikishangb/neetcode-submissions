class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num]  =1

        sorted_by_value = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_by_value.keys())[:k]