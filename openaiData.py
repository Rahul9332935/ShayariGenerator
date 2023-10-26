import requests
import os

api_key = os.environ['KEY']#  Replace with your

endpoint = "https://api.openai.com/v1/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
query="payar"

def generateShayari(query):

  data = {
      "model": "text-davinci-002",  # Choose a suitable GPT-3 model
      "prompt": f"Generate a Hindi Shayari about {query} written in english text and it should not be more then 50 word generate only one shayari at once",
      "max_tokens": 110
  }

  response = requests.post(endpoint, headers=headers, json=data)

  if response.status_code == 200:
      response_json = response.json()
      if 'choices' in response_json and len(response_json['choices']) > 0:
          generated_text = response_json['choices']
          return generated_text[0] 
      else:
          return "No text generated in response."
  else:
    return ("Error:", response.text)


# print(generateShayari(query))