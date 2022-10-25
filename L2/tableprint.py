# computes and visualizes results of binary operation
def tabliczka(x1, x2, y1, y2, fun):
    if x2 < x1 or y2 < y1:
        return ''

    top_id = [x for x in range(x1, x2+1)]
    results = [[fun(i, j) for i in range(x1, x2+1)] for j in range(y1, y2+1)]

    # adding index row
    results.insert([0][0], top_id)

    max_width = len(str(results[-1][-1]))
    if x1 < 0 or y1 < 0:
        max_width += 1
    
    for row_id, row in enumerate(results):

        # adding index column (row index shifted by y1)
        if row_id != 0:
            print(str(row_id+y1-1).rjust(2), end=" ")
        else: print(" ".rjust(3), end="")
        print(' '.join(map(lambda x : str(x).rjust(max_width), row)))
    print('\n')
