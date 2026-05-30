# MeterIngestRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[MeterIngestEventDto]**](MeterIngestEventDto.md) | List of usage events to ingest. | 

## Example

```python
from solifyn.models.meter_ingest_request_dto import MeterIngestRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterIngestRequestDto from a JSON string
meter_ingest_request_dto_instance = MeterIngestRequestDto.from_json(json)
# print the JSON string representation of the object
print(MeterIngestRequestDto.to_json())

# convert the object into a dict
meter_ingest_request_dto_dict = meter_ingest_request_dto_instance.to_dict()
# create an instance of MeterIngestRequestDto from a dict
meter_ingest_request_dto_from_dict = MeterIngestRequestDto.from_dict(meter_ingest_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


