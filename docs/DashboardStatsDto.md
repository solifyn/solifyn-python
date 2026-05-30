# DashboardStatsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revenue** | **float** | Gross revenue in cents | 
**orders_count** | **float** | Total payments processed count | 
**refunds_count** | **float** | Gross amount refunded in cents | 
**active_memberships** | **float** | Number of active paying customers/memberships | 

## Example

```python
from solifyn.models.dashboard_stats_dto import DashboardStatsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardStatsDto from a JSON string
dashboard_stats_dto_instance = DashboardStatsDto.from_json(json)
# print the JSON string representation of the object
print(DashboardStatsDto.to_json())

# convert the object into a dict
dashboard_stats_dto_dict = dashboard_stats_dto_instance.to_dict()
# create an instance of DashboardStatsDto from a dict
dashboard_stats_dto_from_dict = DashboardStatsDto.from_dict(dashboard_stats_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


