# CollectionArchivedResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message indicating the outcome of the action. | 

## Example

```python
from solifyn.models.collection_archived_response_dto import CollectionArchivedResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionArchivedResponseDto from a JSON string
collection_archived_response_dto_instance = CollectionArchivedResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionArchivedResponseDto.to_json())

# convert the object into a dict
collection_archived_response_dto_dict = collection_archived_response_dto_instance.to_dict()
# create an instance of CollectionArchivedResponseDto from a dict
collection_archived_response_dto_from_dict = CollectionArchivedResponseDto.from_dict(collection_archived_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


