import typing as tp
from contextlib import contextmanager
import typing_extensions as te

import neo4j


class Neo4jConnectionHelper:
    _connection: neo4j.Driver

    def __init__(
        self,
        db_url: str,
        user: str,
        password: str
    ) -> None:
        self._db_url = db_url
        self._user = user
        self._password = password

    @contextmanager
    def connect(self) -> tp.Generator[tp.Self, tp.Any, None]:
        try:
            self._connection = neo4j.GraphDatabase.driver(
                uri=self._db_url,
                auth=(self._user, self._password),
            )
            yield self

        finally:
            self._connection.close()

    def execute(self, query: te.LiteralString, **params: tp.Any) -> list[dict[str, tp.Any]]:
        with self._connection.session() as session:
            result = session.run(query, params)
            return result.data()
