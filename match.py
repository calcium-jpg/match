def match(numbers, sequence):
    right = 0
    arr = []
    
    for s in numbers:
        for (i, j) in enumerate(sequence):
                if j == s[i]:
                    right += 1;
        arr.append({"array": s, "right": right})
        right = 0;
    
    return arr