from cognitive_service_vision_model_customization_python_samples import TrainingClient, Model, ModelKind, TrainingParameters, EvaluationParameters, ResourceType
import os

def main(computer_vision_resource_name, dataset_name, model_name):
    multi_service_endpoint = None

    #TODO: Get key from keyvault
    training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, computer_vision_resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
    train_params = TrainingParameters(training_dataset_name=dataset_name, time_budget_in_hours=1, model_kind=ModelKind.GENERIC_OD)  # checkout ModelKind for all valid model kinds

    eval_dataset = None
    eval_params = EvaluationParameters(test_dataset_name=eval_dataset.name) if eval_dataset else None
    print(f"model_name: {model_name}")
    model = Model(model_name, train_params, eval_params)
    model = training_client.train_model(model)
    print(f"model name from env var: {os.getenv('MODEL_NAME')}")

if __name__ == '__main__':
    main(os.getenv("INPUT_RESOURCE_NAME"), os.getenv("INPUT_DATASET_NAME"), os.getenv("MODEL_NAME"))