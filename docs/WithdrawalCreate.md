# WithdrawalCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to withdraw in cents (e.g. 1000 for $10.00) | 
**currency** | **str** | Three-letter ISO currency code (lowercase) | 
**payout_method_id** | **str** | The ID of the payout method to withdraw to. If omitted, default is used. | [optional] 

## Example

```python
from solifyn.models.withdrawal_create import WithdrawalCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalCreate from a JSON string
withdrawal_create_instance = WithdrawalCreate.from_json(json)
# print the JSON string representation of the object
print(WithdrawalCreate.to_json())

# convert the object into a dict
withdrawal_create_dict = withdrawal_create_instance.to_dict()
# create an instance of WithdrawalCreate from a dict
withdrawal_create_from_dict = WithdrawalCreate.from_dict(withdrawal_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


