class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        gram_map={}


        for s in strs:
            print(s)
            new=''.join(sorted(s))
            print(new)

            if new in gram_map:

                gram_map[new].append(s)
            else:

                gram_map[new]=[]
                gram_map[new].append(s)

        result=[value for key ,value in gram_map.items()]
        return result