# PayoutVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The verification check ID | 
**status** | **str** | Status of verification (pending, verified, rejected) | 
**type** | **str** | Verification type (identity, business, address) | 
**details** | **object** | Details and requirements of the verification check | [optional] 

## Example

```python
from solifyn.models.payout_verification import PayoutVerification

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutVerification from a JSON string
payout_verification_instance = PayoutVerification.from_json(json)
# print the JSON string representation of the object
print(PayoutVerification.to_json())

# convert the object into a dict
payout_verification_dict = payout_verification_instance.to_dict()
# create an instance of PayoutVerification from a dict
payout_verification_from_dict = PayoutVerification.from_dict(payout_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


