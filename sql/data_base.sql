CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    temperature_celsius FLOAT NOT NULL,
    humidity_percent INT NOT NULL,
    weather_description VARCHAR(255) NOT NULL,
    timestamp_utc TIMESTAMP NOT NULL
);