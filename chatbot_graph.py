# coding: utf-8


from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是医药智能助理，希望可以帮到您。'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    print('您好，我是医药智能助理，希望可以帮到您。\n')
    print("请问你叫什么名字？")
    userName = input('用户名:')
    while 1:
        question = input('{}:'.format(userName))
        answer = handler.chat_main(question)
        print('医药智能助理:', answer)

