s1 = input("please enter the string" )


if len(s1)<2:
    print("empty")
else:
    print(s1[0]+s1[1]+s1[len(s1)-2]+s1[len(s1)-1])

