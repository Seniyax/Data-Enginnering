from src.extractor import WeatherExtractor
from src.transformer import weatherTransformer
from src.loader import Loader


def run_etl_pipeline():

    print ("🚀 Starting ETL pipeline...")

    # Step 1: Extract
    fecther = WeatherExtractor()
    raw_data = fecther.extract_all()

    # Step 2: Transform
    transformer = weatherTransformer()
    transformed_data = transformer.transfrom(raw_data)

    # Step 3: Load
    loader = Loader()
    loader.load_records(transformed_data)



if __name__ == "__main__":
    run_etl_pipeline()