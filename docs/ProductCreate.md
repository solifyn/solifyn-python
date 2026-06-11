# ProductCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product display name. | 
**description** | **str** | A description of the product. | [optional] 
**price** | **float** | Price value. | 
**currency** | **str** | Product pricing currency. | [default to 'USD']
**image_url** | **str** | URL of the product cover image. | [optional] 
**tax_category** | **str** | Tax classification. | 
**discount** | **float** | Percentage or flat rate discount. | [optional] 
**has_license_key** | **bool** | Whether to automatically issue license keys upon successful orders. | [optional] [default to False]
**has_digital_delivery** | **bool** | Whether the purchase includes downloadable files. | [optional] [default to False]
**has_github_access** | **bool** | Whether the purchase includes GitHub repository access. | [optional] [default to False]
**github_repo** | **str** | GitHub repository to grant access to (format: owner/repo). | [optional] 
**github_permission** | **str** | GitHub collaborator permission level. | [optional] 
**has_discord_access** | **bool** | Whether the purchase includes Discord server role access. | [optional] [default to False]
**discord_guild_id** | **str** | Discord Guild (Server) ID to grant access to. | [optional] 
**discord_role_id** | **str** | Discord Role ID to assign to the user. | [optional] 
**has_framer_access** | **bool** | Whether the purchase includes Framer Template access. | [optional] [default to False]
**framer_template_id** | **str** | Framer Template ID to grant access to. | [optional] 
**is_tax_inclusive** | **bool** | Whether tax is included in the base price. | [optional] [default to False]
**activation_limit** | **int** | Maximum concurrent activated instances allowed per license key. | [optional] 
**brand_id** | **str** | Brand id for the product, if not provided will default to primary brand. | [optional] 
**billing_period** | **int** | Billing period in days (for Subscription products). | [optional] 
**trial_period_days** | **int** | Trial duration in days. | [optional] 
**expiration_days** | **int** | Subscription expiration duration in days. | [optional] 
**statement_descriptor** | **str** | Custom billing descriptor. | [optional] 
**pay_what_you_want** | **bool** | Allow pay-what-you-want pricing. | [optional] [default to False]
**metadata** | **Dict[str, str]** | Developer key-value metadata pairs. | [optional] 
**custom_fields** | [**List[ProductCreateCustomFieldsInner]**](ProductCreateCustomFieldsInner.md) | Form field configurations to gather during checkout. | [optional] 
**stock** | **int** | Initial stock quantity limit. | [optional] 
**is_listed** | **bool** | Whether the product is publicly visible. | [optional] [default to True]
**is_free** | **bool** | Whether the product is free of charge. | [optional] [default to False]
**addons** | [**List[ProductCreateAddonsInner]**](ProductCreateAddonsInner.md) | Product addons configurations. | [optional] 
**entitlement_ids** | **List[str]** | Array of independent entitlement IDs to link to this product. | [optional] 

## Example

```python
from solifyn.models.product_create import ProductCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCreate from a JSON string
product_create_instance = ProductCreate.from_json(json)
# print the JSON string representation of the object
print(ProductCreate.to_json())

# convert the object into a dict
product_create_dict = product_create_instance.to_dict()
# create an instance of ProductCreate from a dict
product_create_from_dict = ProductCreate.from_dict(product_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


