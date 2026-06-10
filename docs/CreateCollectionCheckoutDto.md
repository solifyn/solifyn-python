# CreateCollectionCheckoutDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | The database ID of the collection to checkout | 
**quantity** | **float** | Quantity of collections to buy | [optional] [default to 1]
**discount_code** | **str** | Discount code to apply | [optional] 
**aff** | **str** | Affiliate tracking code | [optional] 
**custom_fields** | **object** | Custom text fields / selected addons | [optional] 

## Example

```python
from solifyn.models.create_collection_checkout_dto import CreateCollectionCheckoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionCheckoutDto from a JSON string
create_collection_checkout_dto_instance = CreateCollectionCheckoutDto.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionCheckoutDto.to_json())

# convert the object into a dict
create_collection_checkout_dto_dict = create_collection_checkout_dto_instance.to_dict()
# create an instance of CreateCollectionCheckoutDto from a dict
create_collection_checkout_dto_from_dict = CreateCollectionCheckoutDto.from_dict(create_collection_checkout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


