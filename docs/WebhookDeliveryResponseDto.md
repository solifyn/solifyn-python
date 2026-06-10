# WebhookDeliveryResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**endpoint_id** | **str** |  | 
**event** | **str** |  | 
**payload** | **object** |  | 
**response_status** | **object** |  | [optional] 
**response_body** | **object** |  | [optional] 
**duration_ms** | **object** |  | [optional] 
**status** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from solifyn.models.webhook_delivery_response_dto import WebhookDeliveryResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryResponseDto from a JSON string
webhook_delivery_response_dto_instance = WebhookDeliveryResponseDto.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryResponseDto.to_json())

# convert the object into a dict
webhook_delivery_response_dto_dict = webhook_delivery_response_dto_instance.to_dict()
# create an instance of WebhookDeliveryResponseDto from a dict
webhook_delivery_response_dto_from_dict = WebhookDeliveryResponseDto.from_dict(webhook_delivery_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


