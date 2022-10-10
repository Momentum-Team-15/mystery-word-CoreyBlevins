STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]
PUNCTUATION = [
    '.', '!', '?', ',', "-", ':', ';', '"', "'"
]
# Function used to sort words by frequency within a txt file
def print_word_freq(file):
    # Open the file
    with open(file, "r") as txt:
    # Read content within file
        text_content = txt.read()
    # Remove punctuation while content is a string
    for char in text_content:
        if char in PUNCTUATION:
            text_content = text_content.replace(char, "")
    # Turn content into a list
    text_content = text_content.split()
    # Convert everything to lowercase
    text_content = [word.lower() for word in text_content]
    print(text_content)
    # Remove stop words from the list
    text_content = [word for word in text_content if word not in STOP_WORDS]
    # Create 2 empty dictionaries. One for * and one for integers
    word_dict = {}
    tally_dict = {}
    # Count every item in the list and add an * for display
    # Pairs every word in content as a key with * or int as value in dictionary
    for word in text_content:
        if word in word_dict and word in tally_dict:
            word_dict[word] += "*"
            tally_dict[word] += 1
        else:
            word_dict[word] = "*"
            tally_dict[word] = 1
    # Sort words from least to most frequent within content
    # Converts dictionary to tuples within a list
    # Lambda function sorts tuple by value in position [1]
    sorted_list = sorted(tally_dict.items(), key=lambda tuple: tuple[1])
    # Convert list tuple back to dictionary
    sorted_dict = dict(sorted_list)
    # For every word in content: print word | integer *
    for key in sorted_dict:
        print(f"{key} | {len(word_dict[key])} {word_dict[key]}")

if __name__ == "__main__":
    import argparse
    from pathlib import Path

parser = argparse.ArgumentParser(
    description='Get the word frequency in a text file.')
parser.add_argument('file', help='file to read')
args = parser.parse_args()

file = Path(args.file)
if file.is_file():
    print_word_freq(file)
else:
    print(f"{file} does not exist!")
    exit(1)


# Figure out why - is not removed