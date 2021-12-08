import string
import matplotlib.pyplot as plt


def load_stop_words(filename):

    with open(filename, 'r') as temp:
        stop_words = []
        for i in temp:
            stop_words.append(i.lower().strip())

    stop_words = set(stop_words)

    return stop_words


def count_words(filepath, stop_words):
    listWords = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for i in file:
            i = i.split()
            for j in i:
                if j not in stop_words and j not in string.punctuation:
                    listWords.append(j)

    listWords_temp = set(listWords)

    word_freq = {}
    for i in listWords_temp:
        word_freq.update({i: listWords.count(i)})

    return word_freq


def compute_ndsi(word_freq_pos, word_freq_neg):

    word_ndsi = {}

    for word in word_freq_neg:
        if word_freq_pos.get(word) is None:
            ndsi = -1
        else:
            ndsi = (word_freq_pos[word] - word_freq_neg[word]) / \
                (word_freq_pos[word] + word_freq_neg[word])

        word_ndsi.update({word: float(ndsi)})

    for word in word_freq_pos:
        if word_freq_neg.get(word) is None:
            ndsi = 1
            word_ndsi.update({word: float(ndsi)})

    return word_ndsi


def show_ndsi_histogram(word_ndsi):

    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor='g', alpha=0.75)
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")
    plt.show()


if __name__ == "__main__":
    stop_words = load_stop_words('Soal_TP/SentimentAnalysis/stopwords.txt')
    word_freq_neg = count_words(
        'Soal_TP/SentimentAnalysis/sent-polarity-data/rt-polarity.neg', stop_words)
    word_freq_pos = count_words(
        'Soal_TP/SentimentAnalysis/sent-polarity-data/rt-polarity.pos', stop_words)
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    show_ndsi_histogram(word_freq_ndsi)

    word_freq_ndsi_sorted = sorted(word_freq_ndsi.items(), key=lambda x: x[1])

    with open('Soal_TP/SentimentAnalysis/ndsi.txt', 'w') as ndsi_filename:
        for i in range(len(word_freq_ndsi_sorted)):
            ndsi_filename.write(
                f"{word_freq_ndsi_sorted[i][0]} {word_freq_ndsi_sorted[i][1]}\n")
