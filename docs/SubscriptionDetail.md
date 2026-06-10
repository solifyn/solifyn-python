# SubscriptionDetail

Represents detailed information about a customer subscription including active base product configuration, billing and payment history, and purchased add-ons.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**Subscription**](Subscription.md) | The main subscription details | 
**payments** | [**List[Order]**](Order.md) | The subscription payments / invoice billing history | 
**purchased_addons** | [**List[ResolvedAddon]**](ResolvedAddon.md) | List of purchased addons associated with this subscription | 
**product** | [**SubscriptionDetailProduct**](SubscriptionDetailProduct.md) | The core product information associated with this subscription | 

## Example

```python
from solifyn.models.subscription_detail import SubscriptionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetail from a JSON string
subscription_detail_instance = SubscriptionDetail.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetail.to_json())

# convert the object into a dict
subscription_detail_dict = subscription_detail_instance.to_dict()
# create an instance of SubscriptionDetail from a dict
subscription_detail_from_dict = SubscriptionDetail.from_dict(subscription_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


