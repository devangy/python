


# finding length of the largest substring without repeatig chars in a string without duplicate chars
#
#

# brute force solutinon

def leet3(s):

    result = 0

    # first start from 1st element and create a set for each element  
    for i in range(len(s)):
        #create set for every element in each iteration
        charSet = set()
        #start iterating on the elements to add to the set if duplicate found break
        for j in range(i,len(s)):
            if s[j] in charSet:
                break
            charSet.add(s[j])
            # calculate max in each iteration and update to result
            result = max(result, len(charSet))
    return result



s = "abcabcbb"


print(leet3(s))
