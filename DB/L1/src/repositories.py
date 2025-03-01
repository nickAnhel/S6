import typing as tp

from database import DBHelper


class CustomersRepository:
    def __init__(self, db: DBHelper) -> None:
        self.db = db

    async def get_all(self) -> list[dict[str, tp.Any]]:
        async with self.db as cur:
            query = """SELECT * FROM customers"""
            result = await cur.execute(query)
            return result


class PartsRepository:
    def __init__(self, db: DBHelper) -> None:
        self.db = db

    async def get_top5_by_sales(self) -> list[dict[str, tp.Any]]:
        async with self.db as cur:
            query = """
                SELECT p.part_name, SUM(sd.quantity) AS total_sold
                FROM sale_details sd
                JOIN parts p USING(part_id)
                GROUP BY p.part_name
                ORDER BY total_sold DESC
                LIMIT 5;
            """
            result = await cur.execute(query)
            return result

    async def get_retail_selling_price_difference(self) -> list[dict[str, tp.Any]]:
        async with self.db as cur:
            query = """
                SELECT
                    p.part_name,
                    AVG(dd.selling_price) AS avg_selling_price,
                    AVG(p.retail_price) AS avg_retail_price,
                    AVG(p.retail_price - dd.selling_price) AS price_difference
                FROM delivery_details dd
                JOIN delivery_requests dr USING(request_id)
                JOIN parts p USING(part_id)
                GROUP BY p.part_name
                ORDER BY price_difference DESC;
            """
            result = await cur.execute(query)
            return result


class SalesRepository:
    def __init__(self, db: DBHelper) -> None:
        self.db = db

    async def get_monthly_revenue(self) -> list[dict[str, tp.Any]]:
        async with self.db as cur:
            query = """
                SELECT
                    DATE_FORMAT(s.sale_date, '%Y-%m') AS month,
                    SUM(sd.retail_price * sd.quantity) AS monthly_revenue
                FROM sales s
                JOIN sale_details sd USING(sale_id)
                GROUP BY month
                ORDER BY month;
            """
            result = await cur.execute(query)
            return result
