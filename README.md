# JJAzure-Python samples

## Access Azure Storage with Azure KeyVault

1. VM with enabled Managed Identity
2. KeyVault in subscription with Access policy to allow VM Identity to read Secret
3. KeyVault firewall with Service Endpoint to VM subnet
4. Storage Account with Privatelink to VM subnet
5. KeyVault Secret value storageConnection with storage connection string

## Application Insights

https://docs.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python

- Trace
- Metrics
- Logs