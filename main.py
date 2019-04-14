from read_wikis import LoadWikis

if __name__ == "__main__":
    folder = "data/articles"
    l = LoadWikis(folder)
    l.load_files()
