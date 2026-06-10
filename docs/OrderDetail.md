# OrderDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_snapshot** | **List[str]** | Snapshot of files accessible after payment. | [optional] 
**license_key** | **str** | Assigned license key, if applicable. | [optional] 
**status** | **str** | Order resolution status. | [optional] 

## Example

```python
from solifyn.models.order_detail import OrderDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetail from a JSON string
order_detail_instance = OrderDetail.from_json(json)
# print the JSON string representation of the object
print(OrderDetail.to_json())

# convert the object into a dict
order_detail_dict = order_detail_instance.to_dict()
# create an instance of OrderDetail from a dict
order_detail_from_dict = OrderDetail.from_dict(order_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


