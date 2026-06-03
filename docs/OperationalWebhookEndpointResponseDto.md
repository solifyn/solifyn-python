# OperationalWebhookEndpointResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**description** | **str** |  | 
**disabled** | **bool** |  | 
**filter_types** | **List[str]** |  | 
**metadata** | **object** |  | [optional] 
**throttle_rate** | **float** |  | 
**uid** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**secret** | **str** | The endpoint&#39;s raw secret (only returned on POST creation). | [optional] 

## Example

```python
from solifyn.models.operational_webhook_endpoint_response_dto import OperationalWebhookEndpointResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalWebhookEndpointResponseDto from a JSON string
operational_webhook_endpoint_response_dto_instance = OperationalWebhookEndpointResponseDto.from_json(json)
# print the JSON string representation of the object
print(OperationalWebhookEndpointResponseDto.to_json())

# convert the object into a dict
operational_webhook_endpoint_response_dto_dict = operational_webhook_endpoint_response_dto_instance.to_dict()
# create an instance of OperationalWebhookEndpointResponseDto from a dict
operational_webhook_endpoint_response_dto_from_dict = OperationalWebhookEndpointResponseDto.from_dict(operational_webhook_endpoint_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


