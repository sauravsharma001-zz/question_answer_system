from json import JSONEncoder
import json


class QuestionAnswerResponseEncoder(JSONEncoder):

    def default(self, object):

        if isinstance(object, QuestionAnswerResponse):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)


class QuestionAnswerResponse:

    def __init__(self, que, ans, sens=None, docs=None):
        self.Question = que
        self.answers = [ans]
        self.sentences = sens
        self.documents = docs
