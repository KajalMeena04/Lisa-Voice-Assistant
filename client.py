import google.generativeai as genai

genai.configure(api_key="")# add api_key here

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content("What is coding?")
print(response.text)

