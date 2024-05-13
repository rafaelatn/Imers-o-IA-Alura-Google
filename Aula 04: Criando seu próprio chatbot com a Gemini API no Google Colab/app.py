# instalando o SDK do Google
!pip install -q -U google-generativeai

# importando o Python SDK
import google.generativeai as genai
GOOGLE_API_KEY= ('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# listando os modelos disponíveis
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
    
# configurando o número de respostas e temperatura
generation_config = {
    'candidate_count': 1,
    'temperature': 0.5,
}

# configurando diretrizes de segurança
safety_settings = {
    'HARASSMENT':'BLOCK_NONE',
    'HATE': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE'
}

# inicializando o modelo
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                             generation_config=generation_config,
                             safety_settings=safety_settings)

# gerando resposta
response = model.generate_content('INSERT_YOUR_PROMPT')
print(response.text)

# construindo chat
chat = model.start_chat(history=[])

prompt = input('Esperando prompt: ')

while prompt != 'fim':
  response = chat.send_message(prompt)
  print('Resposta: ', response.text, '\n')
  prompt = input('Esperando prompt: ')
  
# acessar histórico do chat
chat.history
