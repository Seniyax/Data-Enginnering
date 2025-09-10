class weatherTransformer:

    def __init__(self):
        pass

    def transfrom(self,records):

        transformed = []

        for record in records:
            if not record:
                continue

            try:
                transformed_record = {
                    'city': str(record['city']),
                    'temperature_celsius': float(record['temperature']),
                    'humidity_percent': int(record['humidity']),
                    'weather_description': str(record['weather_description']).capitalize(),
                    'timestamp_utc': record['timestamp'].isoformat()
                }

                transformed.append(transformed_record)
            except (KeyError, ValueError, TypeError) as e:
                print(f"❌Error transforming record {record}: {e}")
                continue    

        return transformed
