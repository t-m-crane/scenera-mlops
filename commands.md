## set subscription
```az account set --name balaraje```
```az account set --subscription 4956d76e-866c-44cb-ae27-659157d2b925```

## check subscription
```az account show```


## create job and run

```az ml job create --file job.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```

## add dataset to the azure ml workspace from your local file system

```az ml data create --file prod-dataset.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```

## Create service principle
```bash
az ad sp create-for-rbac --name "SCENERA-SP" --role contributor \
                              --scopes /subscriptions/4956d76e-866c-44cb-ae27-659157d2b925/resourceGroups/scenera-demo \
                              --sdk-auth
```

## Register a model (https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-models?view=azureml-api-2&tabs=cli%2Cuse-job-output#register-your-model-as-an-asset-in-machine-learning-by-using-the-cli)
```az ml model create --workspace-name scenera-demo-ml --name scenera-demo-model --version 1 --path azureml://jobs/jolly_turnip_zv1k0xm78f/outputs/artifacts/paths/model/```



## Create an endpoint 
```az ml online-endpoint create --name scenera-mlflow-endpoint --file create-endpoint.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```

## update an endpoint
```az ml online-endpoint update --file create-endpoint.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```


## Deploy the model
```az ml online-deployment create --name scenera-mlflow-deployment --endpoint scenera-mlflow-endpoint --file deployment.yml --all-traffic --resource-group scenera-demo --workspace-name scenera-demo-ml```


## Delete deployment
```az ml online-deployment delete --name scenera-mlflow-deployment --endpoint-name scenera-mlflow-endpoint --yes --resource-group scenera-demo --workspace-name scenera-demo-ml```



## create new model v2
```az ml model create --name scenera-demo-ml-2 --type mlflow_model --path azureml://jobs/jolly_turnip_zv1k0xm78f/outputs/artifacts/paths/model/ --workspace-name scenera-demo-ml

```