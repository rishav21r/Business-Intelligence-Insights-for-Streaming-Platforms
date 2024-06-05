import pandas as pd
import os

class DataProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def standardize_ratings(self, rating):
        if rating in ['NOT RATED', 'NOT_RATE', 'NR', 'UNRATED', 'UR']:
            return 'UNRATED'
        elif rating in ['ALL', 'ALL_AGES']:
            return 'ALL_AGES'
        elif rating == 'AGES_16_':
            return '16+'
        elif rating == 'AGES_18_':
            return '18+'
        return rating

    def process_file(self, file_name):
        file_path = os.path.join(self.input_dir, file_name)
        df = pd.read_csv(file_path)
        df['listed_in'] = df['listed_in'].str.split(', ')
        df_exploded = df.explode('listed_in')
        df_exploded['rating'] = df_exploded['rating'].apply(self.standardize_ratings)
        new_file_name = 'transformed_' + file_name
        new_file_path = os.path.join(self.output_dir, new_file_name)
        df_exploded.to_csv(new_file_path, index=False)
        print(f"Transformed file saved: {new_file_path}")

    def process_all_files(self, file_names):
        for file_name in file_names:
            self.process_file(file_name)

def main():
    input_dir = '../data'
    output_dir = '../data'
    file_names = [
        'netflix_titles.csv',
        'amazon_prime_titles.csv',
        'disney_plus_titles.csv',
        'hulu_titles.csv'
    ]

    processor = DataProcessor(input_dir, output_dir)
    processor.process_all_files(file_names)

if __name__ == "__main__":
    main()
