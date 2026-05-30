# CollectionUnarchivedResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message indicating the outcome of the action. | 

## Example

```python
from solifyn.models.collection_unarchived_response_dto import CollectionUnarchivedResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionUnarchivedResponseDto from a JSON string
collection_unarchived_response_dto_instance = CollectionUnarchivedResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionUnarchivedResponseDto.to_json())

# convert the object into a dict
collection_unarchived_response_dto_dict = collection_unarchived_response_dto_instance.to_dict()
# create an instance of CollectionUnarchivedResponseDto from a dict
collection_unarchived_response_dto_from_dict = CollectionUnarchivedResponseDto.from_dict(collection_unarchived_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


