# SyncLoginDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_token** | **str** | The JWT access token from the Live API server | 

## Example

```python
from solifyn.models.sync_login_dto import SyncLoginDto

# TODO update the JSON string below
json = "{}"
# create an instance of SyncLoginDto from a JSON string
sync_login_dto_instance = SyncLoginDto.from_json(json)
# print the JSON string representation of the object
print(SyncLoginDto.to_json())

# convert the object into a dict
sync_login_dto_dict = sync_login_dto_instance.to_dict()
# create an instance of SyncLoginDto from a dict
sync_login_dto_from_dict = SyncLoginDto.from_dict(sync_login_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


