def rank_score(buf):
    if isinstance(buf, bytes):
        k1 = 1.2
        b = 0.75

        bufsize = len(buf)  # Length in bytes.
        match_info = [struct.unpack('@I', buf[i:i+4])[0] for i in range(0, bufsize, 4)]
        score = 0.0
        p, c = match_info[:2]           # p = number of matchable phrases in the query.
                                        # c = number of user-defined columns on the FTS table
        end_of_x = 3*c*p+2
        x = match_info[2:end_of_x]      # x =

        n = match_info[end_of_x]        # the number of rows in the table
        a = match_info[end_of_x+2]      # for the body column, the average number of tokens that are stored.
        l = match_info[end_of_x+4]      # for the body column, the length of the value stored in the current row (in tokens).
        # s = match_info[-1]            # the length of the longest subsequence of phrase matches that the column value
                                        # has in common with the query text.

        frequency_index = 3                       # the term frequency of the first term in the body column (2)
        for phrase_num in range(p):
            term_freq = x[frequency_index]
            # hits_all_rows = x[frequency_index+1]
            docs_with_hits = x[frequency_index+2]
            frequency_index += 6

            inverse_freq_score = log((n-docs_with_hits+0.5)/docs_with_hits+0.5)
            freq_score = (term_freq * (k1+1)) / (term_freq+k1*(1-b+b*(a/l)))
            score += (inverse_freq_score*freq_score)

        return round(score, 3)
    else:
        return None
