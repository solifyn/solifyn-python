# DiscountCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique discount code string (will be automatically capitalized). | 
**name** | **str** | Customer-facing name of the discount. | [optional] 
**type** | **str** | Calculation type: percentage or fixed_amount. | 
**amount** | **float** | The discount value. If percentage, enter value like 10 for 10%. If fixed_amount, enter value like 10 for $10.00. | 
**usage_limit** | **int** | Maximum number of redemptions allowed. | [optional] 
**expires_at** | **datetime** | Expiration timestamp for the discount. | [optional] 
**subscription_cycles** | **int** | Number of subscription cycles this discount applies to. | [optional] 
**restricted_to** | **List[str]** | List of product IDs this discount is restricted to. | [optional] 
**preserve_on_plan_change** | **bool** | Whether to preserve the discount when subscription plan changes. | [optional] 
**metadata** | **object** | Custom metadata for the discount. | [optional] 

## Example

```python
from solifyn.models.discount_create import DiscountCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountCreate from a JSON string
discount_create_instance = DiscountCreate.from_json(json)
# print the JSON string representation of the object
print(DiscountCreate.to_json())

# convert the object into a dict
discount_create_dict = discount_create_instance.to_dict()
# create an instance of DiscountCreate from a dict
discount_create_from_dict = DiscountCreate.from_dict(discount_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


