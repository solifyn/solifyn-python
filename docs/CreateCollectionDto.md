# CreateCollectionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The friendly name of the collection | 
**description** | **str** | A detailed description of this collection | [optional] 
**image_url** | **str** | The display cover image URL for this collection | [optional] 
**status** | **str** | The collection status | [optional] 
**products** | [**List[CollectionProductEntry]**](CollectionProductEntry.md) | List of products to include in this collection. At least one product is required. | 

## Example

```python
from solifyn.models.create_collection_dto import CreateCollectionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionDto from a JSON string
create_collection_dto_instance = CreateCollectionDto.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionDto.to_json())

# convert the object into a dict
create_collection_dto_dict = create_collection_dto_instance.to_dict()
# create an instance of CreateCollectionDto from a dict
create_collection_dto_from_dict = CreateCollectionDto.from_dict(create_collection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


