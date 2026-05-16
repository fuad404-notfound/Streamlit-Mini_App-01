from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")
# initailizing a client
client = genai.Client(api_key= my_api_key)
# note generator 
def ans_generator(text):
    prompt = """Give a short description of the question . Answer the question.
    make sure to add necessary markdown to 
    differenciate different section. everything is in 100 words max."""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents= f"{prompt}\n\nQuestion: {text}")
    
    return response.text