# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
text = """Today various organizations, be it online shopping, government and private sector organizations, catering and tourism industry or other institutions that offer customer services are concerned about their customers and ask for feedback every single time we use their services. Consider the fact, that these companies may be receiving enormous amounts of user feedback every single day. And it would become quite tedious for the management to sit and analyze each of those.
But, the technologies today have reached to an extent where they can do all the tasks of human beings. And the field which makes these things happen is Machine Learning. The machines have become capable of understanding human languages using Natural Language Processing. Today researches are being done in the field of text analytics.
And one such application of text analytics and NLP is a Feedback Summarizer which helps in summarizing and shortening the text in the user feedback. This can be done an algorithm to reduce bodies of text but keeping its original meaning, or giving a great insight into the original text.

If you’re interested in Data Analytics, you will find learning about Natural Language Processing very useful. Python provides immense library support for NLP. We will be using NLTK – the Natural Language Toolkit. which will serve our purpose right. """

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence
print(summary)
