def get_email_text():
    """
    Prompt the user to paste the original email text.

    Returns:
        str: The email text entered by the user.
    """
    email = input("Paste the incoming email text:\n")
    return email.strip()


def get_bullet_points():
    """
    Prompt the user to enter key bullet points (comma-separated).

    Returns:
        list[str]: A list of cleaned bullet points.
    """
    raw_points = input("Enter key points (comma-separated):\n")
    # Split by commas, strip whitespace, and filter out empty strings
    points = [p.strip() for p in raw_points.split(",") if p.strip()]
    return points


def choose_tone():
    """
    Prompt the user to choose a tone for the reply.

    Returns:
        str: The chosen tone string ("formal", "friendly", "concise", "detailed").
    """
    print("\nChoose the tone of the reply:")
    print("1. Formal")
    print("2. Friendly")
    print("3. Concise")
    print("4. Detailed")

    choice = input("Enter choice (1-4): ").strip()
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

    Args:
        email_text (str): The original email text.
        bullet_points (list[str]): List of key points to include.
        tone (str): The chosen tone for the reply.

    Returns:
        str: The formatted prompt string.
    """
    return (
        f"Draft a professional email reply in a {tone} tone based on the following.\n"
        f"Original email: \"{email_text}\"\n"
        f"Key points to include: {bullet_points}\n"
        f"Reply:"
    )


if __name__ == "__main__":
    # Get the original email text from the user
    email_text = get_email_text()

    # Get bullet points from the user
    bullet_points = get_bullet_points()

    # Get the desired reply tone
    tone = choose_tone()

    # Build the final prompt
    prompt = build_prompt(email_text, bullet_points, tone)

    # Display the generated prompt
    print("\nGenerated prompt:\n", prompt)
