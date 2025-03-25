import openai

openai.api_key = ""  

def analyze_stock(price):
    prompt = f"The stock price is {price}. Should I buy, sell, or hold?"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error with AI analysis: {e}")
        return "Unable to analyze stock trends at the moment."
