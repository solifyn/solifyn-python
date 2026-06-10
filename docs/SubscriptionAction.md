# SubscriptionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_days** | **float** | Number of free days to add (used with action: add_free_days) | [optional] 
**cancellation_mode** | **str** | Cancellation mode (used with action: cancel) | [optional] 
**void_payments** | **bool** | Whether to void subsequent payments (used with action: pause) | [optional] 
**addon_product_id** | **str** | ID of the addon product to adjust seats for (used with action: adjust_seats) | [optional] 
**new_quantity** | **float** | The new seat quantity (used with action: adjust_seats) | [optional] 
**proration_type** | **str** | Proration strategy mode (used with action: adjust_seats) | [optional] 
**idempotency_key** | **str** | A unique idempotency key to prevent duplicate mutative actions for network transient retries. | [optional] 

## Example

```python
from solifyn.models.subscription_action import SubscriptionAction

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAction from a JSON string
subscription_action_instance = SubscriptionAction.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAction.to_json())

# convert the object into a dict
subscription_action_dict = subscription_action_instance.to_dict()
# create an instance of SubscriptionAction from a dict
subscription_action_from_dict = SubscriptionAction.from_dict(subscription_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


