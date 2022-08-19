
exam = [
    {
        "id": "1",
        "question": "\nwhich is the highest point on earth ?",
        "A": "A) Caucasus Mountains",
        "B": "B) Mariana",
        "C": "C) Everest Mount\n",
        "Answer": "C"
    },
    {
        "id": "2",
        "question": "\nwhich is the biggest lake on earth ?",
        "A": "A) Tanganyika",
        "B": "B) Caspian Sea",
        "C": "C) Vostok\n",
        "Answer": "B"
    },
    {
        "id": "3",
        "question": "\nwhich is the deepest lake on earth ?",
        "A": "A) Baikal",
        "B": "B) Tanganyika",
        "C": "C) Caspian Sea\n",
        "Answer": "A"
    },
    {
        "id": "4",
        "question": "\nwhich islands has the biggest area ?",
        "A": "A) Greenland",
        "B": "B) New Guinea",
        "C": "C) Madagascar\n",
        "Answer": "A"
    },
    {
        "id": "5",
        "question": "\nWhich country has least population on the world ?",
        "A": "A) Samosir",
        "B": "B) Pitcairn Islands",
        "C": "C) Vatican City\n",
        "Answer": "B"
    },
    {
        "id": "6",
        "question": "\nHow many people live in Pitcairn Islands ?",
        "A": "A) 345 people",
        "B": "B) 230 people",
        "C": "C) 40 people\n",
        "Answer": "C"
    }
]
counter = 0
wrong = 0
correct = 0
answers = []
for i in exam:
    print(i["question"], i["A"], i["B"], i["C"], sep="\n")
    while True:
        ans = input("Your Answer: ")
        if not ans.isalpha() or len(ans) < 1 or not ans in ["a", "b", "c"]:
            print("You can choose only A, B and C")
        else:
            break
    ans = ans.capitalize()

    if ans == i["Answer"]:
        answers.append(ans)
        correct += 1
    else:
        answers.append(ans)
        wrong += 1
    counter += 1

print("-"*30,"\nTotall Correct Answers: ", correct,"\nTotall Wrong Answers: ", wrong,"\n","-"*30,sep="")

while True:
    inp = input("\nPress 'Y' to see correct answers,\nPress 'Q' to exit... :")
    if inp == "y":
        for i in exam:
            print((i["question"]),"\n", i["A"],"\n", i["B"],"\n", i["C"],"\n","-"*30,"\n","Your Answer is:",
                  (answers[counter-1]),"\n", "Correct Answer is:", (i["Answer"]),"\n","-"*30)
        break
    elif inp == "q":
        break
