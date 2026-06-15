# CreateEntitlementDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-friendly name of the entitlement | 
**type** | **str** | The type of access to grant | 
**github_repo** | **str** | The GitHub repository (e.g., owner/repo) | [optional] 
**github_permission** | **str** | The GitHub repository permission level | [optional] [default to 'pull']
**discord_guild_id** | **str** | The Discord Guild/Server ID | [optional] 
**discord_role_id** | **str** | The Discord Role ID to assign | [optional] 
**framer_template_id** | **str** | The associated Framer Template ID | [optional] 
**license_key** | **str** | The static License Key (if not dynamically generated) | [optional] 
**activation_limit** | **float** | The maximum activation limit for licenses | [optional] 
**activation_message** | **str** | A message shown to the user upon license activation | [optional] 
**expiry_hours** | **float** | The number of hours until the entitlement expires | [optional] 
**digital_link** | **str** | The digital download URL or redirect link | [optional] 
**instructions** | **str** | Custom setup instructions for the user | [optional] 
**status** | **str** | The entitlement status | [optional] [default to 'active']

## Example

```python
from solifyn.models.create_entitlement_dto import CreateEntitlementDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntitlementDto from a JSON string
create_entitlement_dto_instance = CreateEntitlementDto.from_json(json)
# print the JSON string representation of the object
print(CreateEntitlementDto.to_json())

# convert the object into a dict
create_entitlement_dto_dict = create_entitlement_dto_instance.to_dict()
# create an instance of CreateEntitlementDto from a dict
create_entitlement_dto_from_dict = CreateEntitlementDto.from_dict(create_entitlement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


