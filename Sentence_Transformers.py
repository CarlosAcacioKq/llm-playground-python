from sentence_transformers import SentenceTransformer, util

# Measure how similar two sentences are using semantic embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode("A man is eating food.")
embedding2 = model.encode("A person is having a meal.")
similarity = util.cos_sim(embedding1, embedding2)

print("Similarity Score:", similarity.item())
