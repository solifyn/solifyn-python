# SubscriptionsAction201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the subscription | 
**status** | **str** | The status of the subscription (e.g. completed, active, trialing, past_due, canceled) | 
**created_at** | **datetime** | Timestamp when the subscription was created | 
**joined_at** | **datetime** | Timestamp when the member joined | 
**updated_at** | **datetime** | Timestamp when the subscription was last updated | 
**manage_url** | **str** | The management URL for the billing/subscription | 
**member** | [**SubscriptionMemberDto**](SubscriptionMemberDto.md) | The member details | 
**user** | [**SubscriptionUserDto**](SubscriptionUserDto.md) | The user details | 
**renewal_period_start** | **object** | Start timestamp of the current renewal period | 
**renewal_period_end** | **object** | End timestamp of the current renewal period | 
**cancel_at_period_end** | **bool** | Whether the subscription is set to cancel at the end of the billing period | 
**cancel_option** | **object** | The cancel option details | 
**cancellation_reason** | **object** | The reason for cancellation | 
**canceled_at** | **object** | Timestamp when the subscription was canceled | 
**currency** | **str** | Billing currency | 
**company** | [**SubscriptionCompanyDto**](SubscriptionCompanyDto.md) | The company context details | 
**plan** | [**SubscriptionPlanDto**](SubscriptionPlanDto.md) | The plan associated with this subscription | 
**promo_code** | **object** | The promo code applied to the subscription | 
**product** | [**SubscriptionProductDto**](SubscriptionProductDto.md) | The product associated with the subscription | 
**license_key** | **object** | The license key associated with this subscription | 
**metadata** | **object** | Additional metadata for the subscription | 
**payment_collection_paused** | **bool** | Whether the payment collection is currently paused | 
**checkout_configuration_id** | **str** | The checkout configuration ID used | 
**price** | **object** | The price/amount of the membership | [optional] 
**type** | **object** | The type of the membership plan | [optional] 
**customer_id** | **object** | The business customer ID | [optional] 
**success** | **bool** | Indicates if the seat adjustment was successful | 
**subscription_id** | **str** | The customer subscription ID | 
**addon_product_id** | **str** | The unique ID of the addon product | 
**old_quantity** | **float** | The previous seat quantity | 
**new_quantity** | **float** | The new seat quantity after adjustment | 
**quantity_delta** | **float** | The difference in seat quantity | 
**proration_type** | **str** | The proration strategy type applied | 
**cost_impact** | **float** | Calculated pro-rata price cost impact in currency unit (charged or credited) | 

## Example

```python
from solifyn.models.subscriptions_action201_response import SubscriptionsAction201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsAction201Response from a JSON string
subscriptions_action201_response_instance = SubscriptionsAction201Response.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsAction201Response.to_json())

# convert the object into a dict
subscriptions_action201_response_dict = subscriptions_action201_response_instance.to_dict()
# create an instance of SubscriptionsAction201Response from a dict
subscriptions_action201_response_from_dict = SubscriptionsAction201Response.from_dict(subscriptions_action201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


