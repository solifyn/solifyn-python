# SubscriptionCompanyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the company | 
**title** | **str** | The title/name of the company | 

## Example

```python
from solifyn.models.subscription_company_dto import SubscriptionCompanyDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCompanyDto from a JSON string
subscription_company_dto_instance = SubscriptionCompanyDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCompanyDto.to_json())

# convert the object into a dict
subscription_company_dto_dict = subscription_company_dto_instance.to_dict()
# create an instance of SubscriptionCompanyDto from a dict
subscription_company_dto_from_dict = SubscriptionCompanyDto.from_dict(subscription_company_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


