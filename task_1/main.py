from collections import Counter
import re
from nltk.corpus import stopwords 


def read_words(filename):
    """
    Reads words from a text file.

    Args:
        filename: The name of the text file.

    Returns:
        A list of words from the file.
    """
    with open(filename, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        return words


def count_lines(filename):
    """
    Counts the number of lines in a text file.

    Args:
        filename: The name of the text file.

    Returns:
        The number of lines in the file.
    """
    with open(filename, 'r') as file:
        return sum(1 for _ in file)


def get_top_n_words(filename, n):
    """
    Gets the top n most frequent words in a text file.

    Args:
        filename: The name of the text file.
        n: The number of top words to return.

    Returns:
        A list of tuples, where each tuple contains a word and its frequency.
    """
    words = read_words(filename)
    stop_words = set(stopwords.words('english'))
    word_counts = Counter(word for word in words if word not in stop_words)
    return word_counts.most_common(n)


def main():
    filename = "romeo-and-juliet.txt"
    word_count = len(read_words(filename))
    line_count = count_lines(filename)
    top_words = get_top_n_words(filename, 5)

    print(f"Total words: {word_count}")
    print(f"Total lines: {line_count}")
    print("Top 5 most frequent words:")
    for word, count in top_words:
        print(f"{word} - {count}")


if __name__ == "__main__":
  main()