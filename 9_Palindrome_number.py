def isPalindrome(x):
    #check if last digit is zero given the number is not 0.
    if (x !=0 and x%10 ==0)or x < 0:
            return 'false'
    
    else:
    # compare the two halves of the string 
        rev_half = 0
        while x > rev_half:
            rev_half = rev_half*10 + x%10
            x //= 10
        #     print("rev_half : {0} x = {1}".format(rev_half,x))
        # print('rev_half // 10 : ', rev_half//10)
        return x == rev_half or x == rev_half//10