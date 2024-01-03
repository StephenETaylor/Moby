"""
Attempt to use the sprawl mechanisms to index the Moby thesaurus

"""
import sprawl.nGram as sn
import sys
import time

start = time.time()
MobyThesaurus = 'mthes/mobythes3'

thes = sn.unigrams(MobyThesaurus, ', \n')
print('after unigram',time.time()-start)
dic1 = sn.dictio(thes,1)
print('after dictio',time.time()-start)
offset = dic1.find('plate')
print(offset, thes.get(offset))

def main():
    pass
    
