# CreateApiKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-friendly name of the API key. | 
**allow_write** | **bool** | Whether the API key is allowed to make mutating write requests. | [optional] [default to True]

## Example

```python
from solifyn.models.create_api_key_dto import CreateApiKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKeyDto from a JSON string
create_api_key_dto_instance = CreateApiKeyDto.from_json(json)
# print the JSON string representation of the object
print(CreateApiKeyDto.to_json())

# convert the object into a dict
create_api_key_dto_dict = create_api_key_dto_instance.to_dict()
# create an instance of CreateApiKeyDto from a dict
create_api_key_dto_from_dict = CreateApiKeyDto.from_dict(create_api_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


