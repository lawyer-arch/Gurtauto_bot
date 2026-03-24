import asyncio
import json

from database.session import async_session
from database.models.car import Car


JSON_PATH = "database/cars.json"  # поправь путь


async def import_cars():
    # 1. Читаем JSON
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        cars_data = json.load(f)

    # 2. Преобразуем в ORM объекты
    cars = []
    for item in cars_data:
        car = Car(
            marka=item.get("marka"),
            model=item.get("model"),
            modification=item.get("modification"),
            body_type=item.get("body_type"),
            generation=item.get("generation"),
        )
        cars.append(car)

    # 3. Сохраняем в БД
    async with async_session() as session:
        session.add_all(cars)
        await session.commit()

    print(f"Импортировано {len(cars)} автомобилей")


if __name__ == "__main__":
    asyncio.run(import_cars())