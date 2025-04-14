from .database_interface import DatabaseInit
from .nutrition_tables import Diet, Food, Workouts, Log
import pandas as pd


class ReadDatabaseInterface(DatabaseInit):
    def __init__(self):
        super().__init__()
        self.food_df = self.get_food()
        self.day_summary = self.get_macro_count()
        self.time_summary = self.get_time_of_day_count()

    def get_food(self):
        session = self.Session()
        results = session.query(Diet, Food).join(
            Food, Diet.food_id == Food.id
        ).all()

        data = []
        for diet, food in results:
            row = {
                "date": diet.date,
                "food_id": diet.food_id,
                "Time of Day": diet.time_of_day.value,
                'servings': diet.servings,
                "food_name": food.name,
                "protein": food.protein * diet.servings,
                "carbs": food.carbs * diet.servings,
                "fat": food.fats * diet.servings,
            }
            data.append(row)
        session.close()
        return pd.DataFrame(data)

    def get_calories(self, df):
        df['calories'] = (df['protein'] + df['carbs']) * 4 + (df['fat'] * 9)
        return df

    def get_macro_count(self):
        df = self.food_df.groupby('date')[['protein', 'carbs', 'fat']].sum()
        return self.get_calories(df)

    def get_time_of_day_count(self):
        df = self.food_df.groupby(['date', 'Time of Day'])[['protein', 'carbs', 'fat']].sum()
        return self.get_calories(df)


if __name__ == "__main__":
    test = ReadDatabaseInterface()
    print(test.day_summary)
    print(test.time_summary)
