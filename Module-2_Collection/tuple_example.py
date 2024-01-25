data=('rajkot','baroda','ahmedabad','surat','jamnagar')
"""print(data)

print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:3])

print(len(data))"""


"""if 'baroda' in data:
    print("Yes...")
else:
    print("Noo")"""


"""for i in data:
    print(i)"""

print(data.index('surat'))

for i in data:
    print(f'{data.index(i)} = {i}')


del data
print(data)