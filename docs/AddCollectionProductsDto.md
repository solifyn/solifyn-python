# AddCollectionProductsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[CollectionProductEntry]**](CollectionProductEntry.md) | List of products to add or update in the collection. | 

## Example

```python
from solifyn.models.add_collection_products_dto import AddCollectionProductsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddCollectionProductsDto from a JSON string
add_collection_products_dto_instance = AddCollectionProductsDto.from_json(json)
# print the JSON string representation of the object
print(AddCollectionProductsDto.to_json())

# convert the object into a dict
add_collection_products_dto_dict = add_collection_products_dto_instance.to_dict()
# create an instance of AddCollectionProductsDto from a dict
add_collection_products_dto_from_dict = AddCollectionProductsDto.from_dict(add_collection_products_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


