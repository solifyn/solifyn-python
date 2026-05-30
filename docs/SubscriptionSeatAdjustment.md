# SubscriptionSeatAdjustment

Represents the detailed cost and billing impact of adjusting subscription seat add-on quantities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates if the seat adjustment was successful | 
**subscription_id** | **str** | The customer subscription ID | 
**addon_product_id** | **str** | The unique ID of the addon product | 
**old_quantity** | **float** | The previous seat quantity | 
**new_quantity** | **float** | The new seat quantity after adjustment | 
**quantity_delta** | **float** | The difference in seat quantity | 
**proration_type** | **str** | The proration strategy type applied | 
**cost_impact** | **float** | Calculated pro-rata price cost impact in currency unit (charged or credited) | 
**currency** | **str** | Billing currency | 

## Example

```python
from solifyn.models.subscription_seat_adjustment import SubscriptionSeatAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionSeatAdjustment from a JSON string
subscription_seat_adjustment_instance = SubscriptionSeatAdjustment.from_json(json)
# print the JSON string representation of the object
print(SubscriptionSeatAdjustment.to_json())

# convert the object into a dict
subscription_seat_adjustment_dict = subscription_seat_adjustment_instance.to_dict()
# create an instance of SubscriptionSeatAdjustment from a dict
subscription_seat_adjustment_from_dict = SubscriptionSeatAdjustment.from_dict(subscription_seat_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


