def hash(siteName):
    firstDot = siteName.find(".")
    if firstDot != -1:
        siteName = siteName[firstDot + 1 :]
    secondDot = siteName.find(".")
    if secondDot != -1:
        siteName = siteName[:secondDot]
    siteName = siteName.upper()
    value = 0
    for i in range(len(siteName)):
        value = value + ord(siteName[i])
    return value


siteName = input("Enter a site name to hash: ")
hashingFunction = hash(siteName)
print(hashingFunction)
