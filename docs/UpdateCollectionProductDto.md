# UpdateCollectionProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | New quantity of this product in the collection. | 

## Example

```python
from solifyn.models.update_collection_product_dto import UpdateCollectionProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCollectionProductDto from a JSON string
update_collection_product_dto_instance = UpdateCollectionProductDto.from_json(json)
# print the JSON string representation of the object
print(UpdateCollectionProductDto.to_json())

# convert the object into a dict
update_collection_product_dto_dict = update_collection_product_dto_instance.to_dict()
# create an instance of UpdateCollectionProductDto from a dict
update_collection_product_dto_from_dict = UpdateCollectionProductDto.from_dict(update_collection_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


