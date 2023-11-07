import logging

from dotenv import dotenv_values

logging.basicConfig(
    level=logging.INFO,
    filename="./log/dev2.log",
    format="%(asctime)s - %(levelname)s - %(module)s  - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

# ==postgres== #
DB = dotenv_values('.env.postgres')
POSTGRES_USER = DB["POSTGRES_USER"]
POSTGRES_PASSWORD = DB["POSTGRES_PASSWORD"]
POSTGRES_HOST = DB["POSTGRES_HOST"]
POSTGRES_PORT = DB["POSTGRES_PORT"]
POSTGRES_DB = DB["POSTGRES_DB"]
sqlalchemy_url = (f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
                  f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')

# ==rabbitmq== #
rabbit_settings = dotenv_values('.env.rabbit')
RABBITMQ_CONSUME_QUEUE = rabbit_settings['RABBITMQ_CONSUME_QUEUE']
RABBITMQ_HOST = rabbit_settings['RABBITMQ_HOST']
RABBITMQ_USER = rabbit_settings['RABBITMQ_USER']
RABBITMQ_PASSWORD = rabbit_settings['RABBITMQ_USER']
RABBITMQ_URL = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}'
