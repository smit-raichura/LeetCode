def romanToInt(s: str) -> int:
    int_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res = 0
    for i in range(0,len(s)):
        if i == len(s)-1:
            res += int_map[s[i]]
        else: 
            if int_map[s[i]] < int_map[s[i+1]]:
                res -= int_map[s[i]]
                i+=2
            else:
                res += int_map[s[i]]
    return res
