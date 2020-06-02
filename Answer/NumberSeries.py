# author Liby Joseph

user_input=int(input("enter an integer : "))
temp=user_input+1
for row in range(1,user_input*2):
    if row<=user_input:
        temp=temp-1
    else:
        temp=temp+1
    for col in range(user_input,0,-1):
        if col==temp:
            for rept in range(1,(temp*2)):
                print(temp," ",end='')
            if temp==user_input:
                break;
            else:
                for rept in range(temp+1,user_input+1):
                    print(rept," ",end='')
                break
        else:
            print(col," ",end='')
    print()
