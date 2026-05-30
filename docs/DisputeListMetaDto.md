# DisputeListMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total count of disputes | 
**page** | **float** | Current page number | 
**limit** | **float** | Limit of items per page | 
**total_pages** | **float** | Total number of pages | 

## Example

```python
from solifyn.models.dispute_list_meta_dto import DisputeListMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeListMetaDto from a JSON string
dispute_list_meta_dto_instance = DisputeListMetaDto.from_json(json)
# print the JSON string representation of the object
print(DisputeListMetaDto.to_json())

# convert the object into a dict
dispute_list_meta_dto_dict = dispute_list_meta_dto_instance.to_dict()
# create an instance of DisputeListMetaDto from a dict
dispute_list_meta_dto_from_dict = DisputeListMetaDto.from_dict(dispute_list_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


