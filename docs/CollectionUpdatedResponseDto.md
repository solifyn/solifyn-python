# CollectionUpdatedResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message indicating the outcome of the action. | 

## Example

```python
from solifyn.models.collection_updated_response_dto import CollectionUpdatedResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionUpdatedResponseDto from a JSON string
collection_updated_response_dto_instance = CollectionUpdatedResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionUpdatedResponseDto.to_json())

# convert the object into a dict
collection_updated_response_dto_dict = collection_updated_response_dto_instance.to_dict()
# create an instance of CollectionUpdatedResponseDto from a dict
collection_updated_response_dto_from_dict = CollectionUpdatedResponseDto.from_dict(collection_updated_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


