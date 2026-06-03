# WebhookRefundPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal refund ID. | [optional] 
**payment_id** | **str** |  | [optional] 
**amount** | **str** | Dollar value, 2 d.p. | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**reference_value** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**provider_created_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from solifyn.models.webhook_refund_payload import WebhookRefundPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRefundPayload from a JSON string
webhook_refund_payload_instance = WebhookRefundPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookRefundPayload.to_json())

# convert the object into a dict
webhook_refund_payload_dict = webhook_refund_payload_instance.to_dict()
# create an instance of WebhookRefundPayload from a dict
webhook_refund_payload_from_dict = WebhookRefundPayload.from_dict(webhook_refund_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


