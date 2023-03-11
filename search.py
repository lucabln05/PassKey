#Simple search program
list = ["Windows 10", "Windows 8", "Windows 7", "Windows Vista", "Windows XP", "Windows ME", "Windows 2000", "Linux", "Debin", "Mint", "Android", "IOS"]

input = input("Object: ")

for i in list:
    if input == i[0:len(input)]:
        print(i)
