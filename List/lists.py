countries = ["USA", "Canada", [1,2,3], "India"]
print(countries)
count=int(0)
print("\n",countries[2])
countries[2]="Russia"
print("\n",countries)
print("\n",countries[::-1])
print("\n",countries[2:2:2])
print("\n",countries[::2])
print("\n",countries[:2:])
print("\n",countries[2::])
print("\n", countries.sort())
for x in [0, 1, 1, 3]:
    for y in [0, 2, 1, 2]:
            print('*')
            count+=1
print("\n",count)