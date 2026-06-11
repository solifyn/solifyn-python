# EntitlementGrantResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique entitlement grant ID. | 
**business_id** | **str** | The business ID context. | 
**customer_id** | **str** | The customer ID. | 
**payment_id** | **str** | Associated payment transaction ID. | [optional] 
**product_id** | **str** | The purchased product ID. | 
**type** | **str** | The type of entitlement (e.g. GITHUB, DISCORD, TELEGRAM). | 
**github_repo** | **str** | Target GitHub repository (owner/repo) if type is GITHUB. | [optional] 
**github_permission** | **str** | GitHub access permission level if type is GITHUB. | [optional] 
**github_username** | **str** | The connected customer GitHub username. | [optional] 
**discord_guild_id** | **str** | Target Discord Guild ID if type is DISCORD. | [optional] 
**discord_role_id** | **str** | Target Discord Role ID if type is DISCORD. | [optional] 
**discord_username** | **str** | The connected customer Discord username. | [optional] 
**discord_user_id** | **str** | The connected customer Discord user ID. | [optional] 
**framer_template_id** | **str** | The Framer template ID if type is FRAMER. | [optional] 
**framer_remix_link** | **str** | The single-use remix link generated for the customer if type is FRAMER. | [optional] 
**status** | **str** | Delivery status of the collaborator invite (PENDING, DELIVERED, FAILED, REVOKED). | 
**oauth_url** | **str** | OAuth URL to redirect the customer to. | [optional] 
**error_details** | **str** | Error message if invitation delivery failed. | [optional] 
**metadata** | **object** | Platform-specific metadata. | [optional] 
**created_at** | **str** | Creation timestamp. | 
**updated_at** | **str** | Modification timestamp. | 

## Example

```python
from solifyn.models.entitlement_grant_response_dto import EntitlementGrantResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementGrantResponseDto from a JSON string
entitlement_grant_response_dto_instance = EntitlementGrantResponseDto.from_json(json)
# print the JSON string representation of the object
print(EntitlementGrantResponseDto.to_json())

# convert the object into a dict
entitlement_grant_response_dto_dict = entitlement_grant_response_dto_instance.to_dict()
# create an instance of EntitlementGrantResponseDto from a dict
entitlement_grant_response_dto_from_dict = EntitlementGrantResponseDto.from_dict(entitlement_grant_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


