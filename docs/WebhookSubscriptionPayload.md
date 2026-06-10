# WebhookSubscriptionPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The subscription ID. | [optional] 
**status** | **str** | Current status of the subscription. | [optional] 
**cancel_at_period_end** | **bool** |  | [optional] 
**renewal_period_start** | **datetime** |  | [optional] 
**renewal_period_end** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_title** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from solifyn.models.webhook_subscription_payload import WebhookSubscriptionPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionPayload from a JSON string
webhook_subscription_payload_instance = WebhookSubscriptionPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionPayload.to_json())

# convert the object into a dict
webhook_subscription_payload_dict = webhook_subscription_payload_instance.to_dict()
# create an instance of WebhookSubscriptionPayload from a dict
webhook_subscription_payload_from_dict = WebhookSubscriptionPayload.from_dict(webhook_subscription_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


