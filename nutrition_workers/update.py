from nutrition_tables import Workouts, Food, Diet
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def update_food_name(session, old_name: str, new_name: str):
    food = session.query(Food).filter_by(name=old_name.title()).first()
    if food:
        food.name = new_name.title()
        session.commit()
        print(f"Updated food name from '{old_name}' to '{new_name}'")
    else:
        print(f"No food found with the name '{old_name}'")


def update_serving(session, food_date, food_name, old_serving, new_serving):
    result = (
        session.query(Diet)
        .join(Food, Diet.food_id == Food.id)
        .filter(
            and_(
                Food.name == food_name.title(),
                Diet.date == food_date,
                Diet.servings == old_serving
            )
        )
        .first()
    )

    if result:
        result.servings = new_serving
        session.commit()
        print("Serving updated successfully.")
    else:
        print("No matching record found.")


if __name__ == '__main__':
    engine = create_engine('sqlite:///nutrition.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

