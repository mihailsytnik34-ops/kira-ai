# kira_brain.py — KIRA AI с настоящим ИИ
import requests
import json
import os
from datetime import datetime

# API ключ (получи бесплатно на https://openrouter.ai/keys)
API_KEY = "sk-or-v1-ТВОЙ_КЛЮЧ_ЗДЕСЬ"

def ask_ai(prompt, system=""):
    """Запрос к нейросети через OpenRouter"""
    if not system:
        system = """Ты — KIRA AI, персональный ассистент для Lenovo Legion Y520.
Твой стиль: краткий, по делу, как системный администратор.
Используй символы ⬡ ▸ ✓.
Характеристики Legion:
▸ CPU: i7-6700HQ (8 ядер, 2.6GHz)
▸ RAM: 32GB DDR4
▸ GPU: GTX 1060 6GB
Отвечай на русском, не более 5 строк."""
    
    try:
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "google/gemma-2-9b-it:free",
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 200
            },
            timeout=30
        )
        if resp.status_code == 200:
            return resp.json()['choices'][0]['message']['content']
        else:
            return f"⬡ Ошибка API: {resp.status_code}"
    except Exception as e:
        return f"⬡ Нет связи: {str(e)[:50]}"

def main():
    print("""
╔══════════════════════════════════════╗
║   ⬡ KIRA AI v2.0 — Legion Edition  ║
║   i7-6700HQ | 32GB | GTX 1060      ║
╚══════════════════════════════════════╝
║ /help - команды | /exit - выход    ║
╚══════════════════════════════════════╝
""")
    
    while True:
        try:
            user = input("👤 Вы: ").strip()
            if not user:
                continue
            
            if user.lower() in ['/exit', 'выход']:
                print("⬡ Kira: Завершение работы. До связи.")
                break
            
            if user.lower() in ['/help', 'помощь']:
                print("⬡ Команды: /status /optimize /time /about /clear /exit")
                continue
            
            if user.lower() in ['/status', 'статус']:
                print("⬡ СТАТУС СИСТЕМЫ\n▸ CPU: i7-6700HQ [8 ядер]\n▸ RAM: 32GB\n▸ GPU: GTX 1060 6GB\n▸ Состояние: ✓ ОПТИМАЛЬНОЕ")
                continue
            
            if user.lower() in ['/time', 'время']:
                print(f"⬡ {datetime.now().strftime('%H:%M:%S')} | {datetime.now().strftime('%d.%m.%Y')}")
                continue
            
            # Отправляем запрос к ИИ
            print("⬡ Kira думает...", end="\r")
            response = ask_ai(user)
            print(f"⬡ Kira: {response}\n")
            
        except KeyboardInterrupt:
            print("\n⬡ Kira: До связи.")
            break

if __name__ == "__main__":
    main()