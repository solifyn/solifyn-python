# SubscriptionPlanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the plan | 
**metadata** | **object** | Additional metadata associated with the plan | [optional] 

## Example

```python
from solifyn.models.subscription_plan_dto import SubscriptionPlanDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlanDto from a JSON string
subscription_plan_dto_instance = SubscriptionPlanDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPlanDto.to_json())

# convert the object into a dict
subscription_plan_dto_dict = subscription_plan_dto_instance.to_dict()
# create an instance of SubscriptionPlanDto from a dict
subscription_plan_dto_from_dict = SubscriptionPlanDto.from_dict(subscription_plan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


