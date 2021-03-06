from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer 
from sumy.summarizers.biased_text_rank import BiasedTextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import sys
from imperative_detector import is_imperative
from question_detector import is_question
from conditional_detector import is_conditional


LANGUAGE = "english"
SENTENCES_COUNT = int(sys.argv[2])
text_file = sys.argv[1]


if __name__ == "__main__":
    parser = PlaintextParser.from_string('yo', Tokenizer(LANGUAGE))    
    parser = PlaintextParser.from_file(text_file, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    bias_functions_and_weights = [[is_imperative, 10.0], [is_question, 10.0], [is_conditional, 10.0]]
    summarizer = BiasedTextRankSummarizer(bias_functions_and_weights, stemmer)
    
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)

