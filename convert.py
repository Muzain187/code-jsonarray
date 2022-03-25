#convert code into json array
#str variable contains multi line input 
str = ""
while True:
    line = input()
    if(line):
        str += line +'\n'
    else:  
        break

#replace "  with \"
a = '''"'''      
b = '''\\"'''
 
str = str.replace(a, b)

# creating list of array splitted by \n
arr = str.split('\n')

for i in range(len(arr)):
    print('"',arr[i],'"',end="")    # " <code> "
    if i != len(arr)-1:
        print(',') #except last line every line end with ,

print()