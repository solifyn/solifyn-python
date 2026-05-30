# SubscriptionUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the user | 
**username** | **str** | The username of the user | 
**name** | **str** | The full name of the user | 
**email** | **str** | The email address of the user | 

## Example

```python
from solifyn.models.subscription_user_dto import SubscriptionUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUserDto from a JSON string
subscription_user_dto_instance = SubscriptionUserDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionUserDto.to_json())

# convert the object into a dict
subscription_user_dto_dict = subscription_user_dto_instance.to_dict()
# create an instance of SubscriptionUserDto from a dict
subscription_user_dto_from_dict = SubscriptionUserDto.from_dict(subscription_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


