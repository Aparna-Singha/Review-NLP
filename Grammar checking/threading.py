import pandas as pd
import language_tool_python
from time import perf_counter_ns
from concurrent.futures import ThreadPoolExecutor

df = pd.read_csv("reviews.csv")


time1= perf_counter_ns()
tool = language_tool_python.LanguageTool('en-US')
def calculate_grammar_score(sentence):
    
    matches = tool.check(sentence)
    # Total issues detected
    error_count = len(matches)
    
    # Normalize score: Assume 5 errors = score 1, and no errors = score 10
    max_errors = 15  # Threshold for poorest grammar
    if error_count == 0:
        score = 10
    elif error_count >= max_errors:
        score = 1
    else:
        score = 10 - (error_count * (10 / max_errors))  # Linear scale
    
    return max(1, min(10, round(score)))

# Test sentence

def pool():
    with ThreadPoolExecutor(max_workers=16) as executor:
        text_data = [df['Text'][i] for i in range(6)]
            # Map the function across the text data
        scores = list(executor.map(calculate_grammar_score, text_data))
        count = 0
    for score in scores:
        print(f"grammar score {score/10}")
        count=count+1
    print(count)
pool()
time2 = perf_counter_ns()
print(time2-time1)