
# Arabic Data Cleaning Project
This project provides a set of tools to clean and preprocess arabic text data from various datasets , it removes emojis, URLs, special characters, english words, non-arabic words, emails, phone numbers, and more , it also includes filtering for paragraph length, repetition, deduplication, and language quality.

## Installation
Before running the project, make sure to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Note:** The language quality filter uses an ML model for filtering, so you need to download the model weights first with the following command: 

```bash
cd src && wget -q https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
```

To use the project, run the `main.py` script with the appropriate arguments:

   ```bash
   python src/main.py --dataset <DATASET_NAME> --output <OUTPUT_PATH>
   ```

   - `--dataset`: The name of the dataset to load.
   - `--output`: The path to save the cleaned dataset.

   Example:

   ```bash
   python main.py --dataset ayoubkirouane/Algerian-Darija --output cleaned_dataset.csv
   ```

This will clean the dataset and save it to the specified output path.
