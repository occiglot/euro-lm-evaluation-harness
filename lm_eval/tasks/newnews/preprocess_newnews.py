"""
Adapted from `wikitext/preprocess_wikitext.py`
"""

import re


def process_results(doc, results):
    (loglikelihood,) = results
    # IMPORTANT: task counts number of words in *original doc before detokenization*
    _words = len(re.split(r"\s+", doc["cleaned_text"]))
    _bytes = len(doc["cleaned_text"].encode("utf-8"))
    return {
        "word_perplexity": (loglikelihood, _words),
        "byte_perplexity": (loglikelihood, _bytes),
        "bits_per_byte": (loglikelihood, _bytes),
    }
