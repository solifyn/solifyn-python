# Business


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique business ID | 
**title** | **str** | Title or name of the business | 
**description** | **str** | A description explaining what the business does | [optional] 
**whop_id** | **str** | The Whop Company ID | 
**merchant_id** | **str** | The merchant owner ID | 
**verified** | **bool** | Whether the business has been KYC-verified on Whop | 
**send_customer_emails** | **bool** | Whether auto-emails are enabled for customers | 
**member_count** | **float** | Total members/customers under this business | 
**route** | **str** | Whop friendly URL path route | [optional] 
**default_currency** | **str** | The default currency of the business | 
**published_reviews_count** | **float** | Number of published user reviews on Whop | 
**metadata** | **object** | Custom key-value metadata | [optional] 
**target_audience** | **str** | The target audience description | [optional] 
**social_links** | **object** | Social links setup | [optional] 
**affiliate_instructions** | **str** | Markdown instructions for affiliates | [optional] 
**whop_created_at** | **datetime** | Whop account creation timestamp | [optional] 
**whop_updated_at** | **datetime** | Whop account last updated timestamp | [optional] 
**created_at** | **datetime** | Timestamp when the business record was created | 
**updated_at** | **datetime** | Timestamp when the business record was last updated | 
**logo_url** | **str** | Brand logo image URL resolved from primary brand | [optional] 

## Example

```python
from solifyn.models.business import Business

# TODO update the JSON string below
json = "{}"
# create an instance of Business from a JSON string
business_instance = Business.from_json(json)
# print the JSON string representation of the object
print(Business.to_json())

# convert the object into a dict
business_dict = business_instance.to_dict()
# create an instance of Business from a dict
business_from_dict = Business.from_dict(business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


