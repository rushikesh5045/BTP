import os
import string
from nltk.tokenize import word_tokenize

def remove_punctuation(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    punctuations = set(string.punctuation)

    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(input_dir, filename), 'r') as file:
                tokens = word_tokenize(file.read())

                tokens = [token for token in tokens if token not in punctuations]

                output_filename = f"clean_{filename}"
                with open(os.path.join(output_dir, output_filename), 'w') as output_file:
                    output_file.write(' '.join(tokens))

if __name__ == "__main__":
    input_dir = './tokenized_notes'
    output_dir = './cleaned_notes'
    remove_punctuation(input_dir, output_dir)
