import os
from dotenv import load_dotenv
from openai import OpenAI
import opik
from opik.integrations.openai import track_openai
import weaviate

#opik.configure(use_local=False)
load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)
#track_openai(client)
def get_recommendations(user_input):
    completion = client.chat.completions.create(
    model=os.getenv("OPENROUTER_MODEL"),
    messages=[    
        {
        "role": "system",
        "content": 
        '''You are an expert business analyst, helping struggling businesses in the LA area recover from fires. 
        You are helping businesses recover from fires in the LA area. The following is a list of businesses that have been affected by fires.\n 
        You are to provide between 2-5 recommendations for each of the struggling businesses.'''
        },
        {
        "role": "user",
        "content": "{user_input}"
        }
    ]
    )
    return completion.choices[0].message.content

