# DocumentTermMatrix

A simple implementation of a Document-term matrix builder. Various methods for calculating term frequency (tf) are implemented, including normal tf calculations with addition to idf (inverse document frequency) and tf-idf (term frequency-inverse document frequency) calculations.

Example usage:
```python3
from DocumentTermMatrix import *

dtm = DocumentTermMatrix()
dtm.read_document('./file')
```
