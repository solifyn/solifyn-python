# Dispute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The dispute ID | 
**whop_id** | **str** | The Whop Dispute ID | 
**amount** | **float** | The dispute amount | 
**currency** | **str** | The currency code | 
**status** | **str** | The status of the dispute | 
**reason** | **str** | The reason for the dispute | [optional] 
**editable** | **bool** | Whether the evidence is still editable | 
**needs_response_by** | **datetime** | Timestamp by when evidence must be submitted | [optional] 
**visa_rdr** | **bool** | Whether Visa RDR was applied | 
**billing_address** | **str** | Customer billing address details | [optional] 
**customer_name** | **str** | Customer name | [optional] 
**customer_email** | **str** | Customer email address | [optional] 
**notes** | **str** | Additional notes | [optional] 
**product_description** | **str** | Product or service description | [optional] 
**service_date** | **str** | Service or purchase date | [optional] 
**access_activity_log** | **str** | Log of access activity | [optional] 
**evidence** | [**DisputeEvidenceDto**](DisputeEvidenceDto.md) | Evidence attachments associated with the dispute | [optional] 
**payment_id** | **str** | The associated payment ID | 
**business_id** | **str** | The associated business ID | 
**created_at** | **datetime** | Timestamp when the dispute was created | 
**updated_at** | **datetime** | Timestamp when the dispute was last updated | 

## Example

```python
from solifyn.models.dispute import Dispute

# TODO update the JSON string below
json = "{}"
# create an instance of Dispute from a JSON string
dispute_instance = Dispute.from_json(json)
# print the JSON string representation of the object
print(Dispute.to_json())

# convert the object into a dict
dispute_dict = dispute_instance.to_dict()
# create an instance of Dispute from a dict
dispute_from_dict = Dispute.from_dict(dispute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


