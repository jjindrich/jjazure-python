# jjazure-python

## Configuration

1. VM with enabled Managed Identity
2. KeyVault in subscription with Access policy to allow VM Identity to read Secret
3. KeyVault firewall with Service Endpoint to VM subnet
4. Storage Account with Privatelink to VM subnet
5. KeyVault Secret value storageConnection with storage connection string
