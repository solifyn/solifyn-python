# SubscriptionProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the product | 
**title** | **str** | The title/name of the product | 
**metadata** | **object** | Additional metadata associated with the product | [optional] 

## Example

```python
from solifyn.models.subscription_product_dto import SubscriptionProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionProductDto from a JSON string
subscription_product_dto_instance = SubscriptionProductDto.from_json(json)
# print the JSON string representation of the object
print(SubscriptionProductDto.to_json())

# convert the object into a dict
subscription_product_dto_dict = subscription_product_dto_instance.to_dict()
# create an instance of SubscriptionProductDto from a dict
subscription_product_dto_from_dict = SubscriptionProductDto.from_dict(subscription_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


