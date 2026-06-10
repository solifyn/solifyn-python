# OperationalWebhookEndpointHeadersInDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **object** | Custom key-value headers to send with the webhook. | 

## Example

```python
from solifyn.models.operational_webhook_endpoint_headers_in_dto import OperationalWebhookEndpointHeadersInDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalWebhookEndpointHeadersInDto from a JSON string
operational_webhook_endpoint_headers_in_dto_instance = OperationalWebhookEndpointHeadersInDto.from_json(json)
# print the JSON string representation of the object
print(OperationalWebhookEndpointHeadersInDto.to_json())

# convert the object into a dict
operational_webhook_endpoint_headers_in_dto_dict = operational_webhook_endpoint_headers_in_dto_instance.to_dict()
# create an instance of OperationalWebhookEndpointHeadersInDto from a dict
operational_webhook_endpoint_headers_in_dto_from_dict = OperationalWebhookEndpointHeadersInDto.from_dict(operational_webhook_endpoint_headers_in_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


