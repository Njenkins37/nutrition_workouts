from .read_file import DatabaseInterface
from .database_interface import DatabaseInit
from .nutrition_tables import Workouts, Food, Diet, Mood, Log
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class InsertInterface(DatabaseInit):
    def __init__(self):
        super().__init__()
        self.db_interface = DatabaseInterface()
        self.is_inserted = self.insert()

    def insert(self):
        session = self.Session()
        print()
        session.add_all([Workouts(**workout) for workout in self.db_interface.workout_dict])
        session.add_all([Food(**foods) for foods in self.db_interface.foods_dict])
        session.add_all([Diet(**diet) for diet in self.db_interface.diet_dict])
        session.add_all([Log(**log) for log in self.db_interface.log_dict])
        session.add_all([Mood(**mood) for mood in self.db_interface.mood_dict])
        session.commit()
        return True


if __name__ == '__main__':
    temp = InsertInterface()
    if temp.is_inserted is True:
        print('All table data handled with no errors')
    else:
        print('Error')
