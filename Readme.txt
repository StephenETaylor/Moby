I had the idea that instead of translation, one could use a thesaurus, and I
downloaded the Moby thesaurus from
https://web.archive.org/web/20170930060409/http://icon.shef.ac.uk/Moby/mthes.tar.Z

The Moby project may also be available through project Guttenberg.

It was apparently compiled by Grady Ward.

The code in this repository uses the sprawl repository code to index, etc.
the Moby thesaurus.  

The overriding idea is to play with synsets as follows:
	(Moby thesaurus synsets are huge.  There are only 
	[about 3E4] of them versus
	[about 2.5E8] words in the thesaurus.
	thus each synset contains on average 8E4 words. So we'll sample the 
	synsets drastically to make the job plausible.)
Consider a word  W with N synsets, of M elements each.
Then at depth 1, we have a max of NM words.  Some of the words will repeat.
     at depth 2, assuming each new word has similar statistics, we have a
      max of (NM)**2 words.

if we are picky about which words and synsets we choose, we can probably have 
an interesting group of synsets S with X < 300 words.  
  if we create an X by 300  matrix of word embeddings for the X words,
  and take the SVD of the matrix, we get a set B of X 300-dimensional basis 
  vectors for the X words.
  In particular, we can represent the word W and all the words in each of its
  synsets in terms of B.   Now each synset S_i presumably has an in-context
  vector V_i, with the property that \forall w \in S_i : V_i \dot w > 0;
  That is, every element in a synset can appear in the synset contexts.  
  So if we built an embedding in which synsets S_i were labeled and thus could
  have embedding vectors V_i, each use of an element of the synset contributes
  to the embedding, and thus (according to its unknown frequency of usage 
  in the synset) has acquired as part of its ordinary skipgram embedding
  a subpart of its embedding which is parallel to V_i. 
  Given that the set of words is chosen based on synsets,
  It seems plausible that B will provide vectors such that each synset vector 
  V_i is 
  dominated by a vector from B



