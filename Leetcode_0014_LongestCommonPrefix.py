#14 Longest Common Prefix
def longestCommonPrefix(self, strs: List[str]) -> str:
    res_str = ''
    strs.sort()
    for i in range (len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            break
        res_str += strs[0][i]
    return res_str
