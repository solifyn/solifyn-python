# MeterEventsResponseDto

Represents a paginated-like response containing recent usage events recorded for a meter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meter_id** | **str** | The unique meter ID. | 
**items** | [**List[MeterUsageEventDto]**](MeterUsageEventDto.md) | List of recent usage events. | 
**count** | **float** | Number of returned usage events. | 

## Example

```python
from solifyn.models.meter_events_response_dto import MeterEventsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterEventsResponseDto from a JSON string
meter_events_response_dto_instance = MeterEventsResponseDto.from_json(json)
# print the JSON string representation of the object
print(MeterEventsResponseDto.to_json())

# convert the object into a dict
meter_events_response_dto_dict = meter_events_response_dto_instance.to_dict()
# create an instance of MeterEventsResponseDto from a dict
meter_events_response_dto_from_dict = MeterEventsResponseDto.from_dict(meter_events_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


