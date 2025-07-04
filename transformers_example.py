from transformers import pipeline

# Generate text continuation using GPT-2, a pretrained language model
generator = pipeline("text-generation", model="gpt2")
output = generator("Once upon a time,", max_length=30, num_return_sequences=1)

print("Generated Text:", output[0]["generated_text"])
