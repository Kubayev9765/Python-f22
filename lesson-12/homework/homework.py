1.
import threading

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Worker function for threads
def prime_worker(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

# Main function
def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = [[] for _ in range(num_threads)]
    range_size = (end - start) // num_threads

    for i in range(num_threads):
        sub_start = start + i * range_size
        sub_end = start + (i + 1) * range_size if i != num_threads - 1 else end
        thread = threading.Thread(target=prime_worker, args=(sub_start, sub_end, results[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Combine results from all threads
    all_primes = []
    for sublist in results:
        all_primes.extend(sublist)

    all_primes.sort()
    return all_primes

# Example usage
if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4

    primes = threaded_prime_checker(start_range, end_range, num_threads)
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes)


2.

import threading
from collections import Counter
import os

# Function for thread to process lines and count words
def count_words(lines, result_list, index):
    counter = Counter()
    for line in lines:
        words = line.strip().split()
        words = [word.strip('.,!?":;()').lower() for word in words]
        counter.update(words)
    result_list[index] = counter

# Main function to read file and process with threads
def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[start:end], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Combine all thread results
    total_counter = Counter()
    for partial in results:
        total_counter.update(partial)

    return total_counter

# Example usage
if __name__ == "__main__":
    # Replace with your actual file path
    file_path = "large_text.txt"
    
    if os.path.exists(file_path):
        word_counts = threaded_word_count(file_path, num_threads=4)
        print("Word Occurrences Summary:")
        for word, count in word_counts.most_common(20):  # top 20 words
            print(f"{word}: {count}")
    else:
        print(f"File '{file_path}' not found.")

