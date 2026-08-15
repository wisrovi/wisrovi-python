"""Motor de Chatbot con Memoria de Sesión."""

class ChatEngine:
    def __init__(self, bot_name: str):
        self.bot_name = bot_name
        self.conversations = {}

    def get_response(self, user_id: str, message: str) -> str:
        if user_id not in self.conversations:
            self.conversations[user_id] = []
        
        self.conversations[user_id].append({"user": message})
        
        # Lógica de respuesta inteligente / FAQ
        msg_lower = message.lower()
        if "precio" in msg_lower or "costo" in msg_lower:
            reply = "Nuestros planes comienzan desde $19/mes con soporte prioritario."
        elif "contacto" in msg_lower or "soporte" in msg_lower:
            reply = "Puedes escribirnos a soporte@empresa.com o llamarnos al +34 900 123 456."
        else:
            reply = f"Hola, soy {self.bot_name}. ¿En qué más puedo orientarte hoy?"
            
        self.conversations[user_id].append({"bot": reply})
        return reply

if __name__ == "__main__":
    bot = ChatEngine("SoporteBot")
    print(bot.get_response("user1", "Hola, cuál es el precio?"))
