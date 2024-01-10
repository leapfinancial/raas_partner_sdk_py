# openapi_client.DefaultApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bank_account**](DefaultApi.md#add_bank_account) | **POST** /user/funding/source/bank/add/{userToken} | 
[**add_card**](DefaultApi.md#add_card) | **POST** /user/funding/source/card/add/{userToken} | 
[**create_contact**](DefaultApi.md#create_contact) | **POST** /user/contacts/{userToken} | 
[**create_pin**](DefaultApi.md#create_pin) | **POST** /user/pin | 
[**delete_payment_method**](DefaultApi.md#delete_payment_method) | **POST** /user/funding/source/delete/{userToken} | 
[**get_available_operation_type**](DefaultApi.md#get_available_operation_type) | **GET** /user/corridors/available-operations/{userToken} | 
[**get_available_payment_methods**](DefaultApi.md#get_available_payment_methods) | **GET** /user/corridors/available-methods/{userToken} | 
[**get_cash_operators**](DefaultApi.md#get_cash_operators) | **POST** /user/funding/cash/operators/{userToken} | 
[**get_cip_info**](DefaultApi.md#get_cip_info) | **GET** /cip/process/{phoneNumber} | 
[**get_corridors**](DefaultApi.md#get_corridors) | **GET** /user/corridors | 
[**get_destination_sof_for_requet_money_operation**](DefaultApi.md#get_destination_sof_for_requet_money_operation) | **GET** /user/funding/source/request-money/{userToken} | 
[**get_exchange_rates**](DefaultApi.md#get_exchange_rates) | **GET** /user/exchange-rates/exchange-rates | 
[**get_in_and_out_operations**](DefaultApi.md#get_in_and_out_operations) | **GET** /user/operations/in-out/{userToken} | 
[**get_operation**](DefaultApi.md#get_operation) | **GET** /user/operations/detail/{id} | 
[**get_operation_quote**](DefaultApi.md#get_operation_quote) | **POST** /user/operations/quotation/{userToken} | 
[**get_payment_method**](DefaultApi.md#get_payment_method) | **GET** /user/funding/source/get-payment-method/{userToken} | 
[**get_payment_method_v2**](DefaultApi.md#get_payment_method_v2) | **GET** /user/funding/source/get-payment-method-v2/{userToken} | 
[**get_profile**](DefaultApi.md#get_profile) | **GET** /user/profile/{phone} | 
[**get_redis_status**](DefaultApi.md#get_redis_status) | **GET** /system/status/redis | 
[**get_session_link**](DefaultApi.md#get_session_link) | **POST** /auth/sessionlink | 
[**get_sof_for_send_money_operation**](DefaultApi.md#get_sof_for_send_money_operation) | **GET** /user/funding/source/send-money/{userToken} | 
[**get_user_token**](DefaultApi.md#get_user_token) | **POST** /auth/get-user-token | 
[**get_while_label_link**](DefaultApi.md#get_while_label_link) | **POST** /auth/white-label-link | 
[**is_phone_available**](DefaultApi.md#is_phone_available) | **POST** /auth/is-phone-available | 
[**list_contacts**](DefaultApi.md#list_contacts) | **GET** /user/contacts/{userToken} | 
[**perform_level_one**](DefaultApi.md#perform_level_one) | **POST** /cip/level/one/{phoneNumber} | 
[**perform_resubmit_upgrade_level**](DefaultApi.md#perform_resubmit_upgrade_level) | **POST** /cip/level/resubmit-upgrade | 
[**pre_quote**](DefaultApi.md#pre_quote) | **POST** /user/operations/pre-quote/{userToken} | 
[**receive**](DefaultApi.md#receive) | **POST** /user/operations/receive-money/{userToken} | 
[**register_user**](DefaultApi.md#register_user) | **POST** /auth/register-user | 
[**register_user_v2**](DefaultApi.md#register_user_v2) | **POST** /auth/register-user-v2 | 
[**request_otp**](DefaultApi.md#request_otp) | **POST** /auth/request-otp | 
[**request_v2**](DefaultApi.md#request_v2) | **POST** /user/operations/request-money-v2/{userToken} | 
[**send**](DefaultApi.md#send) | **POST** /user/operations/send-money/{userToken} | 
[**set_alternate_cip**](DefaultApi.md#set_alternate_cip) | **POST** /cip/alternate | 
[**set_level_two**](DefaultApi.md#set_level_two) | **POST** /cip/level/two/{phoneNumber} | 
[**set_reference_code**](DefaultApi.md#set_reference_code) | **POST** /user/funding/cash/reference-code/{userToken} | 
[**set_trusted_level_two**](DefaultApi.md#set_trusted_level_two) | **POST** /cip/level/two/{phoneNumber}/trusted | 
[**status**](DefaultApi.md#status) | **GET** /user/operations/status/{userToken}/{operationId} | 
[**update_profile**](DefaultApi.md#update_profile) | **PUT** /user/profile/{phone} | 
[**updated_contact**](DefaultApi.md#updated_contact) | **PUT** /user/contacts/{userToken} | 
[**validate_otp**](DefaultApi.md#validate_otp) | **POST** /auth/validate-otp | 
[**validate_phone_number**](DefaultApi.md#validate_phone_number) | **POST** /auth/validate-phone | 
[**validate_pin_code**](DefaultApi.md#validate_pin_code) | **POST** /user/validate-pincode | 


# **add_bank_account**
> add_bank_account(user_token, add_bank_account_params_base)



adds bank account to subscriber's source of funding

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.add_bank_account_params_base import AddBankAccountParamsBase
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    add_bank_account_params_base = openapi_client.AddBankAccountParamsBase() # AddBankAccountParamsBase | 

    try:
        api_instance.add_bank_account(user_token, add_bank_account_params_base)
    except Exception as e:
        print("Exception when calling DefaultApi->add_bank_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **add_bank_account_params_base** | [**AddBankAccountParamsBase**](AddBankAccountParamsBase.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_card**
> AddPaymentMethodResponse add_card(user_token, add_card_partner_params)



adds a card to subscriber's source of funding

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.add_card_partner_params import AddCardPartnerParams
from openapi_client.models.add_payment_method_response import AddPaymentMethodResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    add_card_partner_params = openapi_client.AddCardPartnerParams() # AddCardPartnerParams | 

    try:
        api_response = api_instance.add_card(user_token, add_card_partner_params)
        print("The response of DefaultApi->add_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_card: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **add_card_partner_params** | [**AddCardPartnerParams**](AddCardPartnerParams.md)|  | 

### Return type

[**AddPaymentMethodResponse**](AddPaymentMethodResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> create_contact(user_token, create_contact_request_params_partner)



Create a contact for a user

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_contact_request_params_partner import CreateContactRequestParamsPartner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    create_contact_request_params_partner = openapi_client.CreateContactRequestParamsPartner() # CreateContactRequestParamsPartner | 

    try:
        api_instance.create_contact(user_token, create_contact_request_params_partner)
    except Exception as e:
        print("Exception when calling DefaultApi->create_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. | 
 **create_contact_request_params_partner** | [**CreateContactRequestParamsPartner**](CreateContactRequestParamsPartner.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  |  -  |
**422** | Validation Failed |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pin**
> create_pin(set_pincode_params_partner)



Creates a pincode for the user.  The pincode must be 6 digits long and only numeric characters are allowed.  If the user already has a pincode, an error will be returned.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.set_pincode_params_partner import SetPincodeParamsPartner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    set_pincode_params_partner = openapi_client.SetPincodeParamsPartner() # SetPincodeParamsPartner | 

    try:
        api_instance.create_pin(set_pincode_params_partner)
    except Exception as e:
        print("Exception when calling DefaultApi->create_pin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_pincode_params_partner** | [**SetPincodeParamsPartner**](SetPincodeParamsPartner.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(user_token, payment_method_id)



removes a payment method

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | 

    try:
        api_instance.delete_payment_method(user_token, payment_method_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **payment_method_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_operation_type**
> List[str] get_available_operation_type(user_token, destination_country=destination_country)



Gets available operation types by user country (as source country) and destination country. A corridor is a way to configure available operation between two subscribers.  NOTICE: if an operation is RequestFunds from A to B, you may search for a SendFunds from B to A to determine if operation is available. Probabily you'll not find a RequestFunds option as such.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    destination_country = 'destination_country_example' # str | ISO 3166 2-alpha (optional)

    try:
        api_response = api_instance.get_available_operation_type(user_token, destination_country=destination_country)
        print("The response of DefaultApi->get_available_operation_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_available_operation_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **destination_country** | **str**| ISO 3166 2-alpha | [optional] 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | string[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_payment_methods**
> List[str] get_available_payment_methods(user_token, destination_country=destination_country, operation_type=operation_type)



Gets available payment method types by source country, destination country and operation type. A corridor is a way to configure available operation between two subscribers.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    destination_country = 'destination_country_example' # str | ISO 3166 2-alpha (optional)
    operation_type = 'SendFunds' # str | SendFunds | RequestFunds (optional) (default to 'SendFunds')

    try:
        api_response = api_instance.get_available_payment_methods(user_token, destination_country=destination_country, operation_type=operation_type)
        print("The response of DefaultApi->get_available_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_available_payment_methods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **destination_country** | **str**| ISO 3166 2-alpha | [optional] 
 **operation_type** | **str**| SendFunds | RequestFunds | [optional] [default to &#39;SendFunds&#39;]

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | string[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_operators**
> List[CashOperators] get_cash_operators(user_token, cash_operators_params_base)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.cash_operators import CashOperators
from openapi_client.models.cash_operators_params_base import CashOperatorsParamsBase
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    cash_operators_params_base = openapi_client.CashOperatorsParamsBase() # CashOperatorsParamsBase | 

    try:
        api_response = api_instance.get_cash_operators(user_token, cash_operators_params_base)
        print("The response of DefaultApi->get_cash_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_cash_operators: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **cash_operators_params_base** | [**CashOperatorsParamsBase**](CashOperatorsParamsBase.md)|  | 

### Return type

[**List[CashOperators]**](CashOperators.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cip_info**
> PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC get_cip_info(phone_number)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_response = api_instance.get_cip_info(phone_number)
        print("The response of DefaultApi->get_cip_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_cip_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 

### Return type

[**PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC**](PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corridors**
> List[CorridorDTO] get_corridors(source_country=source_country, destination_country=destination_country, operation_type=operation_type)



Gets corridors by source country, destination country and operation type. A corridor is a way to configure available operation between two subscribers.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.corridor_dto import CorridorDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    source_country = 'source_country_example' # str | ISO 3166 2-alpha (optional)
    destination_country = 'destination_country_example' # str | ISO 3166 2-alpha (optional)
    operation_type = 'SendFunds' # str | SendFunds | RequestFunds (optional) (default to 'SendFunds')

    try:
        api_response = api_instance.get_corridors(source_country=source_country, destination_country=destination_country, operation_type=operation_type)
        print("The response of DefaultApi->get_corridors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_corridors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_country** | **str**| ISO 3166 2-alpha | [optional] 
 **destination_country** | **str**| ISO 3166 2-alpha | [optional] 
 **operation_type** | **str**| SendFunds | RequestFunds | [optional] [default to &#39;SendFunds&#39;]

### Return type

[**List[CorridorDTO]**](CorridorDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CorridorDTO[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_sof_for_requet_money_operation**
> List[SourceOfFunding] get_destination_sof_for_requet_money_operation(user_token, source_country=source_country, destination_country=destination_country)



gets destination sources of funding for request funds

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.source_of_funding import SourceOfFunding
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    source_country = 'source_country_example' # str |  (optional)
    destination_country = 'destination_country_example' # str |  (optional)

    try:
        api_response = api_instance.get_destination_sof_for_requet_money_operation(user_token, source_country=source_country, destination_country=destination_country)
        print("The response of DefaultApi->get_destination_sof_for_requet_money_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_destination_sof_for_requet_money_operation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **source_country** | **str**|  | [optional] 
 **destination_country** | **str**|  | [optional] 

### Return type

[**List[SourceOfFunding]**](SourceOfFunding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_rates**
> List[ExchangeRateDTO] get_exchange_rates(currency_code_src=currency_code_src, currency_code_dest=currency_code_dest)



Gets exchange rates between currencies

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.exchange_rate_dto import ExchangeRateDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    currency_code_src = 'currency_code_src_example' # str | ISO 4217 3-alpha (optional)
    currency_code_dest = 'currency_code_dest_example' # str | ISO 4217 3-alpha (optional)

    try:
        api_response = api_instance.get_exchange_rates(currency_code_src=currency_code_src, currency_code_dest=currency_code_dest)
        print("The response of DefaultApi->get_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_exchange_rates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code_src** | **str**| ISO 4217 3-alpha | [optional] 
 **currency_code_dest** | **str**| ISO 4217 3-alpha | [optional] 

### Return type

[**List[ExchangeRateDTO]**](ExchangeRateDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExchangeRate[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_in_and_out_operations**
> List[OperationDetailResponse] get_in_and_out_operations(user_token, to_phone_number=to_phone_number)



Return all the in and outs operations for an user given his userId

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.operation_detail_response import OperationDetailResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    to_phone_number = 'to_phone_number_example' # str |  (optional)

    try:
        api_response = api_instance.get_in_and_out_operations(user_token, to_phone_number=to_phone_number)
        print("The response of DefaultApi->get_in_and_out_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_in_and_out_operations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **to_phone_number** | **str**|  | [optional] 

### Return type

[**List[OperationDetailResponse]**](OperationDetailResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation**
> OperationDetail get_operation(id)



Gets operation detail by id

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.operation_detail import OperationDetail
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | Operation Id

    try:
        api_response = api_instance.get_operation(id)
        print("The response of DefaultApi->get_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_operation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Operation Id | 

### Return type

[**OperationDetail**](OperationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_quote**
> RaasQuoteTransactionResponse get_operation_quote(user_token, quote_transaction_base)



 Retrieve quote for the operation

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.quote_transaction_base import QuoteTransactionBase
from openapi_client.models.raas_quote_transaction_response import RaasQuoteTransactionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    quote_transaction_base = openapi_client.QuoteTransactionBase() # QuoteTransactionBase | {@link QuoteTransactionBase}

    try:
        api_response = api_instance.get_operation_quote(user_token, quote_transaction_base)
        print("The response of DefaultApi->get_operation_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_operation_quote: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **quote_transaction_base** | [**QuoteTransactionBase**](QuoteTransactionBase.md)| {@link QuoteTransactionBase} | 

### Return type

[**RaasQuoteTransactionResponse**](RaasQuoteTransactionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quotation data |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> RaaSPaymentMethod get_payment_method(user_token, number=number)



Retrieve a payment method by number

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.raa_s_payment_method import RaaSPaymentMethod
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    number = '' # str |  (optional) (default to '')

    try:
        api_response = api_instance.get_payment_method(user_token, number=number)
        print("The response of DefaultApi->get_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_payment_method: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **number** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**RaaSPaymentMethod**](RaaSPaymentMethod.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link PaymentMethod} |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_v2**
> RaaSPartnerPaymentMethod get_payment_method_v2(user_token, id=id)



Retrieve a payment method by ID

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.raa_s_partner_payment_method import RaaSPartnerPaymentMethod
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    id = '' # str |  (optional) (default to '')

    try:
        api_response = api_instance.get_payment_method_v2(user_token, id=id)
        print("The response of DefaultApi->get_payment_method_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_payment_method_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**RaaSPartnerPaymentMethod**](RaaSPartnerPaymentMethod.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link PaymentMethod} |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> User get_profile(phone)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    phone = 'phone_example' # str | 

    try:
        api_response = api_instance.get_profile(phone)
        print("The response of DefaultApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**404** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redis_status**
> GetRedisStatus200Response get_redis_status()



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_redis_status200_response import GetRedisStatus200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.get_redis_status()
        print("The response of DefaultApi->get_redis_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_redis_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRedisStatus200Response**](GetRedisStatus200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_link**
> SessionLinkResponse get_session_link(session_link_params)



Generates Partner API Link Token.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.session_link_params import SessionLinkParams
from openapi_client.models.session_link_response import SessionLinkResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    session_link_params = openapi_client.SessionLinkParams() # SessionLinkParams | {@link SessionLinkParams}

    try:
        api_response = api_instance.get_session_link(session_link_params)
        print("The response of DefaultApi->get_session_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_session_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_link_params** | [**SessionLinkParams**](SessionLinkParams.md)| {@link SessionLinkParams} | 

### Return type

[**SessionLinkResponse**](SessionLinkResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sof_for_send_money_operation**
> List[SourceOfFunding] get_sof_for_send_money_operation(user_token, source_country=source_country, destination_country=destination_country)



gets sources of funding for send funds

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.source_of_funding import SourceOfFunding
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    source_country = 'source_country_example' # str |  (optional)
    destination_country = 'destination_country_example' # str |  (optional)

    try:
        api_response = api_instance.get_sof_for_send_money_operation(user_token, source_country=source_country, destination_country=destination_country)
        print("The response of DefaultApi->get_sof_for_send_money_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sof_for_send_money_operation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **source_country** | **str**|  | [optional] 
 **destination_country** | **str**|  | [optional] 

### Return type

[**List[SourceOfFunding]**](SourceOfFunding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token**
> UserTokenResponse get_user_token(get_user_token_params)



Partner API Token.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_user_token_params import GetUserTokenParams
from openapi_client.models.user_token_response import UserTokenResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    get_user_token_params = openapi_client.GetUserTokenParams() # GetUserTokenParams | {@link GetUserTokenParams}

    try:
        api_response = api_instance.get_user_token(get_user_token_params)
        print("The response of DefaultApi->get_user_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_user_token_params** | [**GetUserTokenParams**](GetUserTokenParams.md)| {@link GetUserTokenParams} | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_while_label_link**
> SessionLinkResponse get_while_label_link()



Generates Partner API White Label Link Token.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.session_link_response import SessionLinkResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.get_while_label_link()
        print("The response of DefaultApi->get_while_label_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_while_label_link: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionLinkResponse**](SessionLinkResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_phone_available**
> IsPhoneAvailableResponse is_phone_available(is_phone_available_request)



Verify is the phone number is available for registration.  It is used to check if the phone number is already registered. Returns true if the phone number is available.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.is_phone_available_request import IsPhoneAvailableRequest
from openapi_client.models.is_phone_available_response import IsPhoneAvailableResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    is_phone_available_request = openapi_client.IsPhoneAvailableRequest() # IsPhoneAvailableRequest | 

    try:
        api_response = api_instance.is_phone_available(is_phone_available_request)
        print("The response of DefaultApi->is_phone_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->is_phone_available: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_phone_available_request** | [**IsPhoneAvailableRequest**](IsPhoneAvailableRequest.md)|  | 

### Return type

[**IsPhoneAvailableResponse**](IsPhoneAvailableResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> List[ContactInfo] list_contacts(user_token)



Retrieve all contacts for a user

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.contact_info import ContactInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.

    try:
        api_response = api_instance.list_contacts(user_token)
        print("The response of DefaultApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_contacts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. | 

### Return type

[**List[ContactInfo]**](ContactInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact List |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_level_one**
> perform_level_one(phone_number, perform_level_one_params)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.perform_level_one_params import PerformLevelOneParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    phone_number = 'phone_number_example' # str | 
    perform_level_one_params = openapi_client.PerformLevelOneParams() # PerformLevelOneParams | 

    try:
        api_instance.perform_level_one(phone_number, perform_level_one_params)
    except Exception as e:
        print("Exception when calling DefaultApi->perform_level_one: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 
 **perform_level_one_params** | [**PerformLevelOneParams**](PerformLevelOneParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_resubmit_upgrade_level**
> perform_resubmit_upgrade_level(perform_resubmit_upgrade_level_params)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.perform_resubmit_upgrade_level_params import PerformResubmitUpgradeLevelParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    perform_resubmit_upgrade_level_params = openapi_client.PerformResubmitUpgradeLevelParams() # PerformResubmitUpgradeLevelParams | 

    try:
        api_instance.perform_resubmit_upgrade_level(perform_resubmit_upgrade_level_params)
    except Exception as e:
        print("Exception when calling DefaultApi->perform_resubmit_upgrade_level: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perform_resubmit_upgrade_level_params** | [**PerformResubmitUpgradeLevelParams**](PerformResubmitUpgradeLevelParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_quote**
> RaasPreQuoteResponse pre_quote(user_token, raas_pre_quote_request)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.raas_pre_quote_request import RaasPreQuoteRequest
from openapi_client.models.raas_pre_quote_response import RaasPreQuoteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    raas_pre_quote_request = openapi_client.RaasPreQuoteRequest() # RaasPreQuoteRequest | 

    try:
        api_response = api_instance.pre_quote(user_token, raas_pre_quote_request)
        print("The response of DefaultApi->pre_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pre_quote: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **raas_pre_quote_request** | [**RaasPreQuoteRequest**](RaasPreQuoteRequest.md)|  | 

### Return type

[**RaasPreQuoteResponse**](RaasPreQuoteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive**
> receive(user_token, receive_money_params)



Receive funds

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.receive_money_params import ReceiveMoneyParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    receive_money_params = openapi_client.ReceiveMoneyParams() # ReceiveMoneyParams | {@link ReceiveMoneyParams}

    try:
        api_instance.receive(user_token, receive_money_params)
    except Exception as e:
        print("Exception when calling DefaultApi->receive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **receive_money_params** | [**ReceiveMoneyParams**](ReceiveMoneyParams.md)| {@link ReceiveMoneyParams} | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> UserTokenResponse register_user(register_user_params)



Registers Partner user. If user exists, return its id.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.register_user_params import RegisterUserParams
from openapi_client.models.user_token_response import UserTokenResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    register_user_params = openapi_client.RegisterUserParams() # RegisterUserParams | {@link RegisterUserParams}

    try:
        api_response = api_instance.register_user(register_user_params)
        print("The response of DefaultApi->register_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_params** | [**RegisterUserParams**](RegisterUserParams.md)| {@link RegisterUserParams} | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user_v2**
> UserTokenResponse register_user_v2(register_user_params)



Registers Partner user. If user exists, return its id.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.register_user_params import RegisterUserParams
from openapi_client.models.user_token_response import UserTokenResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    register_user_params = openapi_client.RegisterUserParams() # RegisterUserParams | {@link RegisterUserParams}

    try:
        api_response = api_instance.register_user_v2(register_user_params)
        print("The response of DefaultApi->register_user_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_user_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_params** | [**RegisterUserParams**](RegisterUserParams.md)| {@link RegisterUserParams} | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_otp**
> request_otp(request_otp_params)



Request OTP for phone number. The phone number must be registered. Using /register endpoint.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.request_otp_params import RequestOTPParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    request_otp_params = openapi_client.RequestOTPParams() # RequestOTPParams | 

    try:
        api_instance.request_otp(request_otp_params)
    except Exception as e:
        print("Exception when calling DefaultApi->request_otp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_otp_params** | [**RequestOTPParams**](RequestOTPParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Code Sent |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_v2**
> PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen request_v2(user_token, request_money_partner_params)



Request money to a contact

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen import PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen
from openapi_client.models.request_money_partner_params import RequestMoneyPartnerParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    request_money_partner_params = openapi_client.RequestMoneyPartnerParams() # RequestMoneyPartnerParams | {@link RequestMoneyParams}

    try:
        api_response = api_instance.request_v2(user_token, request_money_partner_params)
        print("The response of DefaultApi->request_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->request_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **request_money_partner_params** | [**RequestMoneyPartnerParams**](RequestMoneyPartnerParams.md)| {@link RequestMoneyParams} | 

### Return type

[**PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen**](PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link RequestMoneyResponse} |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> SendMoneyResponse send(user_token, send_money_params)



Send funds to a requester

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.send_money_params import SendMoneyParams
from openapi_client.models.send_money_response import SendMoneyResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    send_money_params = openapi_client.SendMoneyParams() # SendMoneyParams | {@link SendMoneyParams}

    try:
        api_response = api_instance.send(user_token, send_money_params)
        print("The response of DefaultApi->send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->send: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **send_money_params** | [**SendMoneyParams**](SendMoneyParams.md)| {@link SendMoneyParams} | 

### Return type

[**SendMoneyResponse**](SendMoneyResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alternate_cip**
> set_alternate_cip(type)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.alternate_flow import AlternateFlow
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    type = openapi_client.AlternateFlow() # AlternateFlow | 

    try:
        api_instance.set_alternate_cip(type)
    except Exception as e:
        print("Exception when calling DefaultApi->set_alternate_cip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AlternateFlow**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_level_two**
> set_level_two(phone_number, level_two_params)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.level_two_params import LevelTwoParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    phone_number = 'phone_number_example' # str | 
    level_two_params = openapi_client.LevelTwoParams() # LevelTwoParams | 

    try:
        api_instance.set_level_two(phone_number, level_two_params)
    except Exception as e:
        print("Exception when calling DefaultApi->set_level_two: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 
 **level_two_params** | [**LevelTwoParams**](LevelTwoParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_reference_code**
> GetReferenceCodeResponse set_reference_code(user_token, set_reference_code_params_base)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_reference_code_response import GetReferenceCodeResponse
from openapi_client.models.set_reference_code_params_base import SetReferenceCodeParamsBase
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    set_reference_code_params_base = openapi_client.SetReferenceCodeParamsBase() # SetReferenceCodeParamsBase | 

    try:
        api_response = api_instance.set_reference_code(user_token, set_reference_code_params_base)
        print("The response of DefaultApi->set_reference_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_reference_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **set_reference_code_params_base** | [**SetReferenceCodeParamsBase**](SetReferenceCodeParamsBase.md)|  | 

### Return type

[**GetReferenceCodeResponse**](GetReferenceCodeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_trusted_level_two**
> set_trusted_level_two(phone_number)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        api_instance.set_trusted_level_two(phone_number)
    except Exception as e:
        print("Exception when calling DefaultApi->set_trusted_level_two: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> str status(user_token, operation_id)



Gets operation status

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | 
    operation_id = 'operation_id_example' # str | 

    try:
        api_response = api_instance.status(user_token, operation_id)
        print("The response of DefaultApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  | 
 **operation_id** | **str**|  | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> update_profile(phone, user_update_params)



Updates user profile

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.user_update_params import UserUpdateParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    phone = 'phone_example' # str | 
    user_update_params = openapi_client.UserUpdateParams() # UserUpdateParams | 

    try:
        api_instance.update_profile(phone, user_update_params)
    except Exception as e:
        print("Exception when calling DefaultApi->update_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **user_update_params** | [**UserUpdateParams**](UserUpdateParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**404** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updated_contact**
> updated_contact(user_token, update_contact_request_params)



Update a contact for a user

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.update_contact_request_params import UpdateContactRequestParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_token = 'user_token_example' # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    update_contact_request_params = openapi_client.UpdateContactRequestParams() # UpdateContactRequestParams | 

    try:
        api_instance.updated_contact(user_token, update_contact_request_params)
    except Exception as e:
        print("Exception when calling DefaultApi->updated_contact: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. | 
 **update_contact_request_params** | [**UpdateContactRequestParams**](UpdateContactRequestParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**422** | Validation Failed |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_otp**
> validate_otp(body)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.pick_validate_otp_params_exclude_keyof_validate_otp_params_device_id import PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    body = openapi_client.PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId() # PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId | 

    try:
        api_instance.validate_otp(body)
    except Exception as e:
        print("Exception when calling DefaultApi->validate_otp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_phone_number**
> str validate_phone_number(validate_phone_number_request)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.validate_phone_number_request import ValidatePhoneNumberRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    validate_phone_number_request = openapi_client.ValidatePhoneNumberRequest() # ValidatePhoneNumberRequest | 

    try:
        api_response = api_instance.validate_phone_number(validate_phone_number_request)
        print("The response of DefaultApi->validate_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->validate_phone_number: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_phone_number_request** | [**ValidatePhoneNumberRequest**](ValidatePhoneNumberRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_pin_code**
> validate_pin_code(body)



### Example

* Api Key Authentication (api_key):
```python
import time
import os
import openapi_client
from openapi_client.models.pick_validate_pin_code_params_exclude_keyof_validate_pin_code_params_device_id import PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    body = openapi_client.PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId() # PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId | 

    try:
        api_instance.validate_pin_code(body)
    except Exception as e:
        print("Exception when calling DefaultApi->validate_pin_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid pincode |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

