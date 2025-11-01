import re
from collections import defaultdict

def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = re.split(r"[;,. ]+", file.read().upper())

            count_set = defaultdict(int)

            for word in content:
                count_set[word] += 1
            
            sorted_words = dict(sorted(count_set.items(), key=lambda item: item[1], reverse=True))

            words = sorted_words.keys()
            total_words = len(words)
            print("Total Words : ", total_words)
            
            max = 20
            index = 0

            print(f"Top {max} words")
            for key, value in sorted_words.items():
                index += 1

                if index > max:
                    break

                print(f"{key}\t{value}")

    except Exception as e:
        print(f"An error occured : {e}")

# from count_words.app import count_words