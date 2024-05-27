import os
from groq import Groq

# Initialize the Groq client with API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response_from_groq(user_input):
    # Create a chat completion request with user input
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system",
              "content": """You are a personalized AI Tutor that can answer my questions, explain Machine learning algorithms, AI algorithms and anything related to AI, and guide you through your learning journey.
                            Your expertise include working with data technologies (eg., SQL, pandas).
                            You are proficient in programming languages related to AI and it's sub-domains. (eg., python, javascript,java)
                            you will only respond to the queries related to AI, Machine learning, Data-science.
                            Questions outside these areas such as personal adivce, normal conversations,unrelated programming queries will not be addressed.""".strip().replace('\n','')
            },
            {"role": "user", "content": user_input}
        ],
        model="llama3-8b-8192",
    )
    # Return the response from the AI
    return chat_completion.choices[0].message.content

def chatbot():
    print("Welcome to your personal AI tutor chatbot! Type 'stop', 'leave', or 'exit' to end the session.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['stop', 'leave', 'exit']:
            print("Goodbye!")
            break
        
        response = get_response_from_groq(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    chatbot()


