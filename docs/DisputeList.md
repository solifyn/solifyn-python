# DisputeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Dispute]**](Dispute.md) | List of disputes | 
**meta** | [**DisputeListMetaDto**](DisputeListMetaDto.md) | Pagination metadata | 

## Example

```python
from solifyn.models.dispute_list import DisputeList

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeList from a JSON string
dispute_list_instance = DisputeList.from_json(json)
# print the JSON string representation of the object
print(DisputeList.to_json())

# convert the object into a dict
dispute_list_dict = dispute_list_instance.to_dict()
# create an instance of DisputeList from a dict
dispute_list_from_dict = DisputeList.from_dict(dispute_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


