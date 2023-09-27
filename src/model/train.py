# Import libraries

import argparse
#import glob
#import os
import mlflow

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from azure.identity import DefaultAzureCredential

# Import the client object from the SDK library
from azure.storage.blob import BlobClient


# define functions
def main(args):
    mlflow.autolog()

    # read data
    df = get_csvs_df(args.training_data)

    # split data
    X_train, X_test, y_train, y_test = split_data(df)

    # train model
    train_model(args.reg_rate, X_train, X_test, y_train, y_test)


def split_data(df):
    X, y = df[['Pregnancies',
               'PlasmaGlucose',
               'DiastolicBloodPressure',
               'TricepsThickness',
               'SerumInsulin',
               'BMI',
               'DiabetesPedigree',
               'Age']].values, df['Diabetic'].values
    # len(X)  nonessential code
    print(np.unique(y, return_counts=True))
    return train_test_split(X, y, test_size=0.30, random_state=0)


def get_csvs_df(args):
    credential = DefaultAzureCredential()
    
    # https://<your-storage-account-name>.blob.core.windows.net/
    storage_url = f"https://{args.account_name}.blob.core.windows.net/"

    # Create the client object using the storage URL and the credential
    blob_client = BlobClient(
        storage_url,
        container_name=args.container_name,
        blob_name=args.blob_name,
        credential=credential,
    )
    # encoding param is necessary for readall() to return str, otherwise it returns bytes
    downloader = blob_client.download_blob(max_concurrency=1, encoding='UTF-8')
    blob_text = downloader.readall()
    return pd.read_csv(blob_text)
   # if not os.path.exists(path):
   #     raise RuntimeError(f"Cannot use non-existent path provided: {path}")
   # csv_files = glob.glob(f"{path}/*.csv")
   # if not csv_files:
   #     raise RuntimeError(f"No CSV files found in provided data path: {path}")
   # return pd.concat((pd.read_csv(f) for f in csv_files), sort=False)

def download_blob_to_string(self, blob_service_client: BlobServiceClient, container_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample-blob.txt")

    # encoding param is necessary for readall() to return str, otherwise it returns bytes
    downloader = blob_client.download_blob(max_concurrency=1, encoding='UTF-8')
    blob_text = downloader.readall()
    print(f"Blob contents: {blob_text}")

def download_blob_to_stream(self, blob_service_client: BlobServiceClient, container_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample-blob.txt")

    # readinto() downloads the blob contents to a stream and returns the number of bytes read
    stream = io.BytesIO()
    num_bytes = blob_client.download_blob().readinto(stream)
    print(f"Number of bytes: {num_bytes}")


def train_model(reg_rate, X_train, X_test, y_train, y_test):
    # train model
    LogisticRegression(C=1/reg_rate, solver="liblinear").fit(X_train, y_train)


def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--training_data", dest='training_data',
                        type=str)
    parser.add_argument("--reg_rate", dest='reg_rate',
                        type=float, default=0.01)

    # parse args
    args = parser.parse_args()

    # return args
    return args


# run script
if __name__ == "__main__":
    # add space in logs
    print("\n\n")
    print("*" * 60)

    # parse args
    args = parse_args()

    # run main function
    main(args)

    # add space in logs
    print("*" * 60)
    print("\n\n")
