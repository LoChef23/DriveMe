# file with questions should be uploaded in the main folder
# script should be launched from the main folder
import json
from Question import Question

with open('questionsToBeInserted.json', 'r', encoding='utf-8') as questionsFile:
    questionsList = json.load(questionsFile)
    

i = 1
for question in questionsList:
    if question['question'] != '' and type(question['isCorrect']) == bool:
        questionID = str(i)
        questionText = question['question']
        if 'image' in question.keys():
            questionImage = question['image']
        else:
            questionImage = '-'
        isCorrect = question['isCorrect']
        QuestionToBeImported = Question(questionID, questionText, questionImage, isCorrect)
        QuestionToBeImported.import_in_dynamodb()
        i += 1
    else:
        print(f'Following question could not be imported:\n{question}')
        continue
print('Import completed')