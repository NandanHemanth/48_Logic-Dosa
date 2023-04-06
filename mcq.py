import spacy
import random
import en_core_web_sm

nlp = en_core_web_sm.load()

# Example text
text = "The Mona Lisa is a half-length portrait painting by the Italian artist Leonardo da Vinci. It is one of the most famous paintings in the world and is housed in the Louvre Museum in Paris."

# Process the text with Spacy
doc = nlp(text)

# Generate MCQs based on named entities
for ent in doc.ents:
    if ent.label_ == 'PERSON':
        question = f"Who painted {ent.text}?"
        correct_answer = ent.text
        distractors = []
        for word in doc:
            if word.pos_ == 'NOUN' and word.text not in correct_answer and word.text not in distractors:
                similarity = word.similarity(ent)
                if similarity > 0.4 and similarity != 1:
                    distractors.append(word.text)

        options = [correct_answer] + distractors
        random.shuffle(options)
        print(question)
        for i, option in enumerate(options):
            print(f"{chr(i+65)}) {option}")

    elif ent.label_ == 'ORG':
        question = f"In which museum is {ent.text} located?"
        correct_answer = ent.text
        distractors = []
        for entity in doc.ents:
            if entity.label_ == 'GPE' and entity.text != correct_answer:
                distractors.append(entity.text)

        options = [correct_answer] + distractors
        random.shuffle(options)
        print(question)
        for i, option in enumerate(options):
            print(f"{chr(i+65)}) {option}")

    elif ent.label_ == 'GPE':
        question = f"In which city is {ent.text} located?"
        correct_answer = ent.text
        distractors = []
        for entity in doc.ents:
            if entity.label_ == 'ORG' and entity.text != correct_answer:
                distractors.append(entity.text)

        options = [correct_answer] + distractors
        random.shuffle(options)
        print(question)
        for i, option in enumerate(options):
            print(f"{chr(i+65)}) {option}")
