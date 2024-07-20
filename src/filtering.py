import heapq
import re


def paragraph_length_filter(x):
    lines = x["text"].split("\n")
    if len(lines) < 1 or min(heapq.nlargest(3, [len(line) for line in lines])) < 3:
        return False
    return True


def paragraph_repetition_filter(x):
    text = x["text"]
    paragraphs = re.compile(r"\n{2,}").split(text.strip())
    paragraphs_duplicates, char_duplicates = find_duplicates(paragraphs)
    if paragraphs_duplicates / len(paragraphs) > 0.3:
        return False
    if char_duplicates / len(text) > 0.2:
        return False
    return True


def find_duplicates(paragraphs):
    unique_x = set()
    duplicate_chars = 0
    duplicate_elements = 0
    for element in paragraphs:
        if element in unique_x:
            duplicate_chars += len(element)
            duplicate_elements += 1
        else:
            unique_x.add(element)
    return duplicate_elements, duplicate_chars


def deduplication(ds):
    def dedup_func(x):
        if x["text"] in unique_text:
            return False
        else:
            unique_text.add(x["text"])
            return True

    unique_text = set()
    ds = ds.filter(dedup_func, load_from_cache_file=False, num_proc=1)
    return ds


def apply_filtering(ds):
    ds = ds.filter(paragraph_length_filter, load_from_cache_file=False)
    ds = ds.filter(paragraph_repetition_filter, load_from_cache_file=False)
    ds = deduplication(ds)
    return ds
