# FramerTemplateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique Framer template ID. | 
**business_id** | **str** | The business ID owning the template. | 
**name** | **str** | The name of the Framer template. | 
**remix_link** | **str** | The public Framer remix link. | 
**description** | **str** | A brief description of the template. | [optional] 
**created_at** | **str** | Creation timestamp. | 
**updated_at** | **str** | Modification timestamp. | 

## Example

```python
from solifyn.models.framer_template_response_dto import FramerTemplateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FramerTemplateResponseDto from a JSON string
framer_template_response_dto_instance = FramerTemplateResponseDto.from_json(json)
# print the JSON string representation of the object
print(FramerTemplateResponseDto.to_json())

# convert the object into a dict
framer_template_response_dto_dict = framer_template_response_dto_instance.to_dict()
# create an instance of FramerTemplateResponseDto from a dict
framer_template_response_dto_from_dict = FramerTemplateResponseDto.from_dict(framer_template_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


