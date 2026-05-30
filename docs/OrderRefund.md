# OrderRefund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_id** | **str** | Unique refund identifier. | 
**payment_id** | **str** | Associated payment ID. | 
**amount** | **int** | Refunded amount in cents. | 
**currency** | **str** | Currency code. | 
**status** | **str** | Status of refund. | 
**reason** | **str** | Reason for refund. | [optional] 
**is_partial** | **bool** | Whether it is a partial refund. | 
**created_at** | **datetime** | Refund creation timestamp. | 

## Example

```python
from solifyn.models.order_refund import OrderRefund

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRefund from a JSON string
order_refund_instance = OrderRefund.from_json(json)
# print the JSON string representation of the object
print(OrderRefund.to_json())

# convert the object into a dict
order_refund_dict = order_refund_instance.to_dict()
# create an instance of OrderRefund from a dict
order_refund_from_dict = OrderRefund.from_dict(order_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


