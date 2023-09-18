## set subscription
```az account set --name balaraje```

## check subscription
```az account show```


## create job and run

```az ml job create --file job.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```

## add dataset to the azure ml workspace from your local file system

```az ml data create --file dataset.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```

## Create service principle
```bash
az ad sp create-for-rbac --name "SCENERA-SP" --role contributor \
                              --scopes /subscriptions/4956d76e-866c-44cb-ae27-659157d2b925/resourceGroups/scenera-demo \
                              --sdk-auth
```