# MeterIngestResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed** | **float** | Number of successfully processed events. | 
**failed** | **float** | Number of failed events. | 
**errors** | **List[object]** | List of errors encountered during ingestion. | 

## Example

```python
from solifyn.models.meter_ingest_response_dto import MeterIngestResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterIngestResponseDto from a JSON string
meter_ingest_response_dto_instance = MeterIngestResponseDto.from_json(json)
# print the JSON string representation of the object
print(MeterIngestResponseDto.to_json())

# convert the object into a dict
meter_ingest_response_dto_dict = meter_ingest_response_dto_instance.to_dict()
# create an instance of MeterIngestResponseDto from a dict
meter_ingest_response_dto_from_dict = MeterIngestResponseDto.from_dict(meter_ingest_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


