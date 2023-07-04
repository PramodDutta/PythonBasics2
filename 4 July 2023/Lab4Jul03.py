# File IO in Python


# # Append
# file2 = open('pramod2.txt','a')
# file2.write("Yes Yes, Append New Data")
# file2.close()
#
# # Write
# file2 = open('pramod3.txt','w')
# file2.write("Yes Yes, Override")
# file2.close()

try:
    file = open('pramod.txt', 'r')
    print(file.read())
except FileNotFoundError as vishal:
    print("File Not Found!", vishal)
finally:
    if file:
        file.close()
