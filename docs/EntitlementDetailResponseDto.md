# EntitlementDetailResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique entitlement ID | 
**business_id** | **str** | The owning business ID | 
**name** | **str** | The name of the entitlement | 
**type** | **str** | The type of access to grant | 
**status** | **str** | Status of the entitlement | 
**created_at** | **datetime** | When the entitlement was created | 
**updated_at** | **datetime** | When the entitlement was last updated | 
**github_repo** | **str** | The GitHub repository (e.g., owner/repo) | [optional] 
**github_permission** | **str** | The GitHub repository permission level | [optional] 
**discord_guild_id** | **str** | The Discord Guild/Server ID | [optional] 
**discord_role_id** | **str** | The Discord Role ID to assign | [optional] 
**framer_template_id** | **str** | The associated Framer Template ID | [optional] 
**license_key** | **str** | The static License Key (if not dynamically generated) | [optional] 
**activation_limit** | **float** | The maximum activation limit for licenses | [optional] 
**activation_message** | **str** | A message shown to the user upon license activation | [optional] 
**expiry_hours** | **float** | The number of hours until the entitlement expires | [optional] 
**digital_link** | **str** | The digital download URL or redirect link | [optional] 
**instructions** | **str** | Custom setup instructions for the user | [optional] 
**grants_count** | **float** | Number of active customer grants issued from this entitlement | 
**products** | [**List[LinkedProductDto]**](LinkedProductDto.md) | Products that are currently linked to this entitlement | 

## Example

```python
from solifyn.models.entitlement_detail_response_dto import EntitlementDetailResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementDetailResponseDto from a JSON string
entitlement_detail_response_dto_instance = EntitlementDetailResponseDto.from_json(json)
# print the JSON string representation of the object
print(EntitlementDetailResponseDto.to_json())

# convert the object into a dict
entitlement_detail_response_dto_dict = entitlement_detail_response_dto_instance.to_dict()
# create an instance of EntitlementDetailResponseDto from a dict
entitlement_detail_response_dto_from_dict = EntitlementDetailResponseDto.from_dict(entitlement_detail_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


