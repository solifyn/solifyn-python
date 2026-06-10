# CollectionProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier (ID) of the product. | 
**name** | **str** | The display name of the product. | 
**price** | **float** | The price amount of the product (e.g. 29.00). | 
**currency** | **str** | The three-letter ISO currency code (e.g. USD, VND, EUR). | 
**description** | **str** | A comprehensive rich text description of the product. | [optional] 
**status** | **str** | The lifecycle status of the product (e.g. ACTIVE, ARCHIVED). | 
**image_url** | **str** | URL of the product cover image. | 
**tax_category** | **str** | The tax classification for the product. | 
**pricing_type** | **str** | Pricing model of the product. | 
**discount** | **float** | Discount value as a percentage or fixed amount. | 
**has_license_key** | **bool** | Indicates if the product issues a cryptographically secure software license key upon checkout completion. | 
**has_digital_delivery** | **bool** | Whether the product includes digital file downloads upon purchase. | 
**has_github_access** | **bool** | Whether the product includes GitHub repository access. | 
**github_repo** | **str** | GitHub repository to grant access to (format: owner/repo). | 
**github_permission** | **str** | GitHub collaborator permission level. | 
**has_discord_access** | **bool** | Whether the product includes Discord role access. | 
**discord_guild_id** | **str** | Discord Guild (Server) ID to grant access to. | 
**discord_role_id** | **str** | Discord Role ID to assign to the user. | 
**is_tax_inclusive** | **bool** | Whether the product price already includes applicable sales taxes. | 
**billing_period** | **int** | The subscription billing cycle interval in days (for subscription products). | 
**trial_period_days** | **int** | Trial duration in days for subscription products. | 
**expiration_days** | **int** | Automatic expiration period in days for the subscription entitlement. | 
**statement_descriptor** | **str** | Custom text displayed on customer credit card statements for purchases of this product. | 
**pay_what_you_want** | **bool** | Indicates if customers are allowed to enter a custom pricing amount at checkout. | 
**metadata** | **Dict[str, str]** | Custom developer metadata key-value pairs associated with the product. | 
**custom_fields** | **List[object]** | Custom form field questions to ask the customer during checkout. | 
**stock** | **int** | Available stock quantity, or null for unlimited inventory. | 
**activation_limit** | **int** | Maximum number of simultaneous active instances/devices allowed per issued license key (applicable if hasLicenseKey is true). | 
**is_listed** | **bool** | Defines if the product is listed publicly on the merchant&#39;s storefront template. | 
**is_free** | **bool** | Whether the product is free. | 
**created_at** | **datetime** | Timestamp indicating exactly when the product was created. | 
**updated_at** | **datetime** | Timestamp indicating when the product was last modified. | 
**is_permanently_deleted** | **bool** | Indicates if the product has been permanently deleted. | 
**brand_id** | **str** | Optional brand identifier. | 
**digital_link** | **str** | Secure link for digital delivery. | 
**instructions** | **str** | Special instructions provided upon purchase. | 
**activation_message** | **str** | Custom message displayed when a license key is activated. | 
**expiry_hours** | **int** | Number of hours until the license key expires. | 
**business_id** | **str** | The unique identifier of the business owning this product. | 
**quantity** | **float** | Quantity of the product in the collection | 

## Example

```python
from solifyn.models.collection_product_dto import CollectionProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionProductDto from a JSON string
collection_product_dto_instance = CollectionProductDto.from_json(json)
# print the JSON string representation of the object
print(CollectionProductDto.to_json())

# convert the object into a dict
collection_product_dto_dict = collection_product_dto_instance.to_dict()
# create an instance of CollectionProductDto from a dict
collection_product_dto_from_dict = CollectionProductDto.from_dict(collection_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


