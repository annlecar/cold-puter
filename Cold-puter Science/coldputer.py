count = int(input())
if count < 1:
    print ("please input 1-100")
elif count > 100:
    print ("please input 1-100")
else:
    answer = 0
    temp = input().split()
    for number in temp:
       
        if int(number) >= 1000000 or int(number) <= -1000000:
            print ("please input temperature greater than -1 000 000 and less than 1 000 000")
        elif int(number) < 0:
            answer += 1
            
print (answer)
