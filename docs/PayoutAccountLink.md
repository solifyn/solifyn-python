# PayoutAccountLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL redirecting to the Stripe Express onboarding/portal | 
**expires_at** | **datetime** | Expiration timestamp of the link | 

## Example

```python
from solifyn.models.payout_account_link import PayoutAccountLink

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutAccountLink from a JSON string
payout_account_link_instance = PayoutAccountLink.from_json(json)
# print the JSON string representation of the object
print(PayoutAccountLink.to_json())

# convert the object into a dict
payout_account_link_dict = payout_account_link_instance.to_dict()
# create an instance of PayoutAccountLink from a dict
payout_account_link_from_dict = PayoutAccountLink.from_dict(payout_account_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


