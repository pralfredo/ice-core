import pandas as pd
from openpyxl import Workbook
df = pd.read_excel('abs.xlsx', sheet_name=1)
abstracts = []
for i in df.values.tolist():
    abstracts.append(i[0])  
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
# Preprocessing function
def preprocess_text(text):
    # Text cleaning
    remove = ['SUB', 'SUP', 'nss', '$\\delta', '$\\Delta']
    ## remove = ['SUB', 'SUP', 'nss', '$\\delta', '$\\Delta', 'ice', 'core', 'greenland', 'antarctica', 'antarctic', 'Ice', 'Core', 'Greenland', 'Antarctica', 'Antarctic']
    for i in remove:
      text = text.replace(i, "")
    text = text.translate(str.maketrans('', '', string.punctuation)) #remove punctuations
    text = text.translate(str.maketrans('', '', string.digits)) #remove digits
    text = text.lower()
    # Tokenization
    tokens = word_tokenize(text)
    # Stop word removal
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # Remove short words
    tokens = [token for token in tokens if len(token) > 2]
    # Join tokens back to text
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text
# Preprocess the list of abstracts
docs = [preprocess_text(abstract) for abstract in abstracts]
wb = Workbook()
ws = wb.active
for item in docs:
    ws.append([item])
wb.save("words.xlsx")