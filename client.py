import google.generativeai as genai

genai.configure(api_key="AIzaSyAj-ehLHpkGRDDFhdocSnf3GlT_39i26xg")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content("What is coding?")
print(response.text)

