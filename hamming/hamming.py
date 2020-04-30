def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are of different length.")
    hamming = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming += 1
    return hamming
