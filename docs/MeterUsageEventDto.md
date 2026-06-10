# MeterUsageEventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique usage event ID. | 
**meter_id** | **str** | The meter ID this event belongs to. | 
**customer_id** | **str** | The customer ID associated with the usage event. | 
**value** | **float** | Numeric usage value recorded for the event. | 
**metadata** | **Dict[str, object]** | Optional event metadata. | [optional] 
**timestamp** | **datetime** | Timestamp when the usage event occurred. | 
**processed_at** | **datetime** | Timestamp when the usage event was processed. | 

## Example

```python
from solifyn.models.meter_usage_event_dto import MeterUsageEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterUsageEventDto from a JSON string
meter_usage_event_dto_instance = MeterUsageEventDto.from_json(json)
# print the JSON string representation of the object
print(MeterUsageEventDto.to_json())

# convert the object into a dict
meter_usage_event_dto_dict = meter_usage_event_dto_instance.to_dict()
# create an instance of MeterUsageEventDto from a dict
meter_usage_event_dto_from_dict = MeterUsageEventDto.from_dict(meter_usage_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


