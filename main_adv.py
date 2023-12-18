#tuples
mytuple = ("Boki", 35, "Ljubljana")
print(mytuple)
name, age, city = mytuple #unpacking
print(name)
print(age)
print(city)

mytuple2 = (1,2,3,4,5,6)
i1, *i2,i3 = mytuple2
print(i1)
print(i2)
print(i3)
print("*"*30)
#dictionary

mydict = {"name": "Bokisups",
          "age": 35, 
          "city": "Ljubljana"}
print(mydict)

mydict2 = dict(name="Viktor", age=5, city="Ljubljana")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = "bokisups@xyz.com"
print(mydict)

for ke in mydict.values():
    print(ke)

mydict.update(mydict2)#update
print(mydict)

mydict3 = {3:9, 1:5, 2:43}

# value = mydict3[0] #error index- no 0 in my dict
value = mydict3[2]
print("to je",(value))

mytuple3 = (8,7)
mydict4 = {mytuple3: 15}
print(mydict4)
print("*"*30)
#SEts - dont duplicate items
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.remove(2)
print(myset)
print(myset.pop())# removes 1 from sets but returns it allso
#union

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print("u is",(u))

i = odds.intersection(primes)
print("i is",(i))

diff = odds.difference(primes)
print("diff is",(diff))
# diff from odds to primes thats why theres no 2
diff2 = odds.symmetric_difference(primes)
# here will be 2
print("diff2 is",(diff2))
print("subset odds - primes",(odds.issubset(primes)))
#issuperset()
#isdisjoint() = means no same numbers
# frozenset cant be modified

#  SRRINGS
my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)
new_string = ' '.join(my_list)
print(new_string)

var = "Boki"
var2 = "Kuzma"
my_string2 = "Your name is %s"% var # prvi %s means place for variable and other %variable
print(my_string2)
my_string2 = "Your age is %d"# %d is for number %f fro float %.2f for 2 decimal
mystring4 = "Your name is {}".format(var,var2)
