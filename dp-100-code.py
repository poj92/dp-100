
# To install azure Python SDK
# pip install azure-ai-ml

# connect to the worksace

# Define parameters
subscription_id = '1c8b603c-35c2-411e-b37f-c4175769d138'
resource_grp = 'rg-dp100-labs'
workspace_name = 'mlw-dp100-labs'


from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential


ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_grp, workspace_name
)

