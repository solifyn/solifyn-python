# OperationalWebhookEndpointListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OperationalWebhookEndpointResponseDto]**](OperationalWebhookEndpointResponseDto.md) |  | 
**done** | **bool** |  | 
**iterator** | **object** |  | [optional] 
**prev_iterator** | **object** |  | [optional] 

## Example

```python
from solifyn.models.operational_webhook_endpoint_list_response_dto import OperationalWebhookEndpointListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalWebhookEndpointListResponseDto from a JSON string
operational_webhook_endpoint_list_response_dto_instance = OperationalWebhookEndpointListResponseDto.from_json(json)
# print the JSON string representation of the object
print(OperationalWebhookEndpointListResponseDto.to_json())

# convert the object into a dict
operational_webhook_endpoint_list_response_dto_dict = operational_webhook_endpoint_list_response_dto_instance.to_dict()
# create an instance of OperationalWebhookEndpointListResponseDto from a dict
operational_webhook_endpoint_list_response_dto_from_dict = OperationalWebhookEndpointListResponseDto.from_dict(operational_webhook_endpoint_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


