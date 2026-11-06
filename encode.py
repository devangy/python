

# encode encode
#
#


strs = ["Hello","World"]



def encode(strs: List[str]) -> str:

    # storing sizes of each string in sizes
    #final string in res

    sizes,res = [],[]

    for s in strs:
        sizes.append(len(s))

    # appending into final res array with size and size converted into string with # to mark the end of sizes
    # finally append the actual strings using extend to flatten instead of nested
    for sz in sizes:
        res.append(str(sz))
        res.append(',')
    res.append('#')
    res.extend(strs) # exten method takes iterable and flattens them without nesting the elements
    
    # finally return the res array as string with no space now we have the sizes
    # we have the # as delimiter after that we append the strings
    return ''.join(res) # return res array with no space between them


def decode(str: str):

    sizes = []
    for char in str:
        if char == ",":
            continue
        if char == "#":
            break
        sizes.append(int(char))


    strings = []

    i = str.index("#") + 1
    
    for sz in sizes:
        word = str[i : i + sz]
        strings.append(word)
        i += sz
    return strings
    








encoded_str = encode(strs)
print(decode(encoded_str))
