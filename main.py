import os
import base64
from openai import OpenAI
from pprint import pprint

AI_MODEL = "gpt-4o"
ROLE = "You are a Software Quality Assurance Engineer, skilled in finding bugs in mobile and web applications and able to formulate several test cases in minimal scenarios"
IMAGES_PATH = ".\images"


def generate_test_cases(prompt):
    client = OpenAI()

    print ("Creating Test Cases")
    completion = client.chat.completions.create(
        model=AI_MODEL,
        messages=prompt
    )

    response = completion.choices[0].message.content

    save_response(response)


def save_response(response):
    f = open("test-cases.txt", "a")
    f.write(response)
    f.close()

    f = open("test-cases.txt", "r")

    print ("Test Cases Created!")


def generate_role(role_description):
    """
    Generates the role that ChatGPT would assume

    Example:
    {
        "role": "system",
        "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
    }
    """
    return {
        "role": "system",
        "content": role_description
    }


def generate_asks(asks):
    """
    Generates the askings
    """
    askings = []

    for ask in asks:
        askings.append({
            "type": "text",
            "text": ask
        })

    return askings


def generate_user_content(askings, image_contents):
    content = askings + image_contents

    user_content = {
        "role": "user",
        "content": content
    }

    return user_content


def generate_prompt(role_description, asks, image_paths):
    image_contents = []
    prompt = []

    role = generate_role(role_description)
    askings = generate_asks(asks)

    for image_path in image_paths:
        base64_image = encode_image(image_path)
        image_contents.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })

    user_content = generate_user_content(askings, image_contents)

    prompt.append(role)
    prompt.append(user_content)

    return prompt


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_image_paths(directory):
    image_paths = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"): 
            image_paths.append(os.path.join(directory, filename))
            continue
        else:
            continue

    return image_paths


def main():
    role_description = ROLE
    asks = [
        "List atleast 20 test cases with steps to reproduce based on the provided images",
        "Group the test cases per uploaded image"
    ]
    image_directory = IMAGES_PATH

    image_paths = get_image_paths(image_directory)
    prompt = generate_prompt(role_description, asks, image_paths)
    generate_test_cases(prompt)


if __name__ == "__main__":
    main()