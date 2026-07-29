class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            delimiter_index=s.find("#",i)
            length=int(s[i:delimiter_index])
            start=delimiter_index+1
            end=start+length
            result.append(s[start:end])
            i=end
        return result


