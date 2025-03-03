import typing as tp
from contextlib import contextmanager
import typing_extensions as te

import neo4j

from config import settings


class Neo4jConnectionHelper:
    _session: neo4j.Session

    def __init__(self, db_url: str, user: str, password: str) -> None:
        self._driver = neo4j.GraphDatabase.driver(
            uri=db_url,
            auth=(user, password),
        )

    @contextmanager
    def session(self, db: str = settings.db_name) -> tp.Generator[tp.Self, tp.Any, None]:
        try:
            self._session = self._driver.session(database=db)
            yield self

        finally:
            self._session.close()

    def execute(self, query: te.LiteralString, **params: tp.Any) -> list[dict[str, tp.Any]]:
        result = self._session.run(query, params)
        return result.data()
