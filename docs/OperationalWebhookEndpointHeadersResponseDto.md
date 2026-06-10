# OperationalWebhookEndpointHeadersResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **object** | Key-value headers sent with the webhook. | 
**sensitive** | **List[str]** | List of sensitive header keys (e.g. Authorization) that are masked. | 

## Example

```python
from solifyn.models.operational_webhook_endpoint_headers_response_dto import OperationalWebhookEndpointHeadersResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalWebhookEndpointHeadersResponseDto from a JSON string
operational_webhook_endpoint_headers_response_dto_instance = OperationalWebhookEndpointHeadersResponseDto.from_json(json)
# print the JSON string representation of the object
print(OperationalWebhookEndpointHeadersResponseDto.to_json())

# convert the object into a dict
operational_webhook_endpoint_headers_response_dto_dict = operational_webhook_endpoint_headers_response_dto_instance.to_dict()
# create an instance of OperationalWebhookEndpointHeadersResponseDto from a dict
operational_webhook_endpoint_headers_response_dto_from_dict = OperationalWebhookEndpointHeadersResponseDto.from_dict(operational_webhook_endpoint_headers_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


