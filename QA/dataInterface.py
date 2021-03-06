import sqlite3 as lite
import sys

import re, math
from collections import Counter

WORD = re.compile(r'\w+')
questions = []
questionsVect = []
answers = []

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def gatherData():
    import os
    dir = os.path.dirname(__file__)
    print(__file__)
    print(dir)
    filename = os.path.join(dir, 'SQLiteStudio','techCrunch2016DB')

    print(filename)
    con = lite.connect(filename)

    with con:    
        
        cur = con.cursor()    
        cur.execute("SELECT * FROM goldenQuestions")

        rows = cur.fetchall()

        for row in rows:
            questions.append(row[1])
            questionsVect.append(text_to_vector( row[1]) )
            answers.append(row[2])
        
    #print(questions)
    #print(answers)
    con.close()

def returnBestAnswer( question ):
    questionVec = text_to_vector(question)

    maxScore = 0
    k = 0
    for  element in questionsVect : 
        score = get_cosine(questionVec, element)
        #print (score)
        if (score  > maxScore):
            bestIndex  = k
            maxScore = score
        k = k +1
        
    print (maxScore)
    if maxScore > 0.5:
        bestAnswer = answers[bestIndex]
    else:
        bestAnswer = "Sorry couldn't understand the question"
    
    return(bestAnswer)
                
if __name__== '__main__':
    print ("in main")
    gatherData()

    testQuestions = ["What do the fuck are you doing",
                    "When is visiting hours?"]

    for question in testQuestions:
        bestAnswer = returnBestAnswer(question)
        print(bestAnswer)

