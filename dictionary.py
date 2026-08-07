dictionay={"name":["kolkar nisha","kolkarzareentaj"],"age":[22,45],"cgpa":[9.8,8.9],"email":("neeshakolkar@gmail.com""kolkarnisha416@gmail.com")}
dict={"k1":"v1","k2":"v2","k3":"v3"}
print(dict)
print(dict.keys())
print(dict.values())
dict.update({"k3":"gangeshpasala"})
print(dict)
#a=dict("k"=="algonex")
# a=dict(["n",20])
#b=dict([("n1","nisha"),("age",22)])
print(dict["k3"])
print(dict.get("k3"))
dict["k4"]="v4"
dict["k5"]="v5"
print(dict)
dict.update({"k6":"v6","k7":"v7"})
print(dict)
dict.popitem()
print(dict)
# dict.pop()
# dict.popitem("k6")
# print(dict)
del(dict["k1"])
print(dict)
# dict.remove("k2")
# print(dict)
dict.clear()
print(dict)
#traverse of dictionary
dict={"k1":"v1","k2":"v2","k3":"v3"}
for i in dict:
    print(i)
for i in dict.items():
    print(i)
# for i in dict:
#     print(dict(i))
for i in dict:
    print(i,dict[i])
for i in dict.values():
    print(i)
for i in dict.keys():
    print(i)
for i in dict.items():
    print(i,dict.values(),dict.keys())
for key,value in dict.items():
    print(key,value)
print("k5" in dict)
print("k5" not in dict)
dict2={"nisha":{
    "name":"mom",
    "relation":"zareentaj"
},"s2":{

"name":"daughter",
"relation":"nisha"
},"s3":{"helo":["s","g","h"]}
}
print(dict2)
print(dict2["nisha"]["name"])
employees=[
    {"id":1,"name":"ganesh"},{"id":2,"name":"rahul"}
]
print(employees[0]["name"])
# a={i:i*i for i in range(5)}
# print(i)
a={}
for i in range(5):
    a[i]=i*i
print(a)
a={}
for i in range(0,10,2):
    a[i]=i*i
print(a)

