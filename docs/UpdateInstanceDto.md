# UpdateInstanceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_name** | **str** | The updated friendly name of the instance | [optional] 
**ip_address** | **str** | The updated IP address of the client device | [optional] 

## Example

```python
from solifyn.models.update_instance_dto import UpdateInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstanceDto from a JSON string
update_instance_dto_instance = UpdateInstanceDto.from_json(json)
# print the JSON string representation of the object
print(UpdateInstanceDto.to_json())

# convert the object into a dict
update_instance_dto_dict = update_instance_dto_instance.to_dict()
# create an instance of UpdateInstanceDto from a dict
update_instance_dto_from_dict = UpdateInstanceDto.from_dict(update_instance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


