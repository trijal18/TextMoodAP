import os
import json
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def analyze_sentiment(review_text):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                        f"Analyze the sentiment of the following review: '{str(review_text)}'. "
                        "Provide sentiment scores for positive, negative, and neutral in the following strict JSON format "
                        "without any extra text, explanations, or additional comments simply give ajson response no extra text, keep the total score to be 1:\n\n"
                        "{\"positive\": score, \"negative\": score, \"neutral\": score}"
                    )
            }
        ],
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content.strip()
    return json.loads(response)



# Example usage:
# review_text = ["bad","good","very good, love it"]
# sentiment_result = analyze_sentiment(review_text)
# print(sentiment_result)
