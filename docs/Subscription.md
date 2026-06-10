# Subscription

Represents a customer subscription membership resource, containing current billing terms, plan, status, and metadata.

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
**currency** | **str** | The currency used for payments | 
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

## Example

```python
from solifyn.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


