class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = Counter(s1)
        dic = {}
        l=0

        for i in range(len(s2)):
            if s2[i] not in s1_dic:
                dic = {}
                l+=1
                continue
            else:
                dic[s2[i]] = dic.get(s2[i],0)+1
                while dic[s2[i]] > s1_dic[s2[i]]:
                    if s2[l] in dic: 
                        dic[s2[l]]-=1
                    l+=1

                if dic == s1_dic: return True
        
        return False
        


            



        