import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

api_key = 'APY_KEY_AQUI'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_hardware_bot(mensagens_historico):
    contexto = (
        "Você é o 'HardwareBot', um especialista técnico em hardware e PC Gaming. "
        "Sua especialidade é otimização de airflow, configurações de fans ARGB e análise de performance "
        "em 1440p para setups com Ryzen 7 e GPUs da linha RX. "
        "Seja técnico, prestativo e use uma linguagem entusiasta de tecnologia."
    )
    
    mensagens_modelo = [('system', contexto)]
    mensagens_modelo += mensagens_historico
    
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

print("💻 HardwareBot: Sistema Online! Como posso ajudar no seu setup hoje? (Digite 'x' para sair)")
print("-" * 70)

historico_conversa = []

while True:
    pergunta = input('👤 Você: ')
    
    if pergunta.lower() == 'x':
        print("💻 HardwareBot: Encerrando... Boa jogatina!")
        break
    
    historico_conversa.append(('user', pergunta))
    
    try:
        resposta = resposta_hardware_bot(historico_conversa)
        historico_conversa.append(('assistant', resposta))
        
        print(f'\n💻 HardwareBot: {resposta}\n')
        print("-" * 70)
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        break
