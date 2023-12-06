# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def getSeqDifferences(seq: str) -> list:
    seq_dif = []
    for i in range(len(seq) - 1):
        next_char = seq[i + 1]
        diff = int(ord(seq[i]) - ord(next_char))
        seq_dif.append(diff)

    return seq_dif

# a = len of str
# b = n strs

# O(a * b) worst case - early terminates as soon as odd one out is found.

def findOdd(series):
    # Write your code here
    # 1. go over each letter, and track difference between adjacent ones
    # 2. check if a pattern emerges
    
    prev_differences = getSeqDifferences(series[0])
    
    for i, seq in enumerate(series[1::], start=1):
        seq_differences = getSeqDifferences(seq)

        if seq_differences != prev_differences:
            # try fetch before value or after, no matter, as long as its safe
            if i < len(series) - 1:
                comparison_differences = getSeqDifferences(series[i+1])
            else:
                comparison_differences = getSeqDifferences(series[i-2])
            
            if comparison_differences == prev_differences:
                return seq
            
            if comparison_differences == seq_differences:
                return series[i-1]
        
        prev_differences = seq_differences
    
    
    
    

print(findOdd([
    "AAB",
    "ABC",
    "AAB"
    ]))