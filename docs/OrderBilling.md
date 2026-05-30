# OrderBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Street address. | [optional] 
**city** | **str** | City. | [optional] 
**state** | **str** | State or province. | [optional] 
**zipcode** | **str** | Postal or ZIP code. | [optional] 
**country** | **str** | Country code. | [optional] 

## Example

```python
from solifyn.models.order_billing import OrderBilling

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBilling from a JSON string
order_billing_instance = OrderBilling.from_json(json)
# print the JSON string representation of the object
print(OrderBilling.to_json())

# convert the object into a dict
order_billing_dict = order_billing_instance.to_dict()
# create an instance of OrderBilling from a dict
order_billing_from_dict = OrderBilling.from_dict(order_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


