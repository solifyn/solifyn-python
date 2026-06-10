# DiscordRolesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Discord Role ID | 
**name** | **str** | The Discord Role Name | 
**position** | **float** | The position of the role in the server hierarchy | 
**color** | **float** | The color of the role (hex integer code) | 

## Example

```python
from solifyn.models.discord_roles_response_dto import DiscordRolesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordRolesResponseDto from a JSON string
discord_roles_response_dto_instance = DiscordRolesResponseDto.from_json(json)
# print the JSON string representation of the object
print(DiscordRolesResponseDto.to_json())

# convert the object into a dict
discord_roles_response_dto_dict = discord_roles_response_dto_instance.to_dict()
# create an instance of DiscordRolesResponseDto from a dict
discord_roles_response_dto_from_dict = DiscordRolesResponseDto.from_dict(discord_roles_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


