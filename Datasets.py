from datasets import load_dataset

# Load 5 samples from the IMDB movie reviews dataset 
dataset = load_dataset("imdb", split="train[:5]")

for example in dataset:
    print("Text:", example["text"])
    print("Label:", example["label"])
