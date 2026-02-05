ref = []
with open("example.ref", "r") as f:
    for line in f:
        ref.append(line.strip())

hyp = []
with open("example.hyp", "r") as f:
    for line in f:
        hyp.append(line.strip())

def word_counts(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def unigram_matching(ref_sentence, hyp_sentence):
    ref_counts = word_counts(ref_sentence)
    hyp_counts = word_counts(hyp_sentence)

    matches = 0
    for word in ref_counts:
        if word in hyp_counts:
            matches += min(ref_counts[word], hyp_counts[word])

    return matches

def precision(ref_sentence, hyp_sentence):
    matches = unigram_matching(ref_sentence, hyp_sentence)
    hyp_words = len(hyp_sentence.split())
    if hyp_words == 0:
        return 0.0
    return matches / hyp_words

def recall(ref_sentence, hyp_sentence):
    matches = unigram_matching(ref_sentence, hyp_sentence)
    ref_words = len(ref_sentence.split())
    if ref_words == 0:
        return 0.0
    return matches / ref_words


print("Unigram Matches for each sentence pair:")
for r, h in zip(ref, hyp):
    matches = unigram_matching(r, h)
    print(f"Ref: {r}\nHyp: {h}\n\nMatches: {matches}")
    precision_score = precision(r, h)
    print(f"Precision: {precision_score}")
    recall_score = recall(r, h)
    print(f"Recall: {recall_score}")