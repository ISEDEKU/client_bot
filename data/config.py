from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

PROMO_TEXT = env.str('PROMO_TEXT')
PROMO_CODES = env.list('PROMO_CODES')
