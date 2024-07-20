import re

import emoji
from datasets import load_dataset


def load_data(dataset_name):
    return load_dataset(dataset_name, split="train")


def remove_emojis(example):
    example["text"] = emoji.replace_emoji(example["text"], replace="")
    return example


def clean_text(example):
    example["text"] = re.sub(r"http[s]?://\S+", "", example["text"])  # Remove URLs
    example["text"] = re.sub(
        r"[^\w\s]", "", example["text"]
    )  # Remove special characters
    example["text"] = re.sub(
        r"\b[A-Za-z]+\b", "", example["text"]
    )  # Remove English words
    example["text"] = re.sub(
        r"\b[^\u0600-\u06FF\s]+\b", "", example["text"]
    )  # Remove non-Arabic words
    example["text"] = re.sub(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", example["text"]
    )  # Remove emails
    example["text"] = re.sub(
        r"\b\d{10,15}\b", "", example["text"]
    )  # Remove phone numbers
    example["text"] = re.sub(r"\n+", "", example["text"])  # Replace multiple newlines
    example["text"] = re.sub(
        r"\s+", " ", example["text"]
    ).strip()  # Replace multiple spaces and strip
    return example


def apply_cleaning(ds):
    ds = ds.map(remove_emojis)
    ds = ds.map(clean_text)
    return ds
