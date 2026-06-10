# UpdateCollectionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The friendly name of the collection | [optional] 
**description** | **str** | A detailed description of this collection | [optional] 
**image_url** | **str** | The display cover image URL for this collection | [optional] 

## Example

```python
from solifyn.models.update_collection_dto import UpdateCollectionDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCollectionDto from a JSON string
update_collection_dto_instance = UpdateCollectionDto.from_json(json)
# print the JSON string representation of the object
print(UpdateCollectionDto.to_json())

# convert the object into a dict
update_collection_dto_dict = update_collection_dto_instance.to_dict()
# create an instance of UpdateCollectionDto from a dict
update_collection_dto_from_dict = UpdateCollectionDto.from_dict(update_collection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


