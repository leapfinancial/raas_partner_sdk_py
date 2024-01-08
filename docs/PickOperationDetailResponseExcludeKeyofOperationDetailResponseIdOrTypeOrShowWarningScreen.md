# PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen

From T, pick a set of properties whose keys are in the union K

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**created_at** | **datetime** |  | 
**amount** | **float** |  | 
**status** | **str** |  | 
**code** | **str** |  | 
**recipient_amout** | **float** |  | 
**from_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**to_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**plat_id** | **str** |  | [optional] 
**status_details** | **str** |  | [optional] 
**mobile_status** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**sender_amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**sender_currency** | **str** |  | [optional] 
**recipient_currency** | **str** |  | [optional] 
**source_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**destination_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**source_fee** | **float** |  | [optional] 
**transaction_fee** | **float** |  | [optional] 
**destination_fee** | **float** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**has_reference_code** | **bool** |  | [optional] 
**attribution_link** | **str** |  | [optional] 
**is_ignored** | **bool** |  | [optional] 
**ignored_data** | [**IgnoredOperationData**](IgnoredOperationData.md) |  | [optional] 
**tenantfee** | **float** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


