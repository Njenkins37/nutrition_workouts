import pandas as pd
from openpyxl import load_workbook
from sqlalchemy.orm import declarative_base
from .nutrition_tables import Food, Workouts
from .database_interface import DatabaseInit

Base = declarative_base()


class DatabaseInterface(DatabaseInit):
    def __init__(self):
        """
        The DatabaseInterface class converts the Excel file information into a dictionary to be inserted into the database.
        The Excel file is located in the Files location.
        """
        super().__init__()
        self.file_name = '../Files/nutrition_workouts.xlsx'
        self.workouts_sheet = 'workouts'
        self.foods_sheet = 'foods'
        self.diet_sheet = 'diet'
        self.log_sheet = 'log'
        self.mood_sheet = 'mood'
        self.food_map = self.get_food_id()
        self.workout_map = self.get_workout_id()
        self.foods_dict = self.get_data(self.foods_sheet)
        self.workout_dict = self.get_data(self.workouts_sheet)
        self.diet_dict = self.get_diet_log('diet')
        self.log_dict = self.get_diet_log('log')
        self.mood_dict = self.get_data(self.mood_sheet)

    def get_data(self, sheet: str) -> list:
        """
        Calls the get_columns fucntion to get the mapping of data for the both sheets in the nutrition excel file
        :return: The data in a dictionary format to be inserted in the database
        """
        data = self.get_dict(pd.read_excel(self.file_name, sheet_name=sheet))

        is_clear = self.clear_sheet_but_keep_header(sheet)
        if is_clear:
            print(f'Data retreived from {sheet} and removed from excel file')
        else:
            print(f'There was no data to retrieve from {sheet}')

        return data

    @staticmethod
    def get_dict(df: pd.DataFrame) -> list:
        """

        :param df: The dataframe resulted from reading the passed excel file and the sheet name
        :return: the dataframe in a dictionary format to be inserted into the dictionary
        """
        if 'muscles' in df.columns:
            df['muscles'] = df['muscles'].apply(
                lambda x: [m.strip().title() for m in x.split(',')] if isinstance(x, str) else x
            )
        if 'name' in df.columns:
            df['name'] = df['name'].apply(lambda x: x.title())

        return [
            {column: row[column] for column in df.columns}
            for _, row in df.iterrows()
        ]

    def clear_sheet_but_keep_header(self, sheet_name: str) -> bool:
        """

        :param sheet_name: The sheet name to delete from
        :return: Boolean. Used in check to determine which log message to print
        """

        # Removes content from the workbook so that it's not reuploaded into the database.
        workbook = load_workbook(self.file_name)
        if sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]
            if sheet.max_row > 1:
                sheet.delete_rows(2, sheet.max_row - 1)
                workbook.save(self.file_name)
                return True
            else:
                return False
        return False

    def get_food_id(self):
        session = self.Session()
        food_map = {food.name: food.id for food in session.query(Food).all()}
        session.close()
        return food_map

    def get_workout_id(self):
        session = self.Session()
        workout_map = {workout.name: workout.id for workout in session.query(Workouts).all()}
        session.close()
        return workout_map

    def get_diet_log(self, param):
        df = pd.read_excel(self.file_name, self.diet_sheet)
        df['name'] = df['name'].apply(lambda x: x.strip().title())

        if param == 'diet':
            df['food_id'] = df['name'].map(self.food_map)
        elif param == 'log':
            df['workout_id'] = df['name'].map(self.food_map)

        df.drop('name', axis=1, inplace=True)
        data = self.get_dict(df)

        is_clear = self.clear_sheet_but_keep_header('diet')
        if is_clear:
            print(f'Data retrieved from {param} sheet and sheet cleared')
        else:
            print(f'There was no data to retrieve from {param}')
        return data


if __name__ == '__main__':
    data = DatabaseInterface()
    print(data.diet_dict)
