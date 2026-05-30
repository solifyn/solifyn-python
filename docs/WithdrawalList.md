# WithdrawalList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Withdrawal]**](Withdrawal.md) | List of withdrawals | 
**total_count** | **float** | Total count of withdrawals matching filters | 

## Example

```python
from solifyn.models.withdrawal_list import WithdrawalList

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalList from a JSON string
withdrawal_list_instance = WithdrawalList.from_json(json)
# print the JSON string representation of the object
print(WithdrawalList.to_json())

# convert the object into a dict
withdrawal_list_dict = withdrawal_list_instance.to_dict()
# create an instance of WithdrawalList from a dict
withdrawal_list_from_dict = WithdrawalList.from_dict(withdrawal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


