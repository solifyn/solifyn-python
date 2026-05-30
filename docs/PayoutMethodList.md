# PayoutMethodList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PayoutMethod]**](PayoutMethod.md) | List of payout methods available for the business | 

## Example

```python
from solifyn.models.payout_method_list import PayoutMethodList

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutMethodList from a JSON string
payout_method_list_instance = PayoutMethodList.from_json(json)
# print the JSON string representation of the object
print(PayoutMethodList.to_json())

# convert the object into a dict
payout_method_list_dict = payout_method_list_instance.to_dict()
# create an instance of PayoutMethodList from a dict
payout_method_list_from_dict = PayoutMethodList.from_dict(payout_method_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


