stdata={'id':1,'name':'sanket','sub':'python'}
"""print(stdata)

print(stdata['sub'])
print(stdata.get('id'))

print(stdata.keys())
print(stdata.values())"""

# ----------------------------------- #
#print(stdata)

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

#print(len(stdata))

#stdata['id']=2
#print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""


# ----------------------------------- #
print(stdata)
#stdata['city']='rajkot'
#stdata.pop('name')
#del stdata['sub']
#stdata.clear()
#del stdata
#print(stdata)


newdict=stdata.copy()
print(newdict)