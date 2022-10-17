def tabliczka(x1, x2, y1, y2):
    top_id = [x for x in range(x1, x2+1)]
    results = [[i*j for i in range(x1, x2+1)] for j in range(y1, y2+1)]
    results.insert([0][0], top_id)
    max_width = len(str(results[-1][-1]))
    if x1 < 0 or y1 < 0:
        max_width += 1
    
    #print(' '.join(map(lambda x : str(x).rjust(max_width), row))
    for row_id, row in enumerate(results):
        if row_id != 0:
            print(str(row_id+y1).rjust(2), end=" ")
        else: print(" ".rjust(3), end="")
        print(' '.join(map(lambda x : str(x).rjust(max_width), row)))

tabliczka(3, 5, 2, 4)