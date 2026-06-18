class Solution:
    hashmap= {}

    def encode(self, strs: List[str]) -> str:
        main_lis = []
        string=""
        for i in strs:
            for j in i:
                ascii = str(ord(j))
                self.hashmap[ascii] = j
                string = string+ascii+"_"
            string = string+ "+"
        return string
                

    def decode(self, s: str) -> List[str]:
        lis = []
        word = ""
        start = 0
        for i in range(len(s)):
            if s[i]=="_":
                letter = s[start:i]
                word = word + self.hashmap[letter]
                start=i+1
            elif s[i] == "+":
                lis.append(word)
                word= ""
                start = i+1
            
        return lis