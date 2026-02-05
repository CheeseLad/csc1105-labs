import numpy as np

ref = []
with open("example.ref", "r") as f:
    for line in f:
        ref.append(line.strip())

hyp = []
with open("example.hyp", "r") as f:
    for line in f:
        hyp.append(line.strip())

def edit_distance(ref_sentence, hyp_sentence):
    ref_len = len(ref_sentence)
    hyp_len = len(hyp_sentence)

    matrix = np.full((ref_len, hyp_len), 10, dtype=int)
    matrix[0][0] = 0

    for r in range(ref_len):
        for h in range(hyp_len):

            if ref_sentence[r] == hyp_sentence[h]:
                cost = 0
            else:
                cost = 1

            position = matrix[r][h]

            if r > 0 and h > 0:
                sub_position = matrix[r-1][h-1]
                if sub_position + cost < position:
                    position = sub_position + cost

            if h > 0:
                ins_position = matrix[r][h-1]
                if ins_position + 1 < position:
                    position = ins_position + 1

            if r > 0:
                del_position = matrix[r-1][h]
                if del_position + 1 < position:
                    position = del_position + 1

            matrix[r][h] = position

    return matrix


for r, h in zip(ref, hyp):
    result = edit_distance(r.split(), h.split())
    print(f"Edit Distance:\n\n{result}")
