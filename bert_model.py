import torch
from transformers import BertTokenizer, BertForTokenClassification

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, num_labels=5)

# Fine-tune BERT for NER using your labeled dataset and training process

def predict_entities(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_labels = torch.argmax(logits, dim=2).squeeze().tolist()

    # Map label indices to entity labels using the model's configuration
    predicted_entities = [model.config.id2label[label_id] for label_id in predicted_labels]

    # Extract entities from the text
    entities = []
    current_entity = None
    for token, entity_label in zip(tokenizer.tokenize(text), predicted_entities):
        if entity_label.startswith("B"):
            if current_entity:
                entities.append(current_entity)
            current_entity = {"start": len(entities), "end": len(entities) + 1, "label": entity_label[2:]}
        elif entity_label.startswith("I") and current_entity:
            current_entity["end"] += 1
        else:
            if current_entity:
                entities.append(current_entity)
                current_entity = None

    return entities

# Example usage
input_text = "Apple Inc. is a technology company."
entities = predict_entities(input_text, model, tokenizer)
print("Predicted Entities:", entities)
