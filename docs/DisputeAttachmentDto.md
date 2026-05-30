# DisputeAttachmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uploaded file ID from the file service | 

## Example

```python
from solifyn.models.dispute_attachment_dto import DisputeAttachmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeAttachmentDto from a JSON string
dispute_attachment_dto_instance = DisputeAttachmentDto.from_json(json)
# print the JSON string representation of the object
print(DisputeAttachmentDto.to_json())

# convert the object into a dict
dispute_attachment_dto_dict = dispute_attachment_dto_instance.to_dict()
# create an instance of DisputeAttachmentDto from a dict
dispute_attachment_dto_from_dict = DisputeAttachmentDto.from_dict(dispute_attachment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


