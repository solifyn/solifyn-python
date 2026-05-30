# UserSettingsUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subdomain** | **str** | The custom store subdomain | [optional] 
**store_name** | **str** | The store name shown to customers | [optional] 
**social_links** | **object** | JSON structure listing social/contact URLs | [optional] 
**page_title** | **str** | SEO title tag of the store page | [optional] 
**seo_description** | **str** | SEO description meta tag | [optional] 
**seo_image** | **str** | SEO preview image URL | [optional] 
**favicon_url** | **str** | Favicon image URL | [optional] 
**google_analytics_id** | **str** | Google Analytics 4 Property ID | [optional] 
**google_tag_manager_id** | **str** | Google Tag Manager Container ID | [optional] 
**meta_pixel_id** | **str** | Facebook Meta Pixel ID | [optional] 
**logo_url** | **str** | Company/Store logo image URL | [optional] 
**business_title** | **str** | Name of the business entity | [optional] 
**statement_descriptor** | **str** | Credit card statement descriptor | [optional] 
**default_currency** | **str** | Three-letter currency symbol | [optional] 
**email** | **str** | User contact email | [optional] 
**first_name** | **str** | User first name | [optional] 
**last_name** | **str** | User last name | [optional] 
**avatar_url** | **str** | User profile avatar URL | [optional] 
**payout_threshold** | **float** | Minimum balance required for automatic payouts in cents | [optional] 
**notify_on_success** | **bool** | Send email notifications on successful payments | [optional] 
**send_license_key_email** | **bool** | Send license keys automatically via email | [optional] 
**send_digital_file_email** | **bool** | Send download links automatically via email | [optional] 
**notify_on_subscription_plan_changed** | **bool** | Send email notifications on subscription plan changes | [optional] 
**notify_on_subscription_set_to_cancel** | **bool** | Send email notifications when subscription is set to cancel | [optional] 
**notify_on_subscription_cancelled** | **bool** | Send email notifications when subscription is cancelled | [optional] 
**notify_on_refund_successful** | **bool** | Send email notifications when refund is successful | [optional] 
**notify_on_payment_failed** | **bool** | Send email notifications when payment fails | [optional] 
**notify_on_subscription_renewal_failed** | **bool** | Send email notifications when subscription renewal fails | [optional] 
**notify_on_subscription_trial_ending** | **bool** | Send email notifications when subscription trial is ending | [optional] 
**notify_on_subscription_paused** | **bool** | Send email notifications when subscription is paused | [optional] 

## Example

```python
from solifyn.models.user_settings_update import UserSettingsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsUpdate from a JSON string
user_settings_update_instance = UserSettingsUpdate.from_json(json)
# print the JSON string representation of the object
print(UserSettingsUpdate.to_json())

# convert the object into a dict
user_settings_update_dict = user_settings_update_instance.to_dict()
# create an instance of UserSettingsUpdate from a dict
user_settings_update_from_dict = UserSettingsUpdate.from_dict(user_settings_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


