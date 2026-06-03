# UpdateWebhookEndpointDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send webhook events to. | [optional] 
**description** | **str** | Optional description for the webhook endpoint. | [optional] 
**events** | **List[str]** | The list of subscribed event types. | [optional] 
**status** | **str** | The status of the webhook endpoint. | [optional] 

## Example

```python
from solifyn.models.update_webhook_endpoint_dto import UpdateWebhookEndpointDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookEndpointDto from a JSON string
update_webhook_endpoint_dto_instance = UpdateWebhookEndpointDto.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookEndpointDto.to_json())

# convert the object into a dict
update_webhook_endpoint_dto_dict = update_webhook_endpoint_dto_instance.to_dict()
# create an instance of UpdateWebhookEndpointDto from a dict
update_webhook_endpoint_dto_from_dict = UpdateWebhookEndpointDto.from_dict(update_webhook_endpoint_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


