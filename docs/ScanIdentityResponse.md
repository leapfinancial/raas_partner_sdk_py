# ScanIdentityResponse

After scan using an non sync engine, API will return this object A client has to pull the data from this object's pull_url  until the status is a ScanIdentityResponse or \"error\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** | If it&#39;s async the client has to pull the data from this url | 
**estimated_time** | **float** | Estimated time in seconds. | [optional] 
**method** | **str** | What scan engine was used | [optional] 
**pull_url** | **str** | Url to pull the data. If the type&#x3D;sync you have perform interval pulls to this url in order to monitor the status | [optional] 
**data** | [**BaseIdentity**](BaseIdentity.md) |  | [optional] 
**attachment_responses** | [**AttachmentResponses**](AttachmentResponses.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


