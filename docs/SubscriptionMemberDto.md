# SubscriptionMemberDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the member | 

## Example

```python
from solifyn.models.subscription_member_dto import SubscriptionMemberDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionMemberDto from a JSON string
subscription_member_dto_instance = SubscriptionMemberDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionMemberDto.to_json())

# convert the object into a dict
subscription_member_dto_dict = subscription_member_dto_instance.to_dict()
# create an instance of SubscriptionMemberDto from a dict
subscription_member_dto_from_dict = SubscriptionMemberDto.from_dict(subscription_member_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


