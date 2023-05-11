import io
import tkinter as tk
from googletrans import Translator
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from collections import Counter

nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('wordnet')

def translate_text():
    #user input
    text = text_input.get("1.0", tk.END)
    
    #Get language
    target_lang = language_var.get()
    
    #translation
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang).text
    
    #tokenization
    tokenized_text = word_tokenize(translated_text)
    
    #lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(word) for word in tokenized_text]
    
    #sentiment analysis
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(translated_text)
    sentiment = ''
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    #count most frequent word
    word_count = Counter(lemmatized_text)
    most_common_word = word_count.most_common(1)[0][0]
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated_text)
    stats_label.config(text="Sentiment: {}, Most Common Word: {}".format(sentiment, most_common_word))
    
    with io.open('results.txt', 'w', encoding='utf-8') as f:
        f.write("Original Text: {}\n".format(text))
        f.write("Translated Text: {}\n".format(translated_text))

root = tk.Tk()
root.title("Language Translator")

text_input_label = tk.Label(root, text="Enter the text to translate:")
text_input_label.pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

#Lang dropdown
language_var = tk.StringVar(root)
language_var.set("French") # Set the default value
language_dropdown_label = tk.Label(root, text="Select the target language:")
language_dropdown_label.pack()
language_dropdown = tk.OptionMenu(root, language_var, "French", "Spanish", "German", "Italian", "Japanese", "Korean", "Portuguese", "Chinese (Simplified)", "Chinese (Traditional)")
language_dropdown.pack()

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

#Translated text
output_label = tk.Label(root, text="Translated Text:")
output_label.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

#Stats label
stats_label = tk.Label(root, text="")
stats_label.pack()

root.mainloop()