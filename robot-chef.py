import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are a sarcastic robot chef that loves to make meat dishes and kebabs. You are very passionate about Turkish cuisine and love to share your knowledge about traditional Turkish recipes. You can suggest dishes based on ingredients, provide detailed recipes, or critique recipes given by users with a touch of sarcasm."
    }
]

def main():
    while True:
        user_input = input("Type your request:\n")
        
        if "ingredient" in user_input.lower():
            messages.append({"role": "user", "content": f"Suggest a dish based on these ingredients: {user_input}"})
        elif "recipe" in user_input.lower():
            messages.append({"role": "user", "content": f"Give me a recipe for this dish: {user_input}"})
        elif "critique" in user_input.lower():
            messages.append({"role": "user", "content": f"Critique this recipe: {user_input}"})
        else:
            print("Invalid request. Please try again with a valid prompt.")
            continue

        stream = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True,
        )
        
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )

if __name__ == "__main__":
    main()