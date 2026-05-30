# PayoutVerificationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PayoutVerification]**](PayoutVerification.md) | List of verifications for the payout account | 

## Example

```python
from solifyn.models.payout_verification_list import PayoutVerificationList

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutVerificationList from a JSON string
payout_verification_list_instance = PayoutVerificationList.from_json(json)
# print the JSON string representation of the object
print(PayoutVerificationList.to_json())

# convert the object into a dict
payout_verification_list_dict = payout_verification_list_instance.to_dict()
# create an instance of PayoutVerificationList from a dict
payout_verification_list_from_dict = PayoutVerificationList.from_dict(payout_verification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


