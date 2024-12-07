import string
import requests
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import logging
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Configure colorful logging
class ColorfulFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        record.msg = f"{color}{record.msg}{Style.RESET_ALL}"
        return super().format(record)

# Logger configuration
handler = logging.StreamHandler()
formatter = ColorfulFormatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger()

# Function to fetch text from a URL
def fetch_text(url):
    try:
        logger.info("Downloading text from URL...")
        response = requests.get(url)
        response.raise_for_status()
        logger.info("Text successfully downloaded.")
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error downloading text: {e}")
        return None

# Function to remove punctuation
def remove_punctuation(text):
    logger.info("Removing punctuation from text...")
    return text.translate(str.maketrans('', '', string.punctuation))

# Map function: creates a (word, 1) pair
def map_function(word):
    return word, 1

# Shuffle function: groups words
def shuffle_function(mapped_values):
    logger.info("Grouping results by keys...")
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    logger.info("Grouping completed.")
    return shuffled.items()

# Reduce function: counts frequency
def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)

# Function to execute MapReduce
def map_reduce(text, top_n=10):
    # Clean text
    cleaned_text = remove_punctuation(text).lower()

    # Split text into words
    words = cleaned_text.split()
    logger.info(f"Word count in text: {len(words)}")

    # Map stage
    with ThreadPoolExecutor() as executor:
        mapped = list(executor.map(map_function, words))
    logger.info("Map stage completed.")

    # Shuffle stage
    shuffled = shuffle_function(mapped)

    # Reduce stage
    with ThreadPoolExecutor() as executor:
        reduced = list(executor.map(reduce_function, shuffled))
    logger.info("Reduce stage completed.")

    # Sort results
    sorted_word_counts = sorted(reduced, key=lambda x: x[1], reverse=True)
    logger.info("Sorting completed.")
    return sorted_word_counts[:top_n]

# Function to visualize results
def visualize_top_words(word_counts):
    logger.info("Visualizing results...")
    words, counts = zip(*word_counts)
    plt.barh(words, counts, color='skyblue')
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title("Top 10 Most Frequent Words")
    plt.gca().invert_yaxis()
    plt.show()
    logger.info("Visualization completed.")

# Main function
if __name__ == "__main__":
    # URL for the text
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    text = fetch_text(url)
    if text:
        # Execute MapReduce
        top_words = map_reduce(text, top_n=10)
        logger.info("Top 10 words by frequency:")
        for word, count in top_words:
            logger.info(f"{word}: {count}")

        # Visualization
        visualize_top_words(top_words)
    else:
        logger.error("Failed to download text for analysis.")
