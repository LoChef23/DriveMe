import json
from Question import Question

with open('questions.json', 'r') as questionsFile:
    questionsList = json.load(questionsFile)

i = 1
for question in questionsList:
    if question['question'] != '' and type(question['isCorrect']) == bool:
        questionID = str(i)
        questionText = question['question']
        isCorrect = question['isCorrect']
        QuestionToBeImported = Question(questionID, questionText, isCorrect)
        QuestionToBeImported.import_in_dynamodb()
        i += 1
    else:
        print(f'Following question could not be imported:\n{question}')
        continue
print('Import completed')