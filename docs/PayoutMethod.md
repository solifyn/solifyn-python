# PayoutMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The payout method ID | 
**type** | **str** | Type of payout method (e.g. bank_account, stripe) | 
**status** | **str** | Status of the payout method | 
**details** | **object** | Metadata and details of the bank/card associated | [optional] 

## Example

```python
from solifyn.models.payout_method import PayoutMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutMethod from a JSON string
payout_method_instance = PayoutMethod.from_json(json)
# print the JSON string representation of the object
print(PayoutMethod.to_json())

# convert the object into a dict
payout_method_dict = payout_method_instance.to_dict()
# create an instance of PayoutMethod from a dict
payout_method_from_dict = PayoutMethod.from_dict(payout_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


