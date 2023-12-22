from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load pre-trained T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def tagline_gen(input_text, model, tokenizer):
    input_text = "generate a tagline: " + input_text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text
    output = model.generate(
        input_ids,
        max_length=50,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.5,
        length_penalty=0.8,
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
