from nutrition_workers import ReadDatabaseInterface

if __name__ == '__main__':
    query = ReadDatabaseInterface()
    print(query.day_summary)
