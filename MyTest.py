import time

score = 0

name = str(input("What's your name? "))
print("Welcome, " + name + " to the test")

def scorePlus():
    global score
    score += 1
    print("Your score: ", score)

def scoreMinus():
    global score
    score -= 1
    print("Your score: ", score)

def q1():
    global score
    print("\n1. What is El Capitan?")
    time.sleep(0.5)
    print("a) An operating system for Windows")
    print("b) An operating system for Mac")
    print("c) A third-party application\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("Well done, that's correct!")
        scorePlus()
    else:
        print("Sorry, that was a wrong answer!")
        scoreMinus()

    q2()


def q2():
    global score
    print("\n2. What is Apple's latest device?")
    time.sleep(0.5)
    print("a) iPhone")
    print("b) MacBook Pro")
    print("c) iPod Touch\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("Well done, that's correct!")
        scorePlus()
    else:
        print("Sorry, that was a wrong answer!")
        scoreMinus()

    q3()

def q3():
    global score
    print("\n3. What is Samsung's latest device?")
    time.sleep(0.5)
    print("a) Galaxy Fold")
    print("b) Galaxy S10")
    print("c) Galaxy Tab\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("Well done, that's correct!")
        scorePlus()
    else:
        print("Sorry, that was a wrong answer!")
        scoreMinus()

q1()