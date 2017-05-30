# python-BM25
Python rank function for an Sqlite full text search based using the Okapi BM25 formula. 

## Assumptions
This function assumes that buf = matchinfo(fts_table, 'pcxnals') and that your full-text table has only two columns: (1) a document id type column and (2) search text body column.
