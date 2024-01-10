# UserDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **object** |  | 
**sub_type** | **float** |  | 
**number** | **str** |  | 
**expiration_date** | **str** |  | [optional] 
**issued_country** | **str** |  | [optional] 
**issued_date** | **str** |  | [optional] 
**user_identity_data** | **Dict[str, object]** |  | [optional] 
**date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.user_document import UserDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDocument from a JSON string
user_document_instance = UserDocument.from_json(json)
# print the JSON string representation of the object
print UserDocument.to_json()

# convert the object into a dict
user_document_dict = user_document_instance.to_dict()
# create an instance of UserDocument from a dict
user_document_form_dict = user_document.from_dict(user_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


