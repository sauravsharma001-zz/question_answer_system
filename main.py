# from read_wikis import LoadWikis
import time, json
from ProcessQuestion import ProcessQuestion as PQ
from QuestionAnswerResponse import QuestionAnswerResponseEncoder, QuestionAnswerResponse
from ProcessWikis import ProcessWiki as PW

questions = []
question_analysis = []
drm = None
paragraphs = []


def read_questions(file):
    try:
        with open(file, "r") as fd:
            for f in fd:
                questions.append(f.strip())
    except OSError as err:
        print("exception", err)


def read_wiki(datasetName):
    try:
        dataset_file = open(datasetName, "r", encoding='utf-8-sig')
        for para in dataset_file.readlines():
            if len(para.strip()) > 0:
                paragraphs.append(para.strip())
    except FileNotFoundError:
        print("Bot> Oops! I am unable to locate \"" + datasetName + "\"")
        exit()


if __name__ == "__main__":

    start = time.time()
    question_file = "data/q.txt"
    read_wiki("data/articles/AppleInc.txt")
    read_questions(question_file)

    drm = PW(paragraphs, True, True)

    for q in questions:
        pq = PQ(q, True, False, True)
        ans, par = drm.query(pq)
        # print(pq)
        question_analysis.append(QuestionAnswerResponse(pq.question, ans, par, pq.searchQuery))

    a = QuestionAnswerResponseEncoder().encode(question_analysis)
    print(a)
    # # folder = "data/articles"
    # # l = LoadWikis(folder)
    # # l.load_files()
    # # l.split_file_in_sentence()
    # # l.extract_token()
    # # l.extract_lemmas()
    # end = time.time()
    # print('Running time', end - start)
