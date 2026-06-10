# DisputeEvidenceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_attachment** | [**DisputeAttachmentDto**](DisputeAttachmentDto.md) | Evidence showing cancellation policy details | [optional] 
**customer_communication_attachment** | [**DisputeAttachmentDto**](DisputeAttachmentDto.md) | Evidence demonstrating communications with the customer | [optional] 
**refund_policy_attachment** | [**DisputeAttachmentDto**](DisputeAttachmentDto.md) | Evidence showing refund policy details | [optional] 
**uncategorized_attachment** | [**DisputeAttachmentDto**](DisputeAttachmentDto.md) | Uncategorized supporting files or documents | [optional] 

## Example

```python
from solifyn.models.dispute_evidence_update import DisputeEvidenceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeEvidenceUpdate from a JSON string
dispute_evidence_update_instance = DisputeEvidenceUpdate.from_json(json)
# print the JSON string representation of the object
print(DisputeEvidenceUpdate.to_json())

# convert the object into a dict
dispute_evidence_update_dict = dispute_evidence_update_instance.to_dict()
# create an instance of DisputeEvidenceUpdate from a dict
dispute_evidence_update_from_dict = DisputeEvidenceUpdate.from_dict(dispute_evidence_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


