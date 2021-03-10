from Op1 import GetMessage
from Op2 import AuthorMessage
from Op3 import DomainMessage
from Op4 import MaxDomain
from Op5 import AuthorInformation
from Op6 import MaxDay
from Op7 import MaxMonth
from Op8 import MaxHour
from Op9 import AverageXDC
from Op10 import AverageNewR
from Op11 import Modified

Enter = int(input("Enter Your Number Question [1-11]: "))

while (Enter > 0 ):

    if Enter == 1:
        print(GetMessage())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 2:
        print(AuthorMessage())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 3:
        print(DomainMessage())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 4:
        print(MaxDomain())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 5:
        print(AuthorInformation())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 6:
        print(MaxDay())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 7:
        print(MaxMonth())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 8:
        print(MaxHour())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 9:
        print(AverageXDC())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 10:
        print(AverageNewR())
        Enter = int(input("Enter Your Number Question [1-11]: "))
    elif Enter == 11:
        print(Modified())
        break
    else:
        print("The number is not correct, please run again!")
        break

