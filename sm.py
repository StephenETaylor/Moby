"""
Attempt to use the sprawl mechanisms to index the Moby thesaurus

"""
import gensim.models as gm
KeyedVectors = gm.KeyedVectors
import pickle
import sprawl.nGram as sn
unigrams=sn.unigrams    # class names needed for unpickling
dictio = sn.dictio
import sys
import time

start = time.time()
MobyThesaurus = 'mthes/mobythes3'
engEmb = '/home/staylor/spring24/EnglishEmbedding12/model.bin'


def main1():
    #get english embedding, and dump it to pickle file
    model = gm.KeyedVectors.load_word2vec_format(engEmb, binary = True)
    print('embedding loaded', time.time()-start)
    with open('12.pickle','wb') as fob:
        pickle.dump(model,fob)
    print('embedding dumped', time.time()-start)

    #get thesaurus, and dump it to pickle file
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
    with open('thes.pickle','wb') as fob:
        pickle.dump((thes,dic1,offsets,counts,histo),fob)
    main2()

def main2(): #load the pickle files
    with open('12.pickle','rb') as fib:
        model2 = pickle.load(fib)

    print('loaded KeyedVectors',time.time()-start)

    with open('thes.pickle','rb') as fib:
        (thes2,dic12,offsets2,counts2,histo2) = pickle.load(fib)

    print('loaded thesaurus',time.time()-start)
    plate_offset = dic12.find('plate')
    plate_line = thes2.contents[plate_offset]
    for i in offsets2:
        if i == plate_offset:
            plate_appearances = counts2[i]
            break
    print('offset:',plate_offset, 'word:', thes2.get(plate_offset))
    print('synset line', plate_line)
    print('appearances', plate_appearances)
    print('offset:',plate_offset+1, 'next word:', thes2.get(plate_offset+1))


if __name__ == '__main__': main1()

        
