# WebhookEndpointResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**description** | **str** |  | 
**events** | **List[str]** |  | 
**status** | **str** |  | 
**masked_secret** | **str** | Masked signing secret for verification. | 
**secret** | **str** | Raw signing secret (only returned once during creation). | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from solifyn.models.webhook_endpoint_response_dto import WebhookEndpointResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEndpointResponseDto from a JSON string
webhook_endpoint_response_dto_instance = WebhookEndpointResponseDto.from_json(json)
# print the JSON string representation of the object
print(WebhookEndpointResponseDto.to_json())

# convert the object into a dict
webhook_endpoint_response_dto_dict = webhook_endpoint_response_dto_instance.to_dict()
# create an instance of WebhookEndpointResponseDto from a dict
webhook_endpoint_response_dto_from_dict = WebhookEndpointResponseDto.from_dict(webhook_endpoint_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


