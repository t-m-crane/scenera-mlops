## set subscription
```az account set --name balaraje```


## create job and run

```az ml job create --file job.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```

## add dataset to the azure ml workspace from your local file system

```az ml data create --file dataset.yml --resource-group scenera-demo --workspace-name scenera-demo-ml```