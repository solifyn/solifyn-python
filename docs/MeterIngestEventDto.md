# MeterIngestEventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique usage event ID for idempotency. | 
**customer_id** | **str** | Unique customer ID associated with the event. | 
**event_name** | **str** | Event name that should match a meter eventName. | 
**value** | **float** | Event quantity value. | [optional] [default to 1]
**metadata** | **Dict[str, object]** | Metadata attached to the usage event. | [optional] 
**timestamp** | **str** | Timestamp of the event in ISO 8601 format. | [optional] 

## Example

```python
from solifyn.models.meter_ingest_event_dto import MeterIngestEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterIngestEventDto from a JSON string
meter_ingest_event_dto_instance = MeterIngestEventDto.from_json(json)
# print the JSON string representation of the object
print(MeterIngestEventDto.to_json())

# convert the object into a dict
meter_ingest_event_dto_dict = meter_ingest_event_dto_instance.to_dict()
# create an instance of MeterIngestEventDto from a dict
meter_ingest_event_dto_from_dict = MeterIngestEventDto.from_dict(meter_ingest_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


