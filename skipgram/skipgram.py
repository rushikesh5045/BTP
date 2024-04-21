import glob
import numpy as np
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

final = []

for file in glob.glob('*.txt'):
    with open(file, 'r') as f:
        file_content = f.read()
        list_temp = [file_content]
        final.append(list_temp)

finalEmbedding = []

max_length = 0  # Track the maximum length of tokenized_text

for sent in final:
    text_data = sent[0]
    tokenized_text = word_tokenize(text_data.lower())
    max_length = max(max_length, len(tokenized_text))
    model = Word2Vec(sentences=[tokenized_text], vector_size=100, window=5, sg=1, min_count=1)
    temp = [model.wv[word] for word in tokenized_text]
    finalEmbedding.append(temp)

# Pad the sequences to make them uniform in length
finalEmbedding_padded = [seq + [[0] * 100] * (max_length - len(seq)) for seq in finalEmbedding]

# Convert finalEmbedding to a numpy array
finalEmbedding_array = np.array(finalEmbedding_padded)

# Save the numpy array to a .npy file
np.save('finalEmbedding.npy', finalEmbedding_array)

# Print the first entry in finalEmbedding
# print(finalEmbedding[0])
