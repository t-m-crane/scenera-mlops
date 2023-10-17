import argparse
from cognitive_service_vision_model_customization_python_samples import TrainingClient, ResourceType
import os
import mlflow

def main(args):
    multi_service_endpoint = None
    model_name = args.model_name

    training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, args.resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))

    mlflow.set_tracking_uri(args.mlflow_tracking_uri)
    model = training_client.wait_for_training_completion(model_name)
    with mlflow.start_run() as run:
        mlflow.log_param("model_name", model_name)
        mlflow.log_param("model_status", model.status)
        mlflow.log_param("model_training_params", model.training_params)
        mlflow.log_metric("model_training_cost", model.training_cost_in_minutes)
        mlflow.log_metric("meanAveragePrecision30", model.model_performance["meanAveragePrecision30"])
        mlflow.log_metric("meanAveragePrecision50", model.model_performance["meanAveragePrecision50"])
        mlflow.log_metric("meanAveragePrecision75", model.model_performance["meanAveragePrecision75"])
    mlflow.end_run()      

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--model_name", type=str, help="Name of the model to be trained")
    parser.add_argument("--resource_name", type=str, help = "Name of the resource to be used for training")
    parser.add_argument("--mlflow_tracking_uri", type=str, help = "MLFlow Tracking URI from Azure Machine Learning Workspace")
    # parse args
    args = parser.parse_args()

    # return args
    return args

if __name__ == '__main__':
    args = parse_args()
    main(args)