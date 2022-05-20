import random

#Variable Declaration
name = input("what's your name: ")
question = input("What's your question? : ")
answer = ""

#Random Number
rnumber = random.randint(1,10)

#Loop Answer
if rnumber == 1 :
  answer = "Yes - definitely"
elif rnumber == 2:
  answer = "It is decidedly so."
elif rnumber == 3:
  answer = "Without a doubt."
elif rnumber == 4:
  answer = "Reply hazy, try again."
elif rnumber == 5:
  answer = "Ask again later."
elif rnumber == 6 :
  answer = "Better not tell you now."
elif rnumber == 7:
  answer = "It is decidedly so."
elif rnumber == 8:
  answer = "Outlook not so good."
elif rnumber == 9:
  answer = "Very doubtful."
elif rnumber == 10:
  answer = "Signs point to yes"

else:
  print("Error")

#Output
if len(question) == 0:
  print("Wait, what's the question? ")
else:
  if len(name) == 0:
    print("The Question : ",question)
    print("Magic 8-Ball's answer: ",answer)
  else:
    print(name,"asks : ",question)
    print("Magic 8-Ball's answer: ",answer)
