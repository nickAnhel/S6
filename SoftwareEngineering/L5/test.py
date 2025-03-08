import requests


API_URL = "https://fakestoreapi.com/products"


def get_data() -> None:
    response = requests.get(API_URL)
    items = response.json()

    for item in items:
        print(
            item["id"],
            item["title"],
            item["price"],
            item["rating"]["count"],
            item["rating"]["rate"],
            item["category"],
            item["description"],
            sep="\n",
        )

        print()



if __name__ == "__main__":
    get_data()
