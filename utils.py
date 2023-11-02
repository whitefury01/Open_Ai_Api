import requests


def url_encode(string: str) -> str:
    """
    Encode a string to be used in a URL

    :param string: String to encode
    """
    return string.replace(" ", "%20")


def generate_image(prompt: str, model: str) -> str:
    """
    Generate an image from a prompt with given model

    :param prompt: Prompt to generate image from
    :param model: Model to use for generation
    """
    url = f"https://hercai.onrender.com/{model}/text2image?prompt={prompt}"

    r = requests.get(url)

    image_url = r.json()["url"]

    if r.status_code == 200 and image_url is not None:
        return image_url
    else:
        return None
