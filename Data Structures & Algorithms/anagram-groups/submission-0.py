class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)
        for str in strs:
            groupMap[tuple(sorted(str))].append(str)

        return list(groupMap.values())