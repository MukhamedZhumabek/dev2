import datetime
from typing import Mapping, NoReturn

from sqlalchemy import func, insert
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from storage.base import Base
from storage.base import async_session


class AwesomeData(Base):
    __tablename__ = "awesome_data"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data: Mapped[str] = mapped_column(index=True)
    control_sum: Mapped[str] = mapped_column(index=True, unique=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    def __repr__(self):
        return f'AwesomeData id: {self.id} data: {self.data} control_sum: {self.control_sum}'


async def insert_new_question(data: Mapping[str, str]) -> None:
    async with async_session() as session:
        stm = insert(AwesomeData).values(**data)
        await session.execute(stm)
        await session.commit()
