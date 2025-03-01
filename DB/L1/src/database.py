import typing as tp

import aiomysql


class DBHelper:
    connection: aiomysql.connection.Connection

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        db: str,
    ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    async def __aenter__(self) -> tp.Self:
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._close()

    async def _connect(self) -> None:
        self.connection = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset="utf8mb4",
            cursorclass=aiomysql.cursors.DictCursor,
        )

    async def _close(self) -> None:
        self.connection.close()

    async def execute(self, query: str) -> list[dict[str, tp.Any]]:
        async with self.connection.cursor() as cur:
            await cur.execute(query)
            result = await cur.fetchall()
            return result or []
