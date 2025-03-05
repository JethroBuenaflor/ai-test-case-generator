import os
import base64
from openai import OpenAI
from pprint import pprint

AI_MODEL = "gpt-4o"
# ROLE = "You are a Software Quality Assurance Engineer, skilled in finding bugs in mobile and web applications and able to formulate several test cases in minimal scenarios"
IMAGES_PATH = "./images"
ROLE = "You are a data encoder, skilled in scanning an image and wirtes data that is seen in the image."


def scan_images(prompt):
    client = OpenAI()

    print("Scanning signature images...")
    completion = client.chat.completions.create(model=AI_MODEL, messages=prompt)

    response = completion.choices[0].message.content

    save_response(response)


def save_response(response):
    f = open("timestamps.csv", "a")
    f.write(response)
    f.close()

    f = open("timestamps.csv", "r")

    print("Signature Timestamp Created!")


def generate_role(role_description):
    """
    Generates the role that ChatGPT would assume

    Example:
    {
        "role": "system",
        "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
    }
    """
    return {"role": "system", "content": role_description}


def generate_asks(asks):
    """
    Generates the askings
    """
    askings = []

    for ask in asks:
        askings.append({"type": "text", "text": ask})

    return askings


def generate_user_content(askings, image_contents):
    content = askings + image_contents

    user_content = {"role": "user", "content": content}

    return user_content


def generate_prompt(role_description, asks, image_paths):
    image_contents = []
    prompt = []

    role = generate_role(role_description)
    askings = generate_asks(asks)

    for index, image_path in enumerate(image_paths):
        print(image_path.split("/")[-1])
        base64_image = encode_image(image_path)
        image_contents.append(
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            }
        )
        askings.append(
            {
                "type": "text",
                "text": f"Image {index + 1} filename: " + image_path.split("/")[-1],
            }
        )

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
        "Write the timestamp that is seen in the lower left part of the image that is in grey background",
        "Write the data in csv format with filename of the image, and timestamp data",
    ]
    image_directory = IMAGES_PATH

    image_paths = get_image_paths(image_directory)
    prompt = generate_prompt(role_description, asks, image_paths)
    scan_images(prompt)


if __name__ == "__main__":
    main()
