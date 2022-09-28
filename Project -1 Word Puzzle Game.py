import random

def shuffleWord(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)


def printPuzzleQuestion(word,score):
    problemwords=shuffleWord(word)
    print("\nArrange the letters to form a valid words:")
    print(problemwords)
    userword=input()
    print()
    if userword.upper()==word:
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1    

    return score


def main():
    score=0
    words=["FATHER","BREAK","COUNTRY","GREEN","AROPLAIN"]
    words=random.sample(words,k=len(words))

    for word in words:
        score=printPuzzleQuestion(word,score)

        print("Your Score is:",score)
main()        

#===========================================OUTPUT==============================================================
""" 
Arrange the letters to form a valid words:
NURCTOY
Country

Correct
Your Score is: 1

Arrange the letters to form a valid words:
GNREE
hfhjh

Wrong
Your Score is: 0

Arrange the letters to form a valid words:
FAHERT
Father

Correct
Your Score is: 1

Arrange the letters to form a valid words:
ALPNORAI
Aroplain

Correct
Your Score is: 2

Arrange the letters to form a valid words:
KBRAE
Break

Correct
Your Score is: 3
 """