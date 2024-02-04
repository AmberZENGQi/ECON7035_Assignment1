import pandas as pd
import argparse

def clean(input1, input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    # Merge the two dataframes based on the ID value
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    # Remove redundant ID column
    merged_df.drop('id', axis=1, inplace=True)

    # Drop rows with missing values
    merged_df.dropna(inplace=True)

    # Drop rows with 'insurance' or 'Insurance' in the 'job' column
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    # Save the df
    return merged_df


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser()
    # Add the positional arguments
    parser.add_argument('input1', help='respondent_contact.csv file')
    parser.add_argument('input2', help='respondent_other.csv file')
    parser.add_argument('output', help='respondent_cleaned.csv file')
    args = parser.parse_args()

    # Call the clean_data function
    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)

    # Print the shape of the output file
    print("Output shape:", cleaned.shape)