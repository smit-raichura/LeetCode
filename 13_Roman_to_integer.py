def lcp(strs):
    prefix = ''
    for i in range(len(strs[0])):
        for s in strs:
            print('string : {0}     index : {1}     cahrAt : {2}'.format(s, i, s[i]))
            if i == len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix 
    