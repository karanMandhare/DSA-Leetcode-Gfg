class Solution(object):
    def reverseVowels(self, s):
        vowel=set("aeiouAEIOU")
        i=0
        j=len(s)-1
        chars=list(s)
        while i<j:
            if chars[i] not in vowel:
                i+=1
            elif chars[j] not in vowel:
                j-=1
            else:
                chars[i],chars[j]=chars[j],chars[i]
                i+=1
                j-=1
        result="".join(chars)
        return result


        