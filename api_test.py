import requests
import base64

prompt = "young Lucy Lawless as Xena"
url = "https://4923-34-90-128-254.ngrok.io/generate-image"

payload = {
    "prompt": prompt
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    generated_image_base64 = data['generated_image']
    with open(f"{prompt}.png", "wb") as f:
        f.write(base64.b64decode(generated_image_base64.split(",")[1]))
else:
    print(f"Request failed with status code {response.status_code}")
