import telebot, random

API_TOKEN = 'YOUR API TOKEN'
bot = telebot.TeleBot(API_TOKEN)

def random_fact():
    """Генерирует случайный факт о сортировке мусора глобальном потеплении"""
    
    sorting_facts = [
🕜 Ускорение истории: Такое быстрое повышение температуры не наблюдалось как минимум последние 800 000 лет.




  
    ]
    
    return random.choice(sorting_facts)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши комманду /fact что бы увидеть рандомный факт о глобальном потеплении!")

@bot.message_handler(commands=['fact'])
def send_recycling_fact(message):
    fact = random_fact()
    bot.send_message(message.chat.id, fact)

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
