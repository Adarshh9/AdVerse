from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def tagline_gen(input_text, model, tokenizer):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text with modified parameters
    output = model.generate(
        input_ids,
        max_length=50,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=1,  # Adjust the temperature to control randomness (lower for more focused, higher for more creative)
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode and return the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Example usage
input_text = input("Enter your prompt: ")
tagline = tagline_gen(input_text, model, tokenizer)
print("Generated Tagline:", tagline)