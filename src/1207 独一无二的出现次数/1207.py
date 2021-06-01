class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for num in arr:
            dic[num] = dic.get(num, 0) + 1
        check = []
        for k,v in dic.items():
            if v not in check:
                check.append(v)
        return True