def solution(s):
    if s == "":
        return []
    return [s[i:i+2]+'_' if len(s[i:i+2])==1 else s[i:i+2] for i in range(0, len(s), 2)]
