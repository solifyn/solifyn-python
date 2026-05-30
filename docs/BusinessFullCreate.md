# BusinessFullCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title/name of the business | 
**website_url** | **str** | The primary website URL for the business | [optional] 
**country** | **str** | Country name of the business registration | 
**category** | **str** | The business market category (e.g. software, media) | [optional] 
**referred_by_code** | **str** | Optional partner referral code used during signup | [optional] 

## Example

```python
from solifyn.models.business_full_create import BusinessFullCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessFullCreate from a JSON string
business_full_create_instance = BusinessFullCreate.from_json(json)
# print the JSON string representation of the object
print(BusinessFullCreate.to_json())

# convert the object into a dict
business_full_create_dict = business_full_create_instance.to_dict()
# create an instance of BusinessFullCreate from a dict
business_full_create_from_dict = BusinessFullCreate.from_dict(business_full_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


