import nltk
from nltk.corpus import stopwords

# Download NLTK stop words (you only need to do this once)
nltk.download('stopwords')

# Load the English stop words
stop_words = set(stopwords.words('english'))

# Function to remove stop words from a document
def remove_stop_words(document):
    # Tokenize the document into words
    words = nltk.word_tokenize(document.lower())  # Lowercase the document before tokenization
    # Remove stop words from the tokenized words
    filtered_words = [word for word in words if word not in stop_words]
    # Join the filtered words back into a sentence
    filtered_sentence = ' '.join(filtered_words)
    return filtered_sentence

# Read the medical dataset from a text file
input_file_path = './final.txt'  # Specify the path to your input text file
output_file_path = './output.txt'  # Specify the path for the output filtered text file

with open(input_file_path, 'r') as input_file:
    # Read the content of the input file
    medical_dataset = input_file.readlines()

# Remove stop words from each document in the dataset
filtered_dataset = [remove_stop_words(document) for document in medical_dataset]

# Save the filtered dataset to a new text file
with open(output_file_path, 'w') as output_file:
    # Write each document in the filtered dataset to the output file
    for document in filtered_dataset:
        output_file.write(document + '\n')

print(f"Filtered dataset saved to '{output_file_path}'.")
