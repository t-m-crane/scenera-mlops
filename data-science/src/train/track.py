from cognitive_service_vision_model_customization_python_samples import TrainingClient, ResourceType
import os
import mlflow

def main(resource_name, model_name):
    multi_service_endpoint = None

    #TODO: Get key from keyvault
    training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
    print(f"model_name: {model_name}")
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
    print(f"Model {model.name} has been trained with status {model.status}, run id {run.info.run_id} and name {run.info.run_name}")
    

if __name__ == '__main__':
    main(os.getenv("INPUT_RESOURCE_NAME"), os.getenv("MODEL_NAME"))