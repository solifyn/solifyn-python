# WebhookDisputePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal dispute ID. | [optional] 
**payment_id** | **str** |  | [optional] 
**amount** | **str** | Dollar value, 2 d.p. | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**editable** | **bool** |  | [optional] 
**needs_response_by** | **datetime** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from solifyn.models.webhook_dispute_payload import WebhookDisputePayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDisputePayload from a JSON string
webhook_dispute_payload_instance = WebhookDisputePayload.from_json(json)
# print the JSON string representation of the object
print(WebhookDisputePayload.to_json())

# convert the object into a dict
webhook_dispute_payload_dict = webhook_dispute_payload_instance.to_dict()
# create an instance of WebhookDisputePayload from a dict
webhook_dispute_payload_from_dict = WebhookDisputePayload.from_dict(webhook_dispute_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


