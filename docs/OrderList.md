# OrderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Order]**](Order.md) | List of order items. | 
**total_count** | **int** | Total number of items matching filters. | 

## Example

```python
from solifyn.models.order_list import OrderList

# TODO update the JSON string below
json = "{}"
# create an instance of OrderList from a JSON string
order_list_instance = OrderList.from_json(json)
# print the JSON string representation of the object
print(OrderList.to_json())

# convert the object into a dict
order_list_dict = order_list_instance.to_dict()
# create an instance of OrderList from a dict
order_list_from_dict = OrderList.from_dict(order_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


