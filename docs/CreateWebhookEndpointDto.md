# CreateWebhookEndpointDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send webhook events to. | 
**description** | **str** | Optional description for the webhook endpoint. | [optional] 
**events** | **List[str]** | The list of subscribed event types. | 

## Example

```python
from solifyn.models.create_webhook_endpoint_dto import CreateWebhookEndpointDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookEndpointDto from a JSON string
create_webhook_endpoint_dto_instance = CreateWebhookEndpointDto.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookEndpointDto.to_json())

# convert the object into a dict
create_webhook_endpoint_dto_dict = create_webhook_endpoint_dto_instance.to_dict()
# create an instance of CreateWebhookEndpointDto from a dict
create_webhook_endpoint_dto_from_dict = CreateWebhookEndpointDto.from_dict(create_webhook_endpoint_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


