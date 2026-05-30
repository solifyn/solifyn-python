# OrderCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The customer identifier. | 
**email** | **str** | The customer email address. | 
**name** | **str** | The customer name. | 
**username** | **str** | The customer username. | [optional] 

## Example

```python
from solifyn.models.order_customer import OrderCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCustomer from a JSON string
order_customer_instance = OrderCustomer.from_json(json)
# print the JSON string representation of the object
print(OrderCustomer.to_json())

# convert the object into a dict
order_customer_dict = order_customer_instance.to_dict()
# create an instance of OrderCustomer from a dict
order_customer_from_dict = OrderCustomer.from_dict(order_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


