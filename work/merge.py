import os

def merge_text_files(input_dir, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w') as outfile:
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(input_dir, filename), 'r') as infile:
                    outfile.write(infile.read() + '\n')

if __name__ == "__main__":
    input_dir = './cleaned_notes' 
    output_file = './merged_text_file.txt'  
    merge_text_files(input_dir, output_file)
