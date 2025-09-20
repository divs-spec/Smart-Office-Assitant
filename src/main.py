from groq import Groq

def get_email_text():
    """
    Prompt the user to enter the incoming email text.
    """
    email_text = input("Paste the incoming email text: ")
    return email_text.strip()


def get_bullet_points():
    """
    Prompt the user to enter bullet points (comma-separated).
    """
    raw_input = input("Enter bullet points (comma-separated): ")
    points = [point.strip() for point in raw_input.split(",") if point.strip()]
    return points


def choose_tone():
    """
    Prompt the user to choose a tone for the email reply.
    """
    print("\nChoose a tone for the reply:")
    print("1. Formal")
    print("2. Friendly")
    print("3. Concise")
    print("4. Detailed")

    choice = input("Enter your choice (1-4): ").strip()
    tone_map = {
        "1": "formal",
        "2": "friendly",
        "3": "concise",
        "4": "detailed"
    }
    return tone_map.get(choice, "formal")


def build_prompt(email_text, bullet_points, tone):
    """
    Construct the final prompt string using all inputs.
    """
    bullet_str = ", ".join(bullet_points)
    prompt = (
        f"Draft a professional email reply in a {tone} tone based on the following.\n"
        f'Original email: "{email_text}"\n'
        f"Key points to include: {bullet_str}\n"
        f"Reply:"
    )
    return prompt


def generate_reply(prompt, api_key):
    """
    Send the prompt to the Groq LLM API and return the reply.
    """
    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_completion_tokens=512
    )

    reply = completion.choices[0].message.content.strip()
    return reply


if __name__ == "__main__":
    # Get inputs
    email_text = get_email_text()
    bullet_points = get_bullet_points()
    tone = choose_tone()

    # Build the prompt
    prompt = build_prompt(email_text, bullet_points, tone)

    # Helpful for debugging
    print("\nGenerated Prompt:\n", prompt)  

    # Get API key from user
    api_key = input("\nEnter your Groq API key: ")

    # Call Groq API
    try:
        reply = generate_reply(prompt, api_key)
        print("\nDrafted Reply:\n", reply)
    except Exception as e:
        print(f"Error: {e}")
