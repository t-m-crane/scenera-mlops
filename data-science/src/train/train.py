from cognitive_service_vision_model_customization_python_samples import TrainingClient, Model, ModelKind, TrainingParameters, EvaluationParameters, ResourceType
import os
import argparse

def main(args):
    multi_service_endpoint = None
    model_name = args.model_name

    training_client = TrainingClient(ResourceType.SINGLE_SERVICE_RESOURCE, args.input_resource_name, multi_service_endpoint, os.getenv('RESOURCE_KEY'))
    train_params = TrainingParameters(training_dataset_name=args.input_dataset_name, time_budget_in_hours=args.time_budget_in_hours, model_kind=ModelKind.GENERIC_OD)  # checkout ModelKind for all valid model kinds

    if args.validation_dataset_name == "None":
        eval_params = None
    else:
        eval_params = EvaluationParameters(test_dataset_name=args.validation_dataset_name)
    
    model = Model(model_name, train_params, eval_params)
    model = training_client.train_model(model)

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--model_name", type=str, help="Name of the model to be trained")
    parser.add_argument("--input_dataset_name", type=str, help="Name of the dataset to be used for training")
    parser.add_argument("--validation_dataset_name", type=str, default=None, help="Name of the dataset to be used for evaluation")
    parser.add_argument("--input_resource_name", type=str, help = "Name of the resource to be used for training")
    parser.add_argument("--time_budget_in_hours", type=int, help = "Number of hours model can train for")
    # parse args
    args = parser.parse_args()

    # return args
    return args

if __name__ == '__main__':
    args = parse_args()
    main(args)