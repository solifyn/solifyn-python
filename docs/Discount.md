# Discount

Represents a discount code created under your business, containing type, amount, usage limits, and expiration details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique prefix-based identifier of the discount (e.g., &#x60;disc_cs8f67sd7f6fw3fs&#x60;). | 
**discount_id** | **str** | Alias for the unique identifier of the discount. | 
**code** | **str** | The unique discount code (e.g. SAVE10) used during checkout. | 
**name** | **str** | The customer-facing name of the discount code (e.g. Summer Sale). | [optional] 
**type** | **str** | The discount calculation type: percentage or fixed_amount. | 
**amount** | **int** | The discount value. For percentage type, it is in basis points (e.g. 1000 &#x3D; 10.00%). For fixed_amount type, it is in cents (e.g. 1000 &#x3D; $10.00). | 
**usage_limit** | **int** | Maximum number of times this discount code can be redeemed. Null represents unlimited usage. | 
**times_used** | **int** | The number of times this discount code has been successfully redeemed. | 
**expires_at** | **datetime** | The expiration timestamp after which the discount code is no longer valid. | 
**status** | **str** | The current status of the discount. | 
**business_id** | **str** | The unique identifier associated with the business this discount belongs to. | 
**created_at** | **datetime** | Timestamp indicating exactly when the discount was created. | 
**updated_at** | **datetime** | Timestamp indicating when the discount was last updated. | 

## Example

```python
from solifyn.models.discount import Discount

# TODO update the JSON string below
json = "{}"
# create an instance of Discount from a JSON string
discount_instance = Discount.from_json(json)
# print the JSON string representation of the object
print(Discount.to_json())

# convert the object into a dict
discount_dict = discount_instance.to_dict()
# create an instance of Discount from a dict
discount_from_dict = Discount.from_dict(discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


