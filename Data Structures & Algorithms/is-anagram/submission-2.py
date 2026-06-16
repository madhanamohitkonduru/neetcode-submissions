class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1= {}
        hash2={}
        len_s = len(s)
        len_t = len(t)
        if len_s!=len_t:
            return False

        for i in range(min(len_s, len_t)):
            hash1[s[i]] = hash1.get(s[i], 0) + 1
            hash2[t[i]] = hash2.get(t[i], 0) + 1

        if hash1==hash2:
            return True
        else:
            return False        