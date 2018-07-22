fileName = "/sdcard/qpython/myScripts/crashText.txt"
num = input("Enter number to repeat ")
separator = input("Enter separator")
n = input("Enter number of times to print ")

file = open(fileName, "w")
for i in range(0, n, 1):
    file.write(num, separator)
file. close()