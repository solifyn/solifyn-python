# Order

Represents an order (payment) processed under your business, containing customer, billing, product cart, and refund details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique internal database identifier. | 
**invoice_url** | **str** | The invoice print URL. | 
**customer** | [**OrderCustomer**](OrderCustomer.md) | Customer details. | 
**total_amount** | **int** | Total paid amount in cents. | 
**subtotal** | **int** | Subtotal amount in cents. | 
**tax_amount** | **int** | Tax amount in cents. | 
**application_fee** | **int** | Application fee in cents. | 
**amount_after_fees** | **int** | Net amount after fees in cents. | 
**currency** | **str** | Currency code. | 
**status** | **str** | Current status of the payment. | 
**created_at** | **datetime** | Payment creation timestamp. | 
**paid_at** | **datetime** | Payment completion/paid timestamp. | [optional] 
**payment_method** | **str** | Payment method utilized. | 
**card_last_four** | **str** | Last four digits of card used. | [optional] 
**card_network** | **str** | Card network/brand. | [optional] 
**card_type** | **str** | Card type. | [optional] 
**billing** | [**OrderBilling**](OrderBilling.md) | Billing address details. | [optional] 
**product_cart** | [**List[OrderProductCart]**](OrderProductCart.md) | Products purchased in this order. | 
**metadata** | **object** | Custom metadata payload associated with this payment. | [optional] 
**order** | [**OrderDetail**](OrderDetail.md) | Order details snapshot. | [optional] 
**refundable** | **bool** | Indicates whether the order is eligible for refund. | 
**refunds** | [**List[OrderRefund]**](OrderRefund.md) | List of refunds associated with this payment. | [optional] 
**business_id** | **str** | Business unique ID identifier. | 
**business_name** | **str** | Business display title/name. | 
**billing_reason** | **str** | Billing reason detail. | [optional] 

## Example

```python
from solifyn.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


