# DisputeEvidenceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy** | **str** | Cancellation policy attachment ID | [optional] 
**customer_communication** | **str** | Customer communication attachment ID | [optional] 
**refund_policy** | **str** | Refund policy attachment ID | [optional] 
**uncategorized** | **str** | Uncategorized attachment ID | [optional] 

## Example

```python
from solifyn.models.dispute_evidence_dto import DisputeEvidenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeEvidenceDto from a JSON string
dispute_evidence_dto_instance = DisputeEvidenceDto.from_json(json)
# print the JSON string representation of the object
print(DisputeEvidenceDto.to_json())

# convert the object into a dict
dispute_evidence_dto_dict = dispute_evidence_dto_instance.to_dict()
# create an instance of DisputeEvidenceDto from a dict
dispute_evidence_dto_from_dict = DisputeEvidenceDto.from_dict(dispute_evidence_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


