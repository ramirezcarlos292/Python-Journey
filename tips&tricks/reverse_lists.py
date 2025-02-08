# iterate a list in reverse
mylist = [1,2,3,4]

for i in range(len(mylist)-1, -1, -1):
	print(mylist[i]) # prints 4,3,2,1
	
# reverse a list
mylist_reverse = mylist[::-1]
print(mylist_reverse)

mylist = [1,2,3,4]
mylist_reverse = list(reversed(mylist))
print(mylist_reverse)