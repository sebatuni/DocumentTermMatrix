import math

class DocumentTermMatrix:
    """
    A simple implementation of a Document-term matrix builder.
    Various methods for calculating term frequency (tf) are implemented,
    including normal tf calculations with addition to idf (inverse document frequency)
    and tf-idf (term frequency-inverse document frequency).
    """
    def __init__(self):
        self.dtm = []


    """ Word is in document """
    def binary(self, X, word):
        try:
            for doc in self.dtm:
                if doc[0] == X:
                    if word not in doc[1]:
                        return 0
                    else:
                        return 1
            raise ValueError("Document doesn't exist.")
        except ValueError as e:
            print('Error:', e)
            return 0


    """ Term frequency calculation using raw count """
    def tf(self, X, word):
        try:
            for doc in self.dtm:
                if doc[0] == X:
                    if word not in doc[1]:
                        return 0
                    else:
                        return doc[1][word] / doc[2]
            raise ValueError("Document doesn't exist.")
        except ValueError as e:
            print('Error:', e)
            return 0


    """ Term frequency calculation using raw count """
    def log_tf(self, X, word):
        try:
            for doc in self.dtm:
                if doc[0] == X:
                    if word not in doc[1]:
                        return 0
                    else:
                        return math.log(1 + doc[1][word])
            raise ValueError("Document doesn't exist.")
        except ValueError as e:
            print('Error:', e)
            return 0


    """
        Augmented Term frequency calculation:
        Calculate the augemented term frequency of
        a given word. Prevents a bias towards longer documents,
        e.g. raw frequency divided by the raw frequency of the most occurring term in the document
    """
    def augemented_tf(self, X, word):
        try:
            for doc in self.dtm:
                if doc[0] == X:
                    if word not in doc[1]:
                        return 0
                    else:
                        return 0.5 + 0.5 * (doc[1][word] / max(doc[1].values()))
            raise ValueError("Document doesn't exist.")
        except ValueError as e:
            print('Error:', e)
            return 0


    """ Inverse Document Frequency calculation """
    def idf(self, word):

        docs_containing = 0
        for doc in self.dtm:
            if word in doc[1]:
                docs_containing += 1
        # Return the total number of documents divided by
        # number of documents containing the given word
        return len(self.dtm) / docs_containing


    """ Term Frequency-Inverse Document Frequency calculation """
    def tf_idf(self, X, word):
        # NOTE: Haven't looked at the different calculations
        # for this in terms of weights
        idf = self.idf(word)
        tf = self.tf(X, word)
        return tf * idf

    """ Calculate term frequency of given document """
    def read_document(self, X):
        word_count = 0
        try:
            with open(X, 'r') as f:
                doc = dict()
                for line in f:
                    line = line.rstrip()
                    word = ''
                    for c in line:
                        if c.isalpha():
                            word += c.lower()
                        elif c == ' ':
                            if word == '':
                                continue
                            # Random one letter words in some datasets
                            elif len(word) == 1 and word != 'a':
                                continue

                            # Count word occurence in the doc dictionary
                            if word not in doc:
                                doc[word] = 1
                            else:
                                doc[word] += 1

                            word_count += 1
                            word = ''

                # Add processed document to dtm
                self.dtm.append((X, doc, word_count))
        except FileNotFoundError as e:
            print('Error:', e)
        except UnicodeDecodeError as e:
            print('Error:', '[', X, ']', e)

    """ Display all terms and frequencies of a given document. """
    def print_document(self, X):
        for doc in self.dtm:
            if doc[0] == X:
                print([(k, doc[1][k]) for k in sorted(doc[1], key=doc[1].get, reverse=True)])
