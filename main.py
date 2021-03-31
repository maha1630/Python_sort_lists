print("Hello world")
#integers
b=[5,4,3,2,2,10,12,13,13]
b.sort() 
print(b)
#In reverse order
b.sort(reverse=True)
print(b)
#strings
c=["maha","food","water","mlh","I love pizza"]
c.sort()
print(c)
#In reverse order
c.sort(reverse=True)
print(c)
#sort by length 
d = ["aaa", "bb", "c"]
d.sort(key=len)
print(d)
#sorting as if all are in lower case, whereby same name the capital letter comes first (lexicographical)
e = ["Emma", "emily", "Amy", "harry","Maha","Bob","Wilder","Oscar","oscar","Jason"]
e.sort(key=str.lower)
print(e)
#a function to sort a list of cilents by age 
class Client:
	def __init__(self, age):
		self.age = age
client1 = Client(67)
client2 = Client(23)
client3 = Client(13)
client4 = Client(35)
#put them in a list 
clients=[client1,client2,client3,client4]
#extract age
def get_age(client):
	return client.age
#Sort by age and print the results
clients.sort(key=get_age)
for client in clients:
	print(client.age)
#sort without causing any change to the list 
# sorted() returns a new sorted copy of the original list
nums = [6.5, 2.4, 7.3, 3.5, 2.6, 7.4]
val = sorted(nums)
print(val)



