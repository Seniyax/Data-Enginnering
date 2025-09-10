from utils.db_manager import Database_manager

class Loader:

    "weather loader class"

    def __init__(self, db_manager: Database_manager):
        self.db_manager = db_manager


    def load_records(self, records):

        if not records:
            print("⚠️ No records to load.")
            return

        insert_query = """
        INSERT INTO weather_data (city, temperature_celsius, humidity_percent, weather_description, timestamp_utc)
        VALUES (%s, %s, %s, %s, %s)
        """""


        for record in records:
            try:
                self.db_manager.execute_query(insert_query, (
                    record['city'],
                    record['temperature_celsius'],
                    record['humidity_percent'],
                    record['weather_description'],
                    record['timestamp_utc']
                ),
                fetch=False
                )
                print(f"✅ Inserted record for {record['city']} at {record['timestamp_utc']}")
            except Exception as e:
                print(f"❌Error inserting record {record}: {e}")
                