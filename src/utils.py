from fasttext.FastText import _FastText


def language_filter(ds):
    model = _FastText("lid.176.bin")

    def is_darija(x):
        language, score = model.predict(x["text"].replace("\n", ""))
        language = language[0].split("__")[2]
        return score > 0.4 and language == "ar"

    ds = ds.filter(is_darija, load_from_cache_file=False, num_proc=1)
    return ds


def export_dataset(ds, output_path):
    ds.to_csv(output_path, index=False)
