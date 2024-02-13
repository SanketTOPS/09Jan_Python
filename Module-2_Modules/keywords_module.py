import keyword

x=keyword.kwlist
print(x)

n=1
for i in keyword.kwlist:
    print(f"{n}={i}")
    n+=1