# OrderRefundCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The refund amount in cents. If full refund is true, this can represent the total amount. | 
**is_full_refund** | **bool** | Whether this is a full refund or a partial refund. | 
**idempotency_key** | **str** | A unique idempotency key to prevent double refunds for transient network retries. | 
**auto_revoke_seats** | **bool** | Whether to automatically revoke seat add-ons matching the refund amount. | [optional] 
**revoke_seats** | [**List[RevokeSeatDto]**](RevokeSeatDto.md) | List of specific addons and the quantities of seats to revoke. | [optional] 

## Example

```python
from solifyn.models.order_refund_create import OrderRefundCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRefundCreate from a JSON string
order_refund_create_instance = OrderRefundCreate.from_json(json)
# print the JSON string representation of the object
print(OrderRefundCreate.to_json())

# convert the object into a dict
order_refund_create_dict = order_refund_create_instance.to_dict()
# create an instance of OrderRefundCreate from a dict
order_refund_create_from_dict = OrderRefundCreate.from_dict(order_refund_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


