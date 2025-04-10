x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

a=("apple","lemon","goa")
b=("chreey","onion","chill")
c=a+b
print(c)

a=(1,2,2,3,3,4,5,6,7,8,)
print(a.count(2))
print(len(a))

dict={"apple":"red","chill":"green","lemon":"yellow"}
print(type(dict))
print(len(dict))
x=dict["apple"]
x=dict.get("apple")
print(x)
b=dict.keys()
c=dict.values()
print(b)
print(c)
x=dict.keys()
dict['ginger']="brown"
print(x)
d=dict.items()
print(d)
a=dict['lemon']='light yellow'
print(a)
a=dict.update({'chill':'light green'})
print(a)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

a={"car":2,"auto":3,"bus":6}
a.update({"bike":4})
print(a)
a.clear()
print(a)

a={"car":2,"auto":3,"bus":6}
b=a.copy()
print(b)

