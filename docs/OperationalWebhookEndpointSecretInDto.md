# OperationalWebhookEndpointSecretInDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Optional custom endpoint signing secret (base64 encoded random bytes optionally prefixed with whsec_). If not set, a new random secret is generated. | [optional] 

## Example

```python
from solifyn.models.operational_webhook_endpoint_secret_in_dto import OperationalWebhookEndpointSecretInDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalWebhookEndpointSecretInDto from a JSON string
operational_webhook_endpoint_secret_in_dto_instance = OperationalWebhookEndpointSecretInDto.from_json(json)
# print the JSON string representation of the object
print(OperationalWebhookEndpointSecretInDto.to_json())

# convert the object into a dict
operational_webhook_endpoint_secret_in_dto_dict = operational_webhook_endpoint_secret_in_dto_instance.to_dict()
# create an instance of OperationalWebhookEndpointSecretInDto from a dict
operational_webhook_endpoint_secret_in_dto_from_dict = OperationalWebhookEndpointSecretInDto.from_dict(operational_webhook_endpoint_secret_in_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


