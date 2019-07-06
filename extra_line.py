import re
import nltk


article_text = "A series of coordinated bombings on Easter Sunday rocked Sri Lanka, killing at least 257 people (with the death toll revised down from 359 by authorities) and wounding 500 others. The attacks were the deadliest on the island nation since the end of its civil war 10 years ago, and targeted three churches as well as four hotels in the capital, Colombo. Nearly all victims were Sri Lankan, many of them Christian worshippers attending Easter mass. Dozens of foreigners were also killed. Authorities said the attacks were carried out by two little-known Muslim organisations."

article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
article_text = re.sub(r'\s+', ' ', article_text)  

formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  

sentence_list = nltk.sent_tokenize(article_text)

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(formatted_article_text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

import heapq  
summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print(summary)  
print("===========================")
print(article_text)

# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
# from nltk.corpus import wordnet as wn

# def tag(sentence):
#   words = word_tokenize(sentence)
#   words = pos_tag(words)
#   return words

# def paraphraseable(tag):
#   return tag.startswith('VB') or tag.startswith('JJ')

# def pos(tag):
#   if tag.startswith('NN'):
#     return wn.NOUN
#   elif tag.startswith('V'):
#     return wn.VERB

# def synonyms(word, tag):
#     lemma_lists = [ss.lemmas() for ss in wn.synsets(word, pos(tag))]
#     lemmas = [lemma.name() for lemma in sum(lemma_lists, [])]
#     return set(lemmas)

# def synonymIfExists(sentence):
#   for (word, t) in tag(sentence):
#     if paraphraseable(t):
#       syns = synonyms(word, t)
#       if syns:
#         if len(syns) > 1:
#           yield list(syns)[0]
#           continue
#     yield word

# def paraphrase(sentence):
#   return [x for x in synonymIfExists(sentence)]

# def the_summary(sentence):
# 	x = ' '.join(paraphrase(sentence))
# 	return x 

# if __name__ == '__main__':
  
#   print(x)