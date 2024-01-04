from gensim.models import Word2Vec

# Sample corpus (list of sentences)
corpus = [
    ["The", "early", "bird", "gets", "the", "worm"],
    ["Success", "requires", "hard", "work"]
]

# Train Word2Vec model on the corpus
model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, sg=0)
model.save("Section-7-word2vec_model.bin")
