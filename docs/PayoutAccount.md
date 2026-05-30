# PayoutAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The payout account ID | 
**status** | **str** | Status of the payout account onboarding | 
**capabilities** | **object** | Onboarding capability status flags (e.g., transfers, payouts) | [optional] 

## Example

```python
from solifyn.models.payout_account import PayoutAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutAccount from a JSON string
payout_account_instance = PayoutAccount.from_json(json)
# print the JSON string representation of the object
print(PayoutAccount.to_json())

# convert the object into a dict
payout_account_dict = payout_account_instance.to_dict()
# create an instance of PayoutAccount from a dict
payout_account_from_dict = PayoutAccount.from_dict(payout_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


