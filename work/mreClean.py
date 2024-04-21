 
import re

def remove_expressions(input_file, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                line = re.sub(r'_+', '', line)
                outfile.write(line)

if __name__ == "__main__":
    input_file = './processed_text_file.txt'  
    output_file = './final.txt' 
    remove_expressions(input_file, output_file)

