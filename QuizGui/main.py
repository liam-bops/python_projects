import requests
from ui import QuizUI
from quizbrain import QuizBrain

parameters = {'amount': 10, 'type': 'boolean', }
data = requests.get(url='https://opentdb.com/api.php', params=parameters).json()['results']
# print(data)
quizbrain = QuizBrain(data)
quizui = QuizUI(quizbrain)
