def polyndromCheck(N):
    checkResult = False;
    NStringArray = list(str(N))
    NStringReverseArray = list(reversed(NStringArray))
    NStringPolyndrom = ''.join(NStringReverseArray)
    if (NStringPolyndrom == str(N)):
        checkResult = True
    return checkResult

def polyndromGet(N):
    nRange = range(0,N-1)
    polyndromeCandidatesList = []
    for i in nRange:
        polyndromeCandidatesList.append(N-i)
    for polyndromCandidate in polyndromeCandidatesList:
        if (polyndromCheck(polyndromCandidate)):
            return polyndromCandidate

polyndromGet(120)