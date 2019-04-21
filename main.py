from read_wikis import LoadWikis
import time


if __name__ == "__main__":
    start = time.time()
    folder = "data/articles"
    l = LoadWikis(folder)
    l.load_files()
    l.split_file_in_sentence()
    l.extract_token()
    l.extract_lemmas()
    end = time.time()
    print('Running time', end - start)
