"""
Attempt to use the sprawl mechanisms to index the Moby thesaurus

"""
import gensim.models as gm
import pickle
import sprawl.nGram as sn
import sys
import time

start = time.time()
MobyThesaurus = 'mthes/mobythes3'
engEmb = '/home/staylor/spring24/EnglishEmbedding12/model.bin'

model = gm.KeyedVectors.load_word2vec_format(engEmb, binary = True)
print('embedding loaded', time.time()-start)


def main():

    thes = sn.unigrams(MobyThesaurus, ', \n')
    print('after unigram',time.time()-start)
    dic1 = sn.dictio(thes,1)
    print('after dictio',time.time()-start)
    offset = dic1.find('plate')
    print(offset, thes.get(offset))
    offsets, counts = dic1.count()
    maxCount = max(counts)
    wordcount = sum(counts)
    print(len(offsets), 'distinct items.  Max count: ', maxCount)
    histo = [0]*(maxCount+1)
    for c in counts:
        histo[c]+=1
    print ('count of counts\n    #    occurrences')
    #for i,c in enumerate(histo):
    #    if c == 0: continue
    #    print(i, c)

    current = wdssofar = ctsofar = 0
    ten = 10
    for i in range(ten):
        num = i+1
        frac = num/ten
        while wdssofar/wordcount < frac:
            wdssofar += current * histo[current] 
            current += 1
        print (wdssofar, 'words with count less than', current)



if __name__ == '__main__': main()

        
