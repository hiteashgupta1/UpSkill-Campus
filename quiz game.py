print("Welcome to Computer Quiz")

playing = input("Do you want to play?")

if(playing!="yes"):
    quit()

print("Okay! Let's Play")

with open('questions.txt' , 'r') as quesfile, open('answers.txt','r') as ansfile:
    questions = [question.strip() for question in quesfile.readlines()]
    answers = [answer.strip() for answer in ansfile.readlines()]

    score = 0

    for question , answer in zip(questions,answers):
        user_ans = input(question+"? ")
        if user_ans.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect")


    print("Thanks for Playing!")
    print(f"Final Score: {score} / {len(questions)}".center(100))