# CollectionProductEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The product ID (whopId or internal database ID) | 
**quantity** | **float** | Quantity of this product in the collection. Required, defaults to 1. | [default to 1]

## Example

```python
from solifyn.models.collection_product_entry import CollectionProductEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionProductEntry from a JSON string
collection_product_entry_instance = CollectionProductEntry.from_json(json)
# print the JSON string representation of the object
print(CollectionProductEntry.to_json())

# convert the object into a dict
collection_product_entry_dict = collection_product_entry_instance.to_dict()
# create an instance of CollectionProductEntry from a dict
collection_product_entry_from_dict = CollectionProductEntry.from_dict(collection_product_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


