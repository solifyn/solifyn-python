# UserSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID | 
**email** | **str** | Primary email address | 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**avatar_url** | **str** | Profile avatar image URL | [optional] 
**payout_threshold** | **float** | Auto-payout minimum threshold limit in cents | 
**notify_on_success** | **bool** | Auto-email receipt toggled | 
**send_license_key_email** | **bool** | Send license keys email automatically | 
**send_digital_file_email** | **bool** | Send digital delivery download link emails automatically | 

## Example

```python
from solifyn.models.user_settings import UserSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettings from a JSON string
user_settings_instance = UserSettings.from_json(json)
# print the JSON string representation of the object
print(UserSettings.to_json())

# convert the object into a dict
user_settings_dict = user_settings_instance.to_dict()
# create an instance of UserSettings from a dict
user_settings_from_dict = UserSettings.from_dict(user_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


