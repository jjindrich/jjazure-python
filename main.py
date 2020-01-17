import os, uuid
import datetime
import requests
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# pip install azure-storage-blob

from azure.keyvault.secrets import SecretClient
# pip install azure-keyvault
from azure.identity import ManagedIdentityCredential
# pip install azure-identity

def get_token():
    # this url is hard-code and only available to services with identity.
    oauth_token = requests.get(
        'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.net',
        headers={'Metadata': 'True'}).json()
    return oauth_token['access_token']


print("1. GET IDENTITY")
token = get_token()

print("2. GET KEYVAULT SECRET")
try:
    credential=ManagedIdentityCredential()
    #kv="https://o2keyvault.vault.azure.net/"
    kv="https://o2centralkeyvault.vault.azure.net/"
    secret_client = SecretClient(vault_url=kv, credential=credential)
    secret = secret_client.get_secret("storageConnection")
    print('secret loaded:' + secret.name)
    #print(secret.value)

except Exception as ex:
    print('Exception:')
    print(ex)

print("3. CREATE STORAGE CONTAINER")
try:
    # privatelink
    connstr = secret.value
    
    blob_service_client = BlobServiceClient.from_connection_string(connstr)

    n = "jjcontainer" + str(datetime.datetime.now().microsecond)
    blob_service_client.create_container(n)    

    print("created:" + n)

except Exception as ex:
    print('Exception:')
    print(ex)
