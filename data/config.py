from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token
ADMINS = list(map(int,env.list("ADMINS")))  # adminlar ro'yxati
MY_GROUP = env.int("MY_GROUP")