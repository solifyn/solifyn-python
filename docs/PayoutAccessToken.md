# PayoutAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The temporary access token for embed portals | 
**expires_at** | **datetime** | Expiration timestamp of the access token | 

## Example

```python
from solifyn.models.payout_access_token import PayoutAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutAccessToken from a JSON string
payout_access_token_instance = PayoutAccessToken.from_json(json)
# print the JSON string representation of the object
print(PayoutAccessToken.to_json())

# convert the object into a dict
payout_access_token_dict = payout_access_token_instance.to_dict()
# create an instance of PayoutAccessToken from a dict
payout_access_token_from_dict = PayoutAccessToken.from_dict(payout_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


