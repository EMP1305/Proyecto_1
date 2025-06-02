# Nudelns Search Tool

Nudelns Search Tool is a text search utility based on cosine similarity over a database of Spanish documents. It uses TF-IDF and natural language processing to find the most relevant documents according to the user's query.

## Requirements

- Python 3.x
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- [nltk](https://www.nltk.org/)

You can install the dependencies by running:

```sh
pip install scikit-learn pandas nltk
```

## Instructions

### Processing the Database

1. Place your documents in the `Db` folder located in the same directory as the search tool.
2. Run `DB_reader.py` to process the documents and generate the `db.pickle` file.
    - Make sure the path to the `Db` folder is correct in the script.

### Performing a Search

1. Run `Nudelns.py` to start the search tool.
2. Enter your query when prompted.
3. The tool will display the most relevant documents based on cosine similarity.

### File Structure

- `DB_reader.py`: Processes the documents and creates the serialized database.
- `Nudelns.py`: Main interface for performing searches.
- `Language_processing.py`: Functions for text processing.
- `cos_sim.py`: Implementation of the cosine similarity algorithm.

> **Note:** Make sure to run `DB_reader.py` every time you add or modify documents in the `Db` folder.

