data={}

key=['id','name','sub']

for i in range(len(key)):
    value=input(f"Enter a value for {key[i]}:")
    data[key[i]]=value

print(data)