# OperationalWebhookEndpointInDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send webhook events to. | 
**description** | **str** | Optional description for the endpoint. | [optional] 
**disabled** | **bool** | Whether the endpoint is disabled. | [optional] [default to False]
**filter_types** | **List[str]** | The operational event types this endpoint will receive. | [optional] 
**metadata** | **object** | Metadata key-value pairs associated with the endpoint. | [optional] 
**secret** | **str** | Optional custom endpoint signing secret (base64 encoded random bytes optionally prefixed with whsec_). If not set, the server will generate one. | [optional] 
**throttle_rate** | **float** | Maximum messages per second to send to this endpoint (outgoing messages will be throttled to this rate). | [optional] 
**uid** | **str** | Optional unique user-defined identifier for the endpoint. | [optional] 

## Example

```python
from solifyn.models.operational_webhook_endpoint_in_dto import OperationalWebhookEndpointInDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalWebhookEndpointInDto from a JSON string
operational_webhook_endpoint_in_dto_instance = OperationalWebhookEndpointInDto.from_json(json)
# print the JSON string representation of the object
print(OperationalWebhookEndpointInDto.to_json())

# convert the object into a dict
operational_webhook_endpoint_in_dto_dict = operational_webhook_endpoint_in_dto_instance.to_dict()
# create an instance of OperationalWebhookEndpointInDto from a dict
operational_webhook_endpoint_in_dto_from_dict = OperationalWebhookEndpointInDto.from_dict(operational_webhook_endpoint_in_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


