import time           # gives us python time function
seconds=int(input("enter seconds:"))
while seconds>0:
    print(seconds)
    time.sleep(1)        #waits for 1 seconds
    seconds-=2
print("TIME'S UP...")