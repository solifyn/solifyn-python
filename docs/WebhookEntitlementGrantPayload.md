# WebhookEntitlementGrantPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique entitlement grant ID. | [optional] 
**business_id** | **str** | The business ID context. | [optional] 
**customer_id** | **str** | The customer ID. | [optional] 
**payment_id** | **str** | Associated payment transaction ID. | [optional] 
**product_id** | **str** | The purchased product ID. | [optional] 
**type** | **str** | The type of entitlement (e.g. GITHUB). | [optional] 
**github_repo** | **str** | Target GitHub repository (owner/repo) if type is GITHUB. | [optional] 
**github_permission** | **str** | GitHub access permission level if type is GITHUB. | [optional] 
**github_username** | **str** | The connected customer GitHub username. | [optional] 
**status** | **str** | Delivery status of the collaborator invite (PENDING, DELIVERED, FAILED, REVOKED). | [optional] 
**oauth_url** | **str** | OAuth URL to redirect the customer to. | [optional] 
**error_details** | **str** | Error message if invitation delivery failed. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from solifyn.models.webhook_entitlement_grant_payload import WebhookEntitlementGrantPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEntitlementGrantPayload from a JSON string
webhook_entitlement_grant_payload_instance = WebhookEntitlementGrantPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookEntitlementGrantPayload.to_json())

# convert the object into a dict
webhook_entitlement_grant_payload_dict = webhook_entitlement_grant_payload_instance.to_dict()
# create an instance of WebhookEntitlementGrantPayload from a dict
webhook_entitlement_grant_payload_from_dict = WebhookEntitlementGrantPayload.from_dict(webhook_entitlement_grant_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


