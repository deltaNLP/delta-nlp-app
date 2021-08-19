import spacy
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from django.conf import settings


# load youtube video and get transcript
transcript = YouTubeTranscriptApi.get_transcript('OgYe6y8_Cx8')
print(transcript)


#  Create df of transcript
transcript_df = pd.DataFrame(transcript)


# get the lenght of the video
start_time = transcript_df['start'].iloc[-1]
duration_time = transcript_df['duration'].iloc[-1]
length = (start_time + duration_time)
print(length)
print(length/60)
print((length/60).round())


# use only the text column
transcript_text_df = transcript_df.loc[:, ['text']]


# lemmatization
nlp = spacy.load('en_core_web_sm')

def lemmatizer(text):        
    sent = []
    doc = nlp(text)
    for word in doc:
        sent.append(word.lemma_)
    return " ".join(sent)

transcript_text_df = transcript_text_df.applymap(lemmatizer)


# get the whole text as one
text = " ".join(i for i in transcript_text_df.text)
text_split = text.split()
text_3_letters = [word for word in text_split if len(word) > 2]
text_3_letters = " ".join(i for i in text_3_letters)


# wordcloud
input_text = text_3_letters

plt.rcParams['figure.figsize']=(12.0,12.0)  # set default size of plots
plt.rcParams['font.size']=12                # set default font size
plt.rcParams['savefig.dpi']=100             # set default save figure resolution
plt.rcParams['figure.subplot.bottom']=.1    # set subplot bottom
# Create stop words list
stop_words = set(STOPWORDS) 
stop_words.update(['','']) # if you want to add a word to the stop words list


# Generate a word cloud image
wordcloud = WordCloud(
                        stopwords=stop_words, # set of words to ignore
                        background_color='white', # set background color
                        max_words=500, # max number of words
                        max_font_size=50, # max font size of the words
).generate(input_text)


# Display the generated image:
fig = plt.figure(1)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()