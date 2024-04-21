import nltk
nltk.download('punkt')
import os
from nltk.tokenize import word_tokenize

def tokenize_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(input_dir, filename), 'r') as file:
                text = file.read()
                tokens = word_tokenize(text)
                output_filename = f"tokenized_{filename}"
                with open(os.path.join(output_dir, output_filename), 'w') as output_file:
                    output_file.write(' '.join(tokens))

if __name__ == "__main__":
    input_dir = './Deidentified_Notes'
    output_dir = './Tokenized_Notes'
    tokenize_files(input_dir, output_dir)
