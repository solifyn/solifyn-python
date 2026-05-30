# DiscountUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer-facing name of the discount. | [optional] 
**type** | **str** | Calculation type: percentage or fixed_amount. | [optional] 
**amount** | **float** | The discount value. | [optional] 
**usage_limit** | **int** | Maximum number of redemptions allowed. | [optional] 
**expires_at** | **datetime** | Expiration timestamp for the discount. | [optional] 
**subscription_cycles** | **int** | Number of subscription cycles this discount applies to. | [optional] 
**restricted_to** | **List[str]** | List of product IDs this discount is restricted to. | [optional] 
**preserve_on_plan_change** | **bool** | Whether to preserve the discount when subscription plan changes. | [optional] 
**metadata** | **object** | Custom metadata for the discount. | [optional] 

## Example

```python
from solifyn.models.discount_update import DiscountUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountUpdate from a JSON string
discount_update_instance = DiscountUpdate.from_json(json)
# print the JSON string representation of the object
print(DiscountUpdate.to_json())

# convert the object into a dict
discount_update_dict = discount_update_instance.to_dict()
# create an instance of DiscountUpdate from a dict
discount_update_from_dict = DiscountUpdate.from_dict(discount_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


