# OrderProductCart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product identifier. | 
**name** | **str** | Product name. | 
**quantity** | **int** | Quantity purchased. | 
**price** | **int** | Price per item in cents. | 
**pricing_type** | **str** | Pricing type, e.g. one-time or renewal. | [optional] 

## Example

```python
from solifyn.models.order_product_cart import OrderProductCart

# TODO update the JSON string below
json = "{}"
# create an instance of OrderProductCart from a JSON string
order_product_cart_instance = OrderProductCart.from_json(json)
# print the JSON string representation of the object
print(OrderProductCart.to_json())

# convert the object into a dict
order_product_cart_dict = order_product_cart_instance.to_dict()
# create an instance of OrderProductCart from a dict
order_product_cart_from_dict = OrderProductCart.from_dict(order_product_cart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


