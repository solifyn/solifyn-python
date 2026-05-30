# OrderBillingUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from solifyn.models.order_billing_update import OrderBillingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBillingUpdate from a JSON string
order_billing_update_instance = OrderBillingUpdate.from_json(json)
# print the JSON string representation of the object
print(OrderBillingUpdate.to_json())

# convert the object into a dict
order_billing_update_dict = order_billing_update_instance.to_dict()
# create an instance of OrderBillingUpdate from a dict
order_billing_update_from_dict = OrderBillingUpdate.from_dict(order_billing_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


