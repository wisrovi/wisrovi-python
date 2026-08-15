import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bot_engine import ChatEngine

def test_chatbot_respuestas():
    bot = ChatEngine("Asistente")
    r1 = bot.get_response("u1", "Quiero saber el precio")
    assert "$19/mes" in r1
    r2 = bot.get_response("u1", "Necesito soporte")
    assert "soporte@empresa.com" in r2
