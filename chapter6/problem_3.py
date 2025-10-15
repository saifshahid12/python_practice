# A spam comment is defined as a text containing following keyy word .

p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message = input("enter your message:")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("this message is spam")

else:
    print("this message is not a spam")