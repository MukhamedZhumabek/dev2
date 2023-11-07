import asyncio
import json
from logging import getLogger

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage

import settings
from storage.models import insert_new_question

logger = getLogger(__name__)


async def on_message(message: AbstractIncomingMessage) -> None:
    data: dict[str, str] = json.loads(message.body)
    logger.info(f'Got message: {data}')
    await insert_new_question(data)


async def listen() -> None:
    connection = await connect(settings.RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(settings.RABBITMQ_CONSUME_QUEUE)
        await queue.consume(on_message, no_ack=True)
        logger.info("Consumer waiting for messages...")
        await asyncio.Future()
