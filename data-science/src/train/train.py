from cognitive_service_vision_model_customization_python_samples import TrainingClient, Model, ModelKind, TrainingParameters, EvaluationParameters, ResourceType
import os
import uuid

def main(computer_vision_resource_name, dataset_name):
    model_name = str(uuid.uuid4())
    multi_service_endpoint = None

    #TODO: Get key from keyvault
    training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, computer_vision_resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
    train_params = TrainingParameters(training_dataset_name=dataset_name, time_budget_in_hours=1, model_kind=ModelKind.GENERIC_OD)  # checkout ModelKind for all valid model kinds

    eval_dataset = None
    eval_params = EvaluationParameters(test_dataset_name=eval_dataset.name) if eval_dataset else None


    model = Model(model_name, train_params, eval_params)
    model = training_client.train_model(model)
    save_model_name()
    
def save_model_name(model_name):
    name = 'model_name'
    value = model_name
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--computer_vision_resource_name', required=True, help='The name of the computer vision resource')
    parser.add_argument('--dataset_name', required=True, help='The name of the dataset')

    args = parser.parse_args()
    main(args.computer_vision_resource_name, args.dataset_name)