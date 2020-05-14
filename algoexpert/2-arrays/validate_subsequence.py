
# Time Complexity O(N)
# Space Complexity O(1)

def validate_subsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)
