from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for alphabet in s:
                chars[ord(alphabet) - 97] += 1
            key = tuple(chars)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())

        