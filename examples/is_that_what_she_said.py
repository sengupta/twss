import twss

sentance = "It's too hard"
print sentance, twss.is_positive(sentance), twss.how_confident(sentance)

sentance = "London 2012"
print sentance, twss.is_positive(sentance), twss.how_confident(sentance)
