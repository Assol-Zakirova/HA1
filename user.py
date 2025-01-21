d={}
a=['What is the users name?','What is the users age?','What is the users country of birth?','What is the users known for?']
for i in range(4):
    print(a[i])
    b=input()
    d[a[i]]=b
for key,value in d.items():
    print(key,value)
