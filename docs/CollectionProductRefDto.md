# CollectionProductRefDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The public product identifier (whopId or internal ID) | 
**quantity** | **float** | Quantity of this product in the collection | 

## Example

```python
from solifyn.models.collection_product_ref_dto import CollectionProductRefDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionProductRefDto from a JSON string
collection_product_ref_dto_instance = CollectionProductRefDto.from_json(json)
# print the JSON string representation of the object
print(CollectionProductRefDto.to_json())

# convert the object into a dict
collection_product_ref_dto_dict = collection_product_ref_dto_instance.to_dict()
# create an instance of CollectionProductRefDto from a dict
collection_product_ref_dto_from_dict = CollectionProductRefDto.from_dict(collection_product_ref_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


