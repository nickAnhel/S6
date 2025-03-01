import typing as tp

import pandas as pd
import matplotlib.pyplot as plt

from repositories import CustomersRepository, PartsRepository, SalesRepository


class CustomersService:
    def __init__(self, repo: CustomersRepository) -> None:
        self.repo = repo

    async def get_all_customers(self) -> list[dict[str, tp.Any]]:
        return await self.repo.get_all()


class PartsService:
    def __init__(self, repo: PartsRepository) -> None:
        self.repo = repo

    async def get_top5_parts_by_sales(self) -> list[dict[str, tp.Any]]:
        return await self.repo.get_top5_by_sales()

    async def draw_top5_parts_by_sales(self) -> None:
        data = await self.repo.get_top5_by_sales()
        df = pd.DataFrame(data)

        plt.bar(
            x=df["part_name"],
            height=df["total_sold"],
        )
        plt.xlabel("Part Name")
        plt.ylabel("Total Sold")
        plt.title("Top 5 Parts by Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    async def get_parts_retail_selling_price_difference(self) -> list[dict[str, tp.Any]]:
        return await self.repo.get_retail_selling_price_difference()

    async def draw_parts_retail_selling_price_difference(self) -> None:
        data = await self.repo.get_retail_selling_price_difference()
        df = pd.DataFrame(data)

        plt.bar(
            x=df["part_name"],
            height=df["price_difference"],
        )
        plt.xlabel("Part Name")
        plt.ylabel("Price Difference")
        plt.title("Parts retail / selling price difference")
        plt.xticks(rotation=45)
        plt.yticks(range(0, 52, 2))
        plt.show()


class SalesService:
    def __init__(self, repo: SalesRepository) -> None:
        self.repo = repo

    async def get_monthly_revenue(self) -> list[dict[str, tp.Any]]:
        return await self.repo.get_monthly_revenue()

    async def draw_monthly_revenue(self) -> None:
        data = await self.repo.get_monthly_revenue()
        df = pd.DataFrame(data)

        plt.pie(
            df["monthly_revenue"],
            labels=df["month"],
            autopct="%1.1f%%",
        )
        plt.title("Monthly Revenue Distribution")
        plt.show()
