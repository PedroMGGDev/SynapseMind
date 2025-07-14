
from SynapseMind.core.llm_interface import chat_with_openai
from SynapseMind.core.memory_manager import create_table, save_message, get_chat_history
from SynapseMind.core.semantic_memory import add_to_memory, search_memory

def chat(user_input):
    create_table()
    save_message("user", user_input)
    history = get_chat_history()
    relevant = search_memory(user_input)

    messages = [{"role": "system", "content": "Você é um assistente inteligente."}]
    messages += [{"role": role, "content": content} for role, content in history]
    if relevant:
        messages.insert(1, {"role": "system", "content": f"Contexto adicional:\n{', '.join(relevant)}"})

    response = chat_with_openai(messages)
    save_message("assistant", response)
    add_to_memory(user_input)
    return response

if __name__ == "__main__":
    while True:
        user = input("Você: ")
        if user.lower() in ["sair", "exit", "quit"]:
            break
        resposta = chat(user)
        print("SynapseMind:", resposta)
