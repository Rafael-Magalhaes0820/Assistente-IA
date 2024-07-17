from openai import OpenAI

# aparentemente o código está certo, o problema é que nao tenho grana pra pagar a API

client = OpenAI(api_key="colocar chave api aqui")

response = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a witty assistant, always answering with a joke"},
        {"role": "user", "content": "who are you?"}
]
)
if response.status_code == 200:
    # Processo de resposta bem-sucedida
    print(response.json())
else:
    # Erro na requisição
    print(f"Erro: {response.status_code}")

input('Press Enter to exit')
