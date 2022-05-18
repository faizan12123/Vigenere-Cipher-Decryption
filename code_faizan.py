stringToDecode = 'Ffowc abiyfsbiq fkh ffbic mnh ofkvyorovgersgq. Dlcup lyup aye ergrmbqjk mypxw elp cxmbnoh mr xfq xiaw. Xfqgb cmpc uqpo pqkkvimzvc fgxc. Rrigd wssffc uqpo qyyvp, usxf zbmetr vcp, xful pgbq.'
keyword = 'mykey'

#looping the key in accordance to the amount of characters in the stringToDecode
def cycleKey(stringToDecode, keyword):
    keyword = list(keyword)
    if len(stringToDecode) == len(keyword):
        return(keyword)
    else:
        for i in range(len(stringToDecode) -
                       len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return("" . join(keyword))


keyword = cycleKey(stringToDecode,keyword)
originalMessage = ""


for i in range(len(stringToDecode)):

    stringToDecodeIndex = ord(stringToDecode[i])
    keywordIndex = ord(keyword[i]) - ord('a')
    
    #upper A and Z
    if (stringToDecodeIndex >= ord('A') and stringToDecodeIndex <= ord('Z')):
        stringToDecodeIndex -= ord('A')
        cipher = (stringToDecodeIndex - keywordIndex + 26) % 26
        cipher += ord('A')
        originalMessage += chr(int(cipher))

    #lower a and z
    elif (stringToDecodeIndex >= ord('a') and stringToDecodeIndex <= ord('z')):
        stringToDecodeIndex -= ord('a')
        cipher = (stringToDecodeIndex - keywordIndex + 26) % 26
        cipher += ord('a')
        originalMessage += chr(int(cipher))

    else:
        originalMessage += chr(int(stringToDecodeIndex))

print('Decrypted Message: ', originalMessage)


