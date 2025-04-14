from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DateTime, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy import Enum
from sqlalchemy import create_engine
import enum

Base = declarative_base()


class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    protein = Column(Float, nullable=False)
    carbs = Column(Float, nullable=False)
    fats = Column(Float, nullable=False)
    serving_size = Column(String, nullable=True)


class Workouts(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    muscles = Column(JSON, nullable=False)


class TimeOfDay(enum.Enum):
    breakfast = "breakfast"
    lunch = "lunch"
    dinner = "dinner"
    snack = "snack"


class Diet(Base):
    __tablename__ = 'diet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    food_id = Column(Integer, ForeignKey('food.id'), nullable=False)
    servings = Column(Float, nullable=False)
    time_of_day = Column(Enum(TimeOfDay), nullable=False)


class Log(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    reps = Column(JSON, nullable=False)
    sets = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)

class Mood(Base):
    __tablename__ = 'mood'
    id = Column(DateTime, primary_key=True, nullable=False)
    fatigue = Column(Integer, nullable=True)
    clarity = Column(Integer, nullable=True)
    focus = Column(Integer, nullable=True)
    soreness = Column(Integer, nullable=True)
    irritability = Column(Integer, nullable=True)
    sleep_quality = Column(Integer, nullable=True)
    libido = Column(Integer, nullable=True)
    reflection = Column(String, nullable=True)

def initialize_tables():
    engine = create_engine('sqlite:///nutrition.db')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    initialize_tables()