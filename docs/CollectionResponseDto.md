# CollectionResponseDto


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
**products** | [**List[CollectionProductRefDto]**](CollectionProductRefDto.md) | List of product references (id + quantity). Full product details are available via GET /products/:id. | [optional] 

## Example

```python
from solifyn.models.collection_response_dto import CollectionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionResponseDto from a JSON string
collection_response_dto_instance = CollectionResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionResponseDto.to_json())

# convert the object into a dict
collection_response_dto_dict = collection_response_dto_instance.to_dict()
# create an instance of CollectionResponseDto from a dict
collection_response_dto_from_dict = CollectionResponseDto.from_dict(collection_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


