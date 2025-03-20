import numpy as np

def load(fname):
    with open(fname, "r") as f:
        rows = f.readlines()
        n = int(rows[0])
        names = []
        matrix = []
        for i in range(1, n+1):
            row = rows[i].strip()
            fields = row.split()
            name = str(fields[0]) + ' ' + str(fields[1])
            scores = np.array(fields[3:], dtype=np.float32).reshape(5, 1)
            names.append(name)
            matrix.append(scores)
    return np.hstack(matrix), names

if __name__ == "__main__":
    matrix, names = load("score.txt")
    matrix = np.sort(matrix, axis=0)
    middleScore = matrix[1 : -1]
    middleScore = np.sum(middleScore, axis=0)
    top3_indices = np.argsort(middleScore)[-3:][::-1]
    print(top3_indices)
    print(names)
    print("Final Ranking:")
    for rank, idx in enumerate(top3_indices, 1):
        print(f"{rank}: {names[idx]} - Score: {middleScore[idx]:.1f}")