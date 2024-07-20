import argparse

from src.cleaning import apply_cleaning, load_data
from src.filtering import apply_filtering
from src.utils import export_dataset, language_filter


def main():
    parser = argparse.ArgumentParser(description="Clean and export dataset.")
    parser.add_argument(
        "--dataset", type=str, required=True, help="Name of the dataset to load."
    )
    parser.add_argument(
        "--output", type=str, required=True, help="Path to save the cleaned dataset."
    )
    args = parser.parse_args()

    print("Loaading dataset...")
    ds = load_data(args.dataset)
    print("Cleaning dataset...")
    ds = apply_cleaning(ds)
    print("Filtering dataset...")
    ds = apply_filtering(ds)
    print("Filtering dataset by language...")
    ds = language_filter(ds)
    print("Exporting dataset...")
    export_dataset(ds, args.output)
    print("Dataset cleaned and exported successfully.")


if __name__ == "__main__":
    main()
