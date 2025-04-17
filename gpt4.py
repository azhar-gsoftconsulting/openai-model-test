import openai
import time
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Parameters
model_name = "gpt-4"  # Change this to test other models
test_prompt = "Explain how machine learning works in simple terms"

def test_model(model, prompt):
    start_time = time.time()

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    end_time = time.time()
    elapsed_time = end_time - start_time
    response_text = response.choices[0].message["content"].strip()

    return response_text, elapsed_time

# Run test
output, duration = test_model(model_name, test_prompt)

# Print results
print(f"\nModel: {model_name}")
print(f"Response Time: {duration:.2f} seconds")
print(f"Output:\n{output}")
