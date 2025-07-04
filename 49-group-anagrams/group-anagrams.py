class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for word in strs:
            sorted_key = tuple(sorted(word))
            dict[sorted_key].append(word)
        return list(dict.values())