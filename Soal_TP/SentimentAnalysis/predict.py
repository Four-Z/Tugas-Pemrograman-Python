import matplotlib.pyplot as plt


def load_ndsi(ndsi_filename):
    word_ndsi = {}
    with open(ndsi_filename, 'r') as file:
        for i in file:
            i = i.split()
            word_ndsi.update({i[0]: float(i[1])})

    return word_ndsi


def compute_score(filename, word_ndsi):
    unknown_label = []
    with open(filename, 'r', encoding='utf-16-le') as file:
        for i in file:
            unknown_label.append(i.split())

    pos_neg_scores = []
    for i in unknown_label:
        ndsi_positif = 0
        ndsi_negatif = 0
        for j in i:
            for k in word_ndsi:
                if j == k:
                    if word_ndsi[k] > 0:
                        ndsi_positif += word_ndsi[k]
                    elif word_ndsi[k] < 0:
                        ndsi_negatif += abs(word_ndsi[k])

        pos_neg_scores.append((ndsi_positif, ndsi_negatif))

    return pos_neg_scores


def show_scatter_plot(pos_neg_scores):
    plt.clf()

    predicted_as_pos = [(pos_score, neg_score) for (pos_score, neg_score)
                        in pos_neg_scores if pos_score > neg_score]
    predicted_as_neg = [(pos_score, neg_score) for (pos_score, neg_score)
                        in pos_neg_scores if pos_score < neg_score]

    x_pos_1 = [pos_score for (pos_score, _) in predicted_as_pos]
    y_pos_1 = [neg_score for (_, neg_score) in predicted_as_pos]
    x_pos_2 = [pos_score for (pos_score, _) in predicted_as_neg]
    y_pos_2 = [neg_score for (_, neg_score) in predicted_as_neg]

    plt.scatter(x_pos_1, y_pos_1, color='blue', s=5)
    plt.scatter(x_pos_2, y_pos_2, color='hotpink', s=5)

    plt.xlabel("Positive Score")
    plt.ylabel("Negative Score")
    plt.xlim(-0.1, 8)
    plt.ylim(-0.1, 8)
    plt.savefig("senti-plot.pdf")
    plt.show()


if __name__ == "__main__":

    word_ndsi = load_ndsi("Soal_TP/SentimentAnalysis/ndsi.txt")

    pos_neg_scores = compute_score(
        "Soal_TP/SentimentAnalysis/sent-unknown-label-utf-16-le.txt", word_ndsi)

    show_scatter_plot(pos_neg_scores)

    for i, (pos_score, neg_score) in enumerate(pos_neg_scores):
        predicted_label = "neutral"
        if pos_score > neg_score:
            predicted_label = "pos"
        elif neg_score > pos_score:
            predicted_label = "neg"
        print(
            f"sentence {i+1} -- pos:{pos_score:6.3f}  neg:{neg_score:6.3f}  prediction:{predicted_label}")
