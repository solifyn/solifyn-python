# CollectionProductDeletedResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message indicating the outcome of the action. | 

## Example

```python
from solifyn.models.collection_product_deleted_response_dto import CollectionProductDeletedResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionProductDeletedResponseDto from a JSON string
collection_product_deleted_response_dto_instance = CollectionProductDeletedResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionProductDeletedResponseDto.to_json())

# convert the object into a dict
collection_product_deleted_response_dto_dict = collection_product_deleted_response_dto_instance.to_dict()
# create an instance of CollectionProductDeletedResponseDto from a dict
collection_product_deleted_response_dto_from_dict = CollectionProductDeletedResponseDto.from_dict(collection_product_deleted_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


