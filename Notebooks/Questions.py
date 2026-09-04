class FillQuestion:
    qtype = '0'
    def __init__(self, prompt, text, answer):
        self.prompt = prompt
        self.text = text
        self.answer = answer
        
class MultQuestion:
    qtype='1'
    def __init__(self, prompt, answer, right ='Correct!', wrong='Incorrect.'):
        self.prompt = prompt
        self.answer = answer
        self.right = right
        self.wrong = wrong
        
class Solution:
    qtype= '2'
    def __init__(self, answer):
        self.answer = answer

class CodeLine:
    qtype = '3'
    def __init__(self, prompt, answer, right='Correct!', wrong='Incorrect.'):
        self.prompt = prompt
        self.answer = answer
        self.right = right
        self.wrong = wrong

def question(q):
    if q.qtype == '0':
        solution = input(q.prompt + "\n\n" + q.text)
        print(q.answer)

    elif q.qtype == '1':
        solution = input(q.prompt)
        if solution == q.answer:
            print(q.right)
        else:
            print(q.wrong + "\n\nThe right answer is " + q.answer)

    elif q.qtype == '2':
        print(q.answer)

    elif q.qtype == '3':
        solution = input(q.prompt + "\n> ")
        if solution.strip() == q.answer.strip():
            print(q.right)
        else:
            print(q.wrong + "\n\nThe right line is:\n" + q.answer)

        
def solution(question):
    if question.qtype=='2':
        print(question.answer)    