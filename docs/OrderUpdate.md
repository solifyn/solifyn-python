# OrderUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing** | [**OrderBillingUpdate**](OrderBillingUpdate.md) |  | [optional] 

## Example

```python
from solifyn.models.order_update import OrderUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdate from a JSON string
order_update_instance = OrderUpdate.from_json(json)
# print the JSON string representation of the object
print(OrderUpdate.to_json())

# convert the object into a dict
order_update_dict = order_update_instance.to_dict()
# create an instance of OrderUpdate from a dict
order_update_from_dict = OrderUpdate.from_dict(order_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


