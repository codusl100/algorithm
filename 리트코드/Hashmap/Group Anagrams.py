class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for word in strs:
            key = "".join(sorted(word)) # 정렬로 비교적 비교 빠르게
            
            if key not in anagram_groups:
                anagram_groups[key] = [word]
            else:
                anagram_groups[key].append(word)
        
        return anagram_groups.values()