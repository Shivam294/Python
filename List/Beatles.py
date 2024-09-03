beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    beatles.append(input())

del beatles[3]
#del beatles[4]

beatles.insert(0, 'Ringo Starr')

print("The Fab ", len(beatles))
print(beatles)