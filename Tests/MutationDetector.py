def MutationDetector():
    geneRef = open("GeneticDatabase.txt")
    geneSequence = [geneRef.readline()]
    geneAcronym = [geneRef.readline()]
    x = 0
    while x < len(geneAcronym):
        geneDict = {}
        geneDict[geneAcronym[x]] = geneSequence[x]
        x += 1
    for nucleotide in geneDict.values():
        geneValues = []
        geneValues.append(nucleotide)
    gene = geneValues[int(input("Please Select Your Gene of Interest: "))]
    geneList = [nucleotide for nucleotide in gene]
    geneTest = input("Please Input the Sequence you wish to test: ")
    nucleotideList = [nucleotide for nucleotide in geneTest]
    x = 0
    while x < len(geneList):
        if geneList[x] == '\n':
            geneList.pop()
        x += 1
    x = 0
    mutationIndex = []
    while x < len(nucleotideList):
        if nucleotideList[x] != geneList[x]:
            mutationIndex.append(x)
        else:
            mutationIndex = []
        x += 1
    print(mutationIndex)
    print("Gene Mutations found at positions ", mutationIndex)
    G = [geneList[x] for x in mutationIndex]
    N = [nucleotideList[x] for x in mutationIndex]
    print("Nucleotides {} were mutated to {}".format(G, N))
    print("Total Mutations found: ", len(mutationIndex))
    geneRef.close()

