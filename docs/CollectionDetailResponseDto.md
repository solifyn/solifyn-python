# CollectionDetailResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The collection ID | 
**name** | **str** | The name of the collection | 
**description** | **str** | A brief description of the collection | [optional] 
**image_url** | **str** | URL of the collection image | [optional] 
**status** | **str** | Status of the collection | 
**business_id** | **str** | The unique identifier of the business owning this collection. | 
**is_permanently_deleted** | **bool** | Indicates if the collection has been permanently deleted. | 
**created_at** | **datetime** | Timestamp when the collection was created | 
**updated_at** | **datetime** | Timestamp when the collection was last updated | 
**products** | [**List[CollectionProductDto]**](CollectionProductDto.md) | Full product details including quantity for each item in the collection | [optional] 

## Example

```python
from solifyn.models.collection_detail_response_dto import CollectionDetailResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDetailResponseDto from a JSON string
collection_detail_response_dto_instance = CollectionDetailResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionDetailResponseDto.to_json())

# convert the object into a dict
collection_detail_response_dto_dict = collection_detail_response_dto_instance.to_dict()
# create an instance of CollectionDetailResponseDto from a dict
collection_detail_response_dto_from_dict = CollectionDetailResponseDto.from_dict(collection_detail_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


