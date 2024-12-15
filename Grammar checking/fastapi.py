from fastapi import FastAPI
from language_tool_python import LanguageTool

app = FastAPI()
tool = LanguageTool("en-US")

def calculate_severity(matches):
    severity = 0
    for match in matches:
        if "punctuation" in match.ruleId.lower():
            severity += 1 
        elif "spelling" in match.ruleId.lower():
            severity += 0.7 
        else:
            severity += 0.5 

    return severity

@app.get("/grammar")
def grammar_score(sentence: str):
    matches = tool.check(sentence)

    # Count of errors in the sentence
    error_count = len(matches)
    
    # Function to calculate severity of the errors (example placeholder logic)
    severity = calculate_severity(matches) 

    # Calculate the base score (errors/maximum errors)
    max_errors = 30 
    base_score = max(0, 1 - (error_count / max_errors))  # Ensures score is not negative

    # Penalty based on error severity (adjusting for severity)
    severity_penalty = min(1, severity / 10) 

    # Sentence length factor (ensuring we do not penalize excessively long sentences)
    sentence_length = len(sentence.split())
    max_length = 50
    length_factor = min(1, sentence_length / max_length)

    # Calculate final score combining the base score, severity, and length factor
    score = base_score - severity_penalty
    score = score * length_factor  # Apply length factor to final score

    # Ensure the final score is clamped between 0 and 1
    return round(max(0, min(1, score)), 2)  # Ensures the score stays between 0 and 1