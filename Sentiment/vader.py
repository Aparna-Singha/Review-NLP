from fastapi import FastAPI, HTTPException
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize FastAPI app and Sentiment Analyzer
app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment score
def get_sentiment_score(text: str):
    try:
        # Get sentiment scores
        sentiment = analyzer.polarity_scores(text)
        
        # Extract the compound score, which is the most useful for overall sentiment
        compound_score = sentiment['compound']
        
        # Convert the compound score from [-1, 1] to [0, 1]
        # This scales -1 -> 0 and 1 -> 1, with values in between mapped linearly
        normalized_score = (compound_score + 1) / 2

        return round(normalized_score, 2)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {e}")

# FastAPI endpoint to process text and return sentiment score
@app.get("/sentiment")
def analyze_sentiment(text: str):
    score = get_sentiment_score(text)
    return score
