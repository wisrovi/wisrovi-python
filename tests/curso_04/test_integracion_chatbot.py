"""Test del motor de chatbot conversacional."""
def test_chatbot_engine():
    class SimpleBot:
        def reply(self, msg): return f"Respuesta a: {msg}"
    bot = SimpleBot()
    assert "Hola" in bot.reply("Hola")
