class WordsFinder:

    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        execute = [',', '.', '=', '!', '?', ';', ':', ' - ']
        split = ' '
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in execute:
                        line = line.replace(i, ' ')
                split = split + line
                all_words.update({self.file_names: split.split()})
        return all_words

    def find(self, word):
        w_p = {}
        all_words = self.get_all_words()
        for file_names, words in all_words.items():
            if word.lower() in words:
                w_p[file_names] = words.index(word.lower()) + 1
        return w_p

    def count(self, word):
        w_p = {}
        all_words = self.get_all_words()
        for file_names, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                w_p[file_names] = count
        return w_p

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего