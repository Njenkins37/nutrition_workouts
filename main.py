from nutrition_workers import ReadDatabaseInterface, InsertInterface

if __name__ == '__main__':
    insert = InsertInterface()
    query = ReadDatabaseInterface()
    print(query.day_summary)
    print(query.time_summary)
    print(query.log_df)
