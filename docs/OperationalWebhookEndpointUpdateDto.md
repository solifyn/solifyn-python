# OperationalWebhookEndpointUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send webhook events to. | 
**description** | **str** | Optional description for the endpoint. | [optional] 
**disabled** | **bool** | Whether the endpoint is disabled. | [optional] 
**filter_types** | **List[str]** | The operational event types this endpoint will receive. | [optional] 
**metadata** | **object** | Metadata key-value pairs associated with the endpoint. | [optional] 
**throttle_rate** | **float** | Maximum messages per second to send to this endpoint. | [optional] 
**uid** | **str** | Optional unique user-defined identifier for the endpoint. | [optional] 

## Example

```python
from solifyn.models.operational_webhook_endpoint_update_dto import OperationalWebhookEndpointUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalWebhookEndpointUpdateDto from a JSON string
operational_webhook_endpoint_update_dto_instance = OperationalWebhookEndpointUpdateDto.from_json(json)
# print the JSON string representation of the object
print(OperationalWebhookEndpointUpdateDto.to_json())

# convert the object into a dict
operational_webhook_endpoint_update_dto_dict = operational_webhook_endpoint_update_dto_instance.to_dict()
# create an instance of OperationalWebhookEndpointUpdateDto from a dict
operational_webhook_endpoint_update_dto_from_dict = OperationalWebhookEndpointUpdateDto.from_dict(operational_webhook_endpoint_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


