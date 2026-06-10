# DisputeFileUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Uploaded file ID | 
**filename** | **str** | Name of the file | 
**upload_url** | **str** | S3 presigned upload URL | [optional] 
**upload_headers** | **object** | HTTP headers required for the S3 upload request | [optional] 

## Example

```python
from solifyn.models.dispute_file_upload import DisputeFileUpload

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeFileUpload from a JSON string
dispute_file_upload_instance = DisputeFileUpload.from_json(json)
# print the JSON string representation of the object
print(DisputeFileUpload.to_json())

# convert the object into a dict
dispute_file_upload_dict = dispute_file_upload_instance.to_dict()
# create an instance of DisputeFileUpload from a dict
dispute_file_upload_from_dict = DisputeFileUpload.from_dict(dispute_file_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


