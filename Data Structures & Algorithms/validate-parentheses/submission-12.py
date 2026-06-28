class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        if len(s)==1:
            return False
        lis = []
        for i in s:
            if i in hashmap.keys():
                if not lis or lis.pop() != hashmap[i]:
                    return False
                # if lis.pop() != hashmap[i]:
                #     return False
            else:
                lis.append(i)


        return True if not lis else False