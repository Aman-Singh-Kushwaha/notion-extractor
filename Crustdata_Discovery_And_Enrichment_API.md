# Crustdata Discovery And Enrichment API

Crustdata Discovery And Enrichment API![](/image/https%3A%2F%2Fbeestat.io%2Fimg%2Fnotion%2Fapi.svg?table=block&id=c66d5236-e8ea-40df-8af1-14f6d447ab48&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)Crustdata Discovery And Enrichment APIMade with![](https://images.unsplash.com/photo-1606606767399-01e271823a2e?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=3600)Drag image to reposition![Page icon](/image/https%3A%2F%2Fbeestat.io%2Fimg%2Fnotion%2Fapi.svg?table=block&id=c66d5236-e8ea-40df-8af1-14f6d447ab48&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)
# Crustdata Discovery And Enrichment API

[Introduction](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#3315bbdfa0054a2aa440e98bdec3ff90)[Getting Started](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#2436c68ecbf24ade8ad88e2f2a9ba70b)[Obtaining Authorization Token](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#52b36bde50314b648620fe782213185f)[Data Dictionary](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#f531a93b8e2d4bb1899ba6067c12c2d7)[Company Endpoints](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#53274edf0e9442d1a64091b213d689c2)[Enrichment: Company Data API](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#10ee4a7d95b1807bb965dad5a67086e3)[Company Discovery: Screening API](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#6258aca01eab458db4c5b94d66e20ccc)[Additional examples](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#a6b8fc580e7f42f8870fc777c8e56fa1)[Company Identification API](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#a6b1d0a6d79c420fad2d45c01893447b)[Company Dataset API](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#a6c3072d9dd2423bb5dda4a37e2666a6)[All dataset endpoints](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#a69f30268d8541c1a8217ded2c2cb39b)[Search: LinkedIn Company Search API (real-time)](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#116e4a7d95b180ca8d10c692c840ca30)[Building the Company/People Search Criteria Filter](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#116e4a7d95b180528ce4f6c485a76c40)[Making Requests](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#116e4a7d95b180cc900dc44049416103)[LinkedIn Posts by Company API (real-time)](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#4f91fbfc792a4e08a1e41400851f4da7)[LinkedIn Posts Keyword Search (real-time)](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#13ce4a7d95b1802fbd92f9e99c4c0530)[People Endpoints](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#eba67524e2b64652821db282c4fc51d1)[Enrichment: People Profile(s) API](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#53b549c4f66f46908f9fb31677d6b9d3)[Search: LinkedIn People Search API (real-time)](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#116e4a7d95b18081a753e062c8545f40)[Making Requests](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#116e4a7d95b18072b791c595c06f3c69)[LinkedIn Posts by Person API (real-time)](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#675b493db1144c00a31c89e91da7c082)[LinkedIn Posts Keyword Search (real-time)](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#13ce4a7d95b180579f19cc25235f053b)[API Usage Endpoints](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#b4e6a881ea0a4f0db865789fcaf5649e)[Get remaining credits](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=25#96e09fde1c16451590f5c6b796936b43)
## Introduction

The Crustdata API gives you programmatic access to firmographic and growth metrics data for companies across the world from more than 16 datasets (Linkedin headcount, Glassdoor, Instagram, G2, Web Traffic, Apple App Store reviews, Google Play Store, News among others).This documentation describes various available API calls and schema of the response. If you have any questions, please reach out to [abhilash@crustdata.com](mailto:abhilash@crustdata.com).
## Getting Started

#### Obtaining Authorization Token

 Reach out to [abhilash@crustdata.com](mailto:abhilash@crustdata.com) get an authorization token (API key) . 
## Data Dictionary

[![📔](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)Crustdata Data Dictionary](/Crustdata-Data-Dictionary-c265aa415fda41cb871090cbf7275922?pvs=25)
## Company Endpoints

### Enrichment: Company Data API

Overview: This endpoint enriches company data by retrieving detailed information about one or multiple companies using either their domain, name, or ID.Required: authentication token auth\_token for authorization.RequestParameterscompany\_domain: string (comma-separated list, up to 25 domains)Description: The domain(s) of the company(ies) you want to retrieve data for.Example: company\_domain=hubspot.com,google.comcompany\_name: string (comma-separated list, up to 25 names; use double quotes if names contain commas)Description: The name(s) of the company(ies) you want to retrieve data for.Example: company\_name="Acme, Inc.","Widget Co"company\_linkedin\_url: string (comma-separated list, up to 25 URLs)Description: The LinkedIn URL(s) of the company(ies).Example: company\_linkedin\_url=https://linkedin.com/company/hubspot,https://linkedin.com/company/clay-hqcompany\_id: integer (comma-separated list, up to 25 IDs)Description: The unique ID(s) of the company(ies) you want to retrieve data for.Example: company\_id=12345,67890fields: string (comma-separated list of fields)Description: Specifies the fields you want to include in the response. Supports nested fields up to a certain level.Example: fields=company\_name,company\_domain,glassdoor.glassdoor\_review\_countenrich\_realtime: boolean (False by default)Description: When True and the requested company is not present in Crustdata’s database, the company is enriched within 10 minutes of the request
#### Using the fields Parameter

The fields parameter allows you to customize the response by specifying exactly which fields you want to retrieve. This can help reduce payload size and improve performance.
#### Important Notes

Nested Fields: You can specify nested fields up to the levels defined in the response structure (see [Field Structure](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#10ee4a7d95b181029abaedc38f28666a) below). Fields nested beyond the allowed levels or within lists (arrays) cannot be individually accessed.Default Fields:Top-Level Non-Object Fields: If you do not specify the fields parameter, the response will include all top-level non-object fields by default (e.g., company\_name, company\_id).Object Fields: By default, the response will not include object fields like decision\_makers and founders.profiles, even if you have access to them. To include these fields, you must explicitly specify them using the fields parameter.User Permissions: Access to certain fields may be restricted based on your user permissions. If you request fields you do not have access to, the API will return an error indicating unauthorized access.
#### Examples

Request by Company Domain:Use Case: Ideal for users who have one or more company website domains and need to fetch detailed profiles.Note: You can provide up to 25 domains in a comma-separated list.Request:BashCopycurl 'https://api.crustdata.com/screener/company?company\_domain=hubspot.com,google.com' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token'
​Request by Company Name:Use Case: Suitable for users who have one or more company names and need to retrieve detailed profiles.Note: You can provide up to 25 names in a comma-separated list. If a company name contains a comma, enclose the name in double quotes.Request:BashCopycurl 'https://api.crustdata.com/screener/company?company\_name="HubSpot","Google, Inc."' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token'
​Request by Company LinkedIn URL:Use Case: Suitable for users who have one or more company Linkedin urls and need to retrieve detailed profiles.Note: You can provide up to 25 names in a comma-separated list. If a company name contains a comma, enclose the name in double quotes.Request:BashCopycurl 'https://api.crustdata.com/screener/company?company\_linkedin\_url=https://linkedin.com/company/hubspot,https://linkedin.com/company/clay-hq' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token'
​Request by Company ID:Use Case: Suitable for users who have ingested one or more companies from Crustdata already and want to enrich their data by Crustdata’s company\_id. Users generally use this when they want time-series data for specific companies after obtaining the company\_id from the [screening endpoint](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#6258aca01eab458db4c5b94d66e20ccc).Note: You can provide up to 25 IDs in a comma-separated list.Request:BashCopycurl 'https://api.crustdata.com/screener/company?company\_id=631480,789001' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token'
​Request with Specific FieldsUse Case: Fetch only specific fields to tailor the response to your needs.RequestBashCopycurl 'https://api.crustdata.com/screener/company?company\_domain=swiggy.com&fields=company\_name,headcount.linkedin\_headcount' \
--header 'Authorization: Token $token' \
--header 'Accept: application/json'
​More examples of Using fields parameter
#### Example 1: Request Specific Top-Level Fields

Request:ShellCopycurl 'https://api.crustdata.com/screener/company?company\_id=123&fields=company\_name,company\_website\_domain' \
--header 'Authorization: Token $token' \
--header 'Accept: application/json'
​Response Includes:company\_namecompany\_website\_domainrest of [top-level fields](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#10ee4a7d95b18158bde9c20e0e929316)
#### Example 2: Request Nested Fields

Request:ShellCopycurl 'https://api.crustdata.com/screener/company?company\_id=123&fields=glassdoor.glassdoor\_overall\_rating,glassdoor.glassdoor\_review\_count' \
--header 'Authorization: Token $token' \
--header 'Accept: application/json'
​Response Includes:glassdoorglassdoor\_overall\_ratingglassdoor\_review\_countrest of [top-level fields](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#10ee4a7d95b18158bde9c20e0e929316)
#### Example 3: Include 'decision\_makers' and 'founders.profiles'

Request:ShellCopycurl 'https://api.crustdata.com/screener/company?company\_id=123&fields=decision\_makers,founders.profiles' \
--header 'Authorization: Token $token' \
--header 'Accept: application/json'
​Response Includes:decision\_makers: Full array of decision-maker profiles.foundersprofiles: Full array of founder profiles.rest of [top-level fields](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#10ee4a7d95b18158bde9c20e0e929316)
#### Example 4: Requesting Unauthorized Fields

Assuming you do not have access to the headcount field.Request:ShellCopycurl 'https://api.crustdata.com/screener/company?company\_id=123&fields=company\_name,headcount' \
--header 'Authorization: Token $token' \
--header 'Accept: application/json'
​Error Response:ShellCopy{
"error": "Unauthorized access to field(s): headcount"
}
​Request with Realtime EnrichmentUse Case: For companies not tracked by Crustdata, you want to enrich them within 10 minutes of the requestShellCopycurl --location 'https://api.crustdata.com/screener/company?company\_linkedin\_url=https://www.linkedin.com/company/usebramble&enrich\_realtime=True' \
--header 'Accept: application/json, text/plain, /' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token'
​Response StructureThe response is a JSON array containing company objects. Below is the structure of the response up to the levels where you can filter using the fields parameter.
### Top-Level Fields

company\_id: integercompany\_name: stringlinkedin\_profile\_url: stringlinkedin\_id: stringlinkedin\_logo\_url: stringcompany\_twitter\_url: stringcompany\_website\_domain: stringhq\_country: stringheadquarters: stringlargest\_headcount\_country: stringhq\_street\_address: stringcompany\_website: stringyear\_founded: string (ISO 8601 date)fiscal\_year\_end: stringestimated\_revenue\_lower\_bound\_usd: integerestimated\_revenue\_higher\_bound\_usd: integeremployee\_count\_range: stringcompany\_type: stringlinkedin\_company\_description: stringacquisition\_status: string or nullceo\_location: string
### Nested Objects

You can filter up to the following nested levels:
#### all\_office\_addresses

array of strings
#### markets

array of strings
#### stock\_symbols

array of strings
#### taxonomy

linkedin\_specialities: array of stringslinkedin\_industries: array of stringscrunchbase\_categories: array of strings
#### competitors

competitor\_website\_domains: array of strings or nullpaid\_seo\_competitors\_website\_domains: array of stringsorganic\_seo\_competitors\_website\_domains: array of strings
#### headcount

linkedin\_headcount: integerlinkedin\_headcount\_total\_growth\_percentmom: floatqoq: floatsix\_months: floatyoy: floattwo\_years: floatlinkedin\_headcount\_total\_growth\_absolutemom: floatqoq: floatsix\_months: floatyoy: floattwo\_years: floatlinkedin\_headcount\_by\_role\_absolute: objectlinkedin\_headcount\_by\_role\_percent: objectlinkedin\_role\_metricsall\_roles: string0\_to\_10\_percent: string11\_to\_30\_percent: string31\_to\_50\_percent: string or null51\_to\_70\_percent: string or null71\_to\_100\_percent: string or nulllinkedin\_headcount\_by\_role\_six\_months\_growth\_percent: objectlinkedin\_headcount\_by\_role\_yoy\_growth\_percent: objectlinkedin\_headcount\_by\_region\_absolute: objectlinkedin\_headcount\_by\_region\_percent: objectlinkedin\_region\_metricsall\_regions: string0\_to\_10\_percent: string11\_to\_30\_percent: string31\_to\_50\_percent: string or null51\_to\_70\_percent: string or null71\_to\_100\_percent: string or nulllinkedin\_headcount\_by\_skill\_absolute: objectlinkedin\_headcount\_by\_skill\_percent: objectlinkedin\_skill\_metricsall\_skills: string0\_to\_10\_percent: string or null11\_to\_30\_percent: string31\_to\_50\_percent: string or null51\_to\_70\_percent: string or null71\_to\_100\_percent: string or nulllinkedin\_headcount\_timeseries: array of objects (Cannot filter within this array)linkedin\_headcount\_by\_function\_timeseries: object (Cannot filter within this object)
#### web\_traffic

monthly\_visitors: integermonthly\_visitor\_mom\_pct: floatmonthly\_visitor\_qoq\_pct: floattraffic\_source\_social\_pct: floattraffic\_source\_search\_pct: floattraffic\_source\_direct\_pct: floattraffic\_source\_paid\_referral\_pct: floattraffic\_source\_referral\_pct: floatmonthly\_visitors\_timeseries: array of objects (Cannot filter within this array)traffic\_source\_social\_pct\_timeseries: array of objects (Cannot filter within this array)traffic\_source\_search\_pct\_timeseries: array of objects (Cannot filter within this array)traffic\_source\_direct\_pct\_timeseries: array of objects (Cannot filter within this array)traffic\_source\_paid\_referral\_pct\_timeseries: array of objects (Cannot filter within this array)traffic\_source\_referral\_pct\_timeseries: array of objects (Cannot filter within this array)
#### glassdoor

glassdoor\_overall\_rating: floatglassdoor\_ceo\_approval\_pct: integerglassdoor\_business\_outlook\_pct: integerglassdoor\_review\_count: integerglassdoor\_senior\_management\_rating: floatglassdoor\_compensation\_rating: floatglassdoor\_career\_opportunities\_rating: floatglassdoor\_culture\_rating: float or nullglassdoor\_diversity\_rating: float or nullglassdoor\_work\_life\_balance\_rating: float or nullglassdoor\_recommend\_to\_friend\_pct: integer or nullglassdoor\_ceo\_approval\_growth\_percentmom: floatqoq: floatyoy: floatglassdoor\_review\_count\_growth\_percentmom: floatqoq: floatyoy: float
#### g2

g2\_review\_count: integerg2\_average\_rating: floatg2\_review\_count\_mom\_pct: floatg2\_review\_count\_qoq\_pct: floatg2\_review\_count\_yoy\_pct: float
#### linkedin\_followers

linkedin\_followers: integerlinkedin\_follower\_count\_timeseries: array of objects (Cannot filter within this array)linkedin\_followers\_mom\_percent: floatlinkedin\_followers\_qoq\_percent: floatlinkedin\_followers\_six\_months\_growth\_percent: floatlinkedin\_followers\_yoy\_percent: float
#### funding\_and\_investment

crunchbase\_total\_investment\_usd: integerdays\_since\_last\_fundraise: integerlast\_funding\_round\_type: stringcrunchbase\_investors: array of stringslast\_funding\_round\_investment\_usd: integerfunding\_milestones\_timeseries: array of objects (Cannot filter within this array)
#### job\_openings

recent\_job\_openings\_title: string or nulljob\_openings\_count: integer or nulljob\_openings\_count\_growth\_percentmom: float or nullqoq: float or nullyoy: float or nulljob\_openings\_by\_function\_qoq\_pct: objectjob\_openings\_by\_function\_six\_months\_growth\_pct: objectopen\_jobs\_timeseries: array of objects (Cannot filter within this array)recent\_job\_openings: array of objects (Cannot filter within this array)
#### seo

average\_seo\_organic\_rank: integermonthly\_paid\_clicks: integermonthly\_organic\_clicks: integeraverage\_ad\_rank: integertotal\_organic\_results: integer or floatmonthly\_google\_ads\_budget: integer or floatmonthly\_organic\_value: integertotal\_ads\_purchased: integerlost\_ranked\_seo\_keywords: integergained\_ranked\_seo\_keywords: integernewly\_ranked\_seo\_keywords: integer
#### founders

founders\_locations: array of stringsfounders\_education\_institute: array of stringsfounders\_degree\_name: array of stringsfounders\_previous\_companies: array of stringsfounders\_previous\_titles: array of stringsprofiles: array of objects (Cannot filter within this array)
#### decision\_makers

decision\_makers: array of objects (Cannot filter within this array)
#### news\_articles

news\_articles: array of objects (Cannot filter within this array)Response
#### Examples

The response provides a comprehensive profile of the company, including firmographic details, social media links, headcount data, and growth metrics. For a detailed response data structure, refer to this JSON [![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/QN8Qj7dg8MbW)​Key Points
#### Credits

Database Enrichment:1 credits per company.Real-Time Enrichment (enrich\_realtime=True):4+1 credits per company.
#### Enrichment Status

When you request data for a company not in our database, we start an enrichment process that takes up to 24 hours (or 10 minutes if enrich\_realtime is true).The API response includes a status field:enriching : The company is being processed, poll later to get the full company infonot\_found : Enrichment failed (e.g., no website or employees). You can stop polling for this company.JavaScriptCopy[
{
"status": "enriching",
"message": "The following companies will be enriched in the next 24 hours",
"companies": [
{
"identifier": "https://www.linkedin.com/company/123456",
"type": "linkedin\_url"
}
]
}
]
​
#### Limitations on Nested Fields

Maximum Nesting Level: You can specify nested fields only up to the levels defined aboveDefault Exclusion of Certain Fields: Even if you have access to fields like decision\_makers and founders.profiles, they will not be included in the response by default when the fields parameter is not provided. You must explicitly request these fields using the fields parameter.Example:BashCopy# Will not include 'decision\_makers' or 'founders.profiles' by default
curl 'https://api.crustdata.com/screener/company?company\_id=123' \
--header 'Authorization: Token $token' \
--header 'Accept: application/json'
​To include them, specify in fields:BashCopycurl 'https://api.crustdata.com/screener/company?company\_id=123&fields=decision\_makers,founders.profiles' \
--header 'Authorization: Token $token' \
--header 'Accept: application/json'
​Unavailable Fields: If you request a field that is not available or beyond the allowed nesting level, the API will return an error indicating that the field is not available for filtering.
### Company Discovery: Screening API

Overview: The company screening API request allows you to screen and filter companies based on various growth and firmographic criteria. Required: authentication token auth\_token for authorization.RequestIn the example below, we get companies that meet the following criteria:Have raised > $5,000,000 in total funding ANDHave headcount > 50 ANDHave largest headcount country as USAcURLBashCopycurl 'https://api.crustdata.com/screener/screen/' \
-H 'Accept: application/json, text/plain, /' \
-H 'Accept-Language: en-US,en;q=0.9' \
-H 'Authorization: Token $auth\_token' \
-H 'Connection: keep-alive' \
-H 'Content-Type: application/json' \
-H 'Origin: https://crustdata.com' \
--data-raw '{
"metrics": [
{
"metric\_name": "linkedin\_headcount\_and\_glassdoor\_ceo\_approval\_and\_g2"
}
],
"filters": {
"op": "and",
"conditions": [
{
"column": "crunchbase\_total\_investment\_usd",
"type": "=>",
"value": 5000000,
"allow\_null": false
},
{
"column": "linkedin\_headcount",
"type": "=>",
"value": 50,
"allow\_null": false
},
{
"column": "largest\_headcount\_country",
"type": "(.)",
"value": "USA",
"allow\_null": false
}
]
},
"hidden\_columns": [],
"offset": 0,
"count": 100,
"sorts": []
}' \
--compressed
​PythonPythonCopyimport requests
headers = {
'Accept': 'application/json, text/plain, /',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Token $auth\_token', # replace $auth\_token
'Connection': 'keep-alive',
'Content-Type': 'application/json',
'Origin': 'https://crustdata.com'
}
json\_data = {
'metrics': [
{
'metric\_name': 'linkedin\_headcount\_and\_glassdoor\_ceo\_approval\_and\_g2',
},
],
'filters': {
'op': 'and',
'conditions': [
{
'column': 'crunchbase\_total\_investment\_usd',
'type': '=>',
'value': 5000000,
'allow\_null': False,
},
{
'column': 'linkedin\_headcount',
'type': '=>',
'value': 50,
'allow\_null': False,
},
{
'column': 'largest\_headcount\_country',
'type': '(.)',
'value': 'USA',
'allow\_null': False,
},
],
},
'hidden\_columns': [],
'offset': 0,
'count': 100,
'sorts': []
}
response = requests.post('https://api.crustdata.com/screener/screen/', headers=headers, json=json\_data)
​Request Body Overview The request body is a JSON object that contains the following parameters:

| Parameter | Description | Required |
| --- | --- | --- |
| metrics | An array of metric objects containing the metric name. Value should always be [{"metric\_name": "linkedin\_headcount\_and\_glassdoor\_ceo\_approval\_and\_g2"}] | Yes |
| filters | An object containing the filter conditions. | Yes |
| offset | The starting point of the result set. Default value is 0. | Yes |
| count | The number of results to return in a single request. Maximum value is 100. Default value is 100. | Yes |
| sorts | An array of sorting criteria. | No |

#### Parameters:

metricsDictates the columns in the response. The only possible value isBashCopy[{"metric\_name": "linkedin\_headcount\_and\_glassdoor\_ceo\_approval\_and\_g2"}]
​filtersExample: JSONCopy{
"op": "and",
"conditions": [
{
"op": "or",
"conditions": [
{"hq\_country", "type": "(.)", "value": "USA"},
{"hq\_country", "type": "(.)", "value": "IND"}
],
}
{"column": "crunchbase\_total\_investment\_usd", "type": "=>", "value": "5000000"},
{"column": "largest\_headcount\_country", "type": "(.)", "value": "USA"}
]
}
​The filters object contains the following parameters:

| Parameter | Description | Required |
| --- | --- | --- |
| op | The operator to apply on the conditions. The value can be "and" or "or". | Yes |
| conditions | An array of complex filter objects or basic filter objects (see below) | Yes |

conditions parameterThis has two possible types of valuesBasic Filter ObjectExample: {"column": "linkedin\_headcount", "type": "=>", "value": "50" } The object contains the following parameters:

| Parameter | Description | Required |
| --- | --- | --- |
| column | The name of the column to filter. | Yes |
| type | The filter type. The value can be "=>", "=<", "=", "!=", “in”, “(.)”, “[.]” | Yes |
| value | The filter value. | Yes |
| allow\_null | Whether to allow null values. The value can be "true" or "false". Default value is "false". | No |

List of all column values[![📔](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)Crustdata Data Dictionary](https://crustdata.notion.site/Crustdata-Data-Dictionary-c265aa415fda41cb871090cbf7275922?pvs=24) List of all type values

| condition type | condition description | applicable column types | example |
| --- | --- | --- | --- |
| "=>" | Greater than or equal | number | { "column": "linkedin\_headcount", "type": "=>", "value": "50"} |
| "=<" | Lesser than or equal | number | { "column": "linkedin\_headcount", "type": "=<", "value": "50"} |
| "=", | Equal | number | { "column": "linkedin\_headcount", "type": "=", "value": "50"} |
| “<” | Lesser than | number | { "column": "linkedin\_headcount", "type": "<", "value": "50"} |
| “>” | Greater than | number | { "column": "linkedin\_headcount", "type": ">", "value": "50"} |
| “(.)” | Contains, case insensitive | string | { "column": "crunchbase\_categories", "type": "(.)", "value": "artificial intelligence"} |
| “[.]” | Contains, case sensitive | string | { "column": "crunchbase\_categories", "type": "[.]", "value": "Artificial Intelligence"} |
| "!=" | Not equals | number |  |
| “in” | Exactly matches atleast one of the elements of list | string, number | { "column": "company\_id", "type": "in", "value": [123, 346. 564]} |

Complex Filter ObjectExample: JSONCopy{
"op": "or",
"conditions": [
{"hq\_country", "type": "(.)", "value": "USA"},
{"hq\_country", "type": "(.)", "value": "IND"}
]
}
​Same schema as the parent [filters](https://crustdata.notion.site/filters-c66d5236e8ea40df8af114f6d447ab48?pvs=24#8a72acfe02a5455e895ea9a9dede08c4) parameter ResponseExample: [![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/ntHvSKVeZJIc)​The response is JSON object that consists of two main components: fields and rows.fields: An array of objects representing the columns in the dataset.rows: An array of arrays, each representing a row of data.The values in each of the rows elements are ordered in the same sequence as the fields in the fields array. For example, the ith value in a row corresponds to the ith field in the fields array.Parsing the responseGiven the following response objectJSONCopy{
"fields": [
{"type": "string", "api\_name": "company\_name", "hidden": false},
{"type": "number", "api\_name": "valuation\_usd", "hidden": false},
{"type": "number", "api\_name": "crunchbase\_total\_investment\_usd", "hidden": false},
{"type": "string", "api\_name": "markets", "hidden": false},
{"type": "number", "api\_name": "days\_since\_last\_fundraise", "hidden": false},
{"type": "number", "api\_name": "linkedin\_headcount", "hidden": false},
{"type": "number", "api\_name": "linkedin\_headcount\_mom\_percent", "hidden": false}
],
"rows": [
["Sketch", null, 20000000, "PRIVATE", 1619, 258, -11.64]
]
}
​The first element in rows (i.e. "Sketch") corresponds to fields[0]["api\_name"] (i.e. "company\_name"). The second element in rows (i.e. null) corresponds to fields[1]["api\_name"] (i.e. "valuation\_usd"), and so on.
#### Pseudo code for mapping fields → rows[i]

Here's a pseudo code to help understand this mapping:Plain TextCopyfor each row in rows:
for i in range(length(row)):
field\_name = fields[i]["api\_name"]
field\_value = row[i]
# Map field\_name to field\_value​In simple terms:For each row, iterate over each value.Map the ith value of the row to the ith api\_name in the fields.Here is the complete list of fields in the response for each companyComplete list of columns company\_namecompany\_websitecompany\_website\_domainlinkedin\_profile\_urlmonthly\_visitorsvaluation\_usdcrunchbase\_total\_investment\_usdmarketsdays\_since\_last\_fundraiselinkedin\_headcountlinkedin\_headcount\_mom\_percentlinkedin\_headcount\_qoq\_percentlinkedin\_headcount\_yoy\_percentlinkedin\_headcount\_mom\_absolutelinkedin\_headcount\_qoq\_absolutelinkedin\_headcount\_yoy\_absoluteglassdoor\_overall\_ratingglassdoor\_ceo\_approval\_pctglassdoor\_business\_outlook\_pctglassdoor\_review\_countg2\_review\_countg2\_average\_ratingcompany\_idhq\_countryheadquarterslargest\_headcount\_countrylast\_funding\_round\_typevaluation\_datelinkedin\_categorieslinkedin\_industriescrunchbase\_investorscrunchbase\_categoriesacquisition\_statuscompany\_year\_foundedtechnology\_domainsfounder\_names\_and\_profile\_urlsfounders\_locationceo\_locationfounders\_education\_institutefounders\_degree\_namefounders\_previous\_companyfounders\_previous\_titlemonthly\_visitor\_mom\_pctmonthly\_visitor\_qoq\_pcttraffic\_source\_social\_pcttraffic\_source\_search\_pcttraffic\_source\_direct\_pcttraffic\_source\_paid\_referral\_pcttraffic\_source\_referral\_pctmeta\_total\_adsmeta\_active\_adsmeta\_ad\_platformsmeta\_ad\_urlmeta\_ad\_idaverage\_organic\_rankmonthly\_paid\_clicksmonthly\_organic\_clicksaverage\_ad\_ranktotal\_organic\_resultsmonthly\_google\_ads\_budgetmonthly\_organic\_valuetotal\_ads\_purchasedlost\_ranksgained\_ranksnewly\_rankedpaid\_competitorsorganic\_competitorslinkedin\_followerslinkedin\_headcount\_engineeringlinkedin\_headcount\_saleslinkedin\_headcount\_operationslinkedin\_headcount\_human\_resourcelinkedin\_headcount\_indialinkedin\_headcount\_usalinkedin\_headcount\_engineering\_percentlinkedin\_headcount\_sales\_percentlinkedin\_headcount\_operations\_percentlinkedin\_headcount\_human\_resource\_percentlinkedin\_headcount\_india\_percentlinkedin\_headcount\_usa\_percentlinkedin\_followers\_mom\_percentlinkedin\_followers\_qoq\_percentlinkedin\_followers\_yoy\_percentlinkedin\_all\_employee\_skill\_nameslinkedin\_all\_employee\_skill\_countlinkedin\_employee\_skills\_0\_to\_10\_pctlinkedin\_employee\_skills\_11\_to\_30\_pctlinkedin\_employee\_skills\_31\_to\_50\_pctlinkedin\_employee\_skills\_51\_to\_70\_pctlinkedin\_employee\_skills\_71\_to\_100\_pctglassdoor\_culture\_ratingglassdoor\_diversity\_ratingglassdoor\_work\_life\_balance\_ratingglassdoor\_senior\_management\_ratingglassdoor\_compensation\_ratingglassdoor\_career\_opportunities\_ratingglassdoor\_recommend\_to\_friend\_pctglassdoor\_ceo\_approval\_mom\_pctglassdoor\_ceo\_approval\_qoq\_pctglassdoor\_ceo\_approval\_mom\_pct.1glassdoor\_review\_count\_mom\_pctglassdoor\_review\_count\_qoq\_pctglassdoor\_review\_count\_yoy\_pctg2\_review\_count\_mom\_pctg2\_review\_count\_qoq\_pctg2\_review\_count\_yoy\_pctinstagram\_followers (deprecated)instagram\_posts (deprecated)instagram\_followers\_mom\_pct (deprecated)instagram\_followers\_qoq\_pct (deprecated)instagram\_followers\_yoy\_pct (deprecated)recent\_job\_openings\_titlerecent\_job\_openings\_title\_countjob\_openings\_countjob\_openings\_count\_mom\_pctjob\_openings\_count\_qoq\_pctjob\_openings\_count\_yoy\_pctjob\_openings\_accounting\_qoq\_pctjob\_openings\_accounting\_six\_months\_growth\_pctjob\_openings\_art\_and\_design\_qoq\_pctjob\_openings\_art\_and\_design\_six\_months\_growth\_pctjob\_openings\_business\_development\_qoq\_pctjob\_openings\_business\_development\_six\_months\_growth\_pctjob\_openings\_engineering\_qoq\_pctjob\_openings\_engineering\_six\_months\_growth\_pctjob\_openings\_finance\_qoq\_pctjob\_openings\_finance\_six\_months\_growth\_pctjob\_openings\_human\_resource\_qoq\_pctjob\_openings\_human\_resource\_six\_months\_growth\_pctjob\_openings\_information\_technology\_qoq\_pctjob\_openings\_information\_technology\_six\_months\_growth\_pctjob\_openings\_marketing\_qoq\_pctjob\_openings\_marketing\_six\_months\_growth\_pctjob\_openings\_media\_and\_communication\_qoq\_pctjob\_openings\_media\_and\_communication\_six\_months\_growth\_pctjob\_openings\_operations\_qoq\_pctjob\_openings\_operations\_six\_months\_growth\_pctjob\_openings\_research\_qoq
#### Additional examples

[![🔍](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)Crustdata Company Screening API Detailed Examples](/Crustdata-Company-Screening-API-Detailed-Examples-375908d855464d87a01efd2c7a369750?pvs=25)
### Company Identification API

Given a company’s name, website or LinkedIn profile, you can identify the company in Crustdata’s database with company identification APIThe input to this API is any combination of the following fields name of the company website of the company LinkedIn profile url of the companyRequestBashCopy curl 'https://api.crustdata.com/screener/identify/' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $api\_token' \
--header 'Connection: keep-alive' \
--header 'Content-Type: application/json' \
--header 'Origin: https://crustdata.com' \
--data '{"query\_company\_website": "serverobotics.com", "count": 1}'
​Payload fields (at least one of the query fields required):query\_company\_name : name of the companyquery\_company\_website : website of the companyquery\_company\_linkedin\_url : LinkedIn profile url of the companycount : maximum number of results. Default is 10.ResultExample:BashCopy[
{
"company\_id": 628895,
"company\_name": "Serve Robotics",
"company\_website\_domain": "serverobotics.com",
"company\_website": "http://www.serverobotics.com",
"linkedin\_profile\_url": "https://www.linkedin.com/company/serverobotics",
"linkedin\_headcount": 82,
"acquisition\_status": null,
"score": 0.3
}
]
​Each item in the result corresponds to a company record in Crustdata’s database. The records are ranked by the matching score, highest first. The score is maximum when all the query fields are provided and their values exactly matches the value of the corresponding company in Crustdata’s database.Each result record contains the following fields for the companycompany\_id : A unique identifier for the company in Crustdata’s database.company\_name : Name of the company in Crustdata’s databasecompany\_website\_domain : Website domain of the company as mentioned on its Linkedin pagecompany\_website : Website of the companylinkedin\_profile\_url : LinkedIn profile url for the companylinkedin\_headcount : Latest headcount of the company in Crustdata’s databaseacquisition\_status : Either acquired or nullscore : a relative score based on the query parameters provided and how well they match the company fields in Crustdata’s database
### Company Dataset API

Overview: The Company Dataset API allows users to retrieve specific datasets related to companies, such as job listings, decision makers, news articles, G2 etc.Request Example (Job Listings)To retrieve data for job listings, make a POST request to the following endpoint:
### Request URL

Plain TextCopyhttps://api.crustdata.com/data\_lab/job\_listings/Table/​
### Request Headers

| Header Name | Description | Example Value |
| --- | --- | --- |
| Accept | Specifies the types of media that the client can process. | application/json, text/plain, \*/\* |
| Accept-Language | Specifies the preferred language for the response. | en-US,en;q=0.9 |
| Authorization | Contains the authentication credentials for HTTP authentication. | Token $token |
| Content-Type | Indicates the media type of the resource or data. | application/json |
| User-Agent | Contains information about the user agent (browser) making the request. | Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 ... |

### Request Body

| Parameter | Type | Description | Example Value |
| --- | --- | --- | --- |
| tickers | Array | Can contain specific tickers for filtering. | [] |
| dataset | Object | Contains details about the dataset being requested. | {"name":"job\_listings","id":"joblisting"} |
| filters | Object | Contains conditions for filtering the data. | See detailed breakdown below. |
| groups | Array | For grouping the data. | [] |
| aggregations | Array | For data aggregations. | [] |
| functions | Array | For applying functions on the data. | [] |
| offset | Number | The starting point for data retrieval. | 0 |
| count | Number | The number of records to retrieve. | 100 |
| sorts | Array | For sorting the data. | [] |

Filters Object Breakdown

| Parameter | Type | Description | Example Value |
| --- | --- | --- | --- |
| op | String | The operation for the condition. It can be logical operations like and, or, etc. | and |
| conditions | Array | An array of conditions. Each condition can have sub-conditions. | See detailed breakdown below. |

Sub-Condition Breakdown

| Parameter | Type | Description | Example Value |
| --- | --- | --- | --- |
| column | String | The column to be filtered. | company\_id |
| type | String | The type of operation for filtering. Common operations include =, >, <, =>, etc. | = |
| value | Various | The value for filtering. The datatype can vary based on the column being filtered. | 7576 |

### Response Body

| Parameter | Type | Description |
| --- | --- | --- |
| fields | Array | An array of objects detailing the attributes of the job listings. |
| rows | Array | Contains the job listings data. Each entry corresponds to the attributes in the "fields" section. |

Fields Object Breakdown

| Parameter | Type | Description |
| --- | --- | --- |
| type | String | The data type of the field. |
| api\_name | String | The name used in the API for this field. |
| hidden | Boolean | Indicates if the field is hidden. |
| options | Array | Related options for the field. |
| summary | String | A brief summary of the field. |
| local\_metric | Boolean | Indicates if the field is a local metric. |
| display\_name | String | The display name of the field. |
| geocode | Boolean | Indicates if the field contains geocode data. |

#### All dataset endpoints

[![](/icons/database_yellow.svg?mode=dark)Crustdata Dataset API Detailed Examples](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25)
### Search: LinkedIn Company Search API (real-time)

Overview: Search for company profiles using either directly a LinkedIn Sales Navigator accounts search URL or a custom search criteria as a filter. This endpoint allows you to retrieve detailed information about companies matching specific criteria.Each request returns up-to 25 results. To paginate, update the page number of the Sales Navigator search URL and do the request again.In the request payload, either set the url of the Sales Navigator Accounts search from your browser in the parameter linkedin\_sales\_navigator\_search\_url or specify the search criteria as a JSON object in the parameter filtersRequired: authentication token auth\_token for authorization.
#### Building the Company/People Search Criteria Filter

Based on the field on you are filtering, filters can be categorized into 3 different categoriesText FilterA text filter is used to filter based on specific text values. Each text filter must contain filter\_type, type and list of value.Example:Plain TextCopy{
"filter\_type": "COMPANY\_HEADCOUNT",
"type": "in",
"value": ["10,001+", "1,001-5,000"]
}​Valid type:in: To include values.not in: To exclude values. Excluding values might not be supported for every filter.Range FilterA range filter is used to filter based on a range of values. Each filter must contain filter\_type, type and value. Few range filters might contain a sub\_filter. Ensure that you correctly pass sub\_filter if required.sub\_filterThe sub\_filter is an optional field that provides additional context for the range filter. For example, with the DEPARTMENT\_HEADCOUNT filter, the sub\_filter specifies which department the filter applies to. Ensure that you correctly pass sub\_filter if required.Example:Plain TextCopy{
"filter\_type": "ANNUAL\_REVENUE",
"type": "between",
"value": {"min": 1, "max": 500},
"sub\_filter": "USD"
}​Valid type:between: To specify a range of values, indicating that the value must fall within the defined minimum and maximum limits.Boolean FilterA boolean filter is used to filter based on true/false values. It doesn't contain any type or valueExample:Plain TextCopy{
"filter\_type": "IN\_THE\_NEWS"
}​And here is the full dictionary for filter attributes and possible values you can pass:Filter Dictionary for Company Search

| Filter Type | Description | Properties | Value/Sub-filter |
| --- | --- | --- | --- |
| COMPANY\_HEADCOUNT | Specifies the size of the company based on the number of employees. | types: [in] | "1-10", "11-50", "51-200", "201-500", "501-1,000", "1,001-5,000", "5,001-10,000", "10,001+" |
| REGION | Specifies the geographical region of the company. | types: [in, not in] | [region\_values](https://crustdata-docs-region-json.s3.us-east-2.amazonaws.com/updated_regions.json) |
| INDUSTRY | Specifies the industry of the company. | types: [in, not in] | [industry\_values](https://crustdata-docs-region-json.s3.us-east-2.amazonaws.com/industry_values.json) |
| NUM\_OF\_FOLLOWERS | Specifies the number of followers a company has. | types: [in] | "1-50", "51-100", "101-1000", "1001-5000", "5001+" |
| FORTUNE | Specifies the Fortune ranking of the company. | types: [in] | "Fortune 50", "Fortune 51-100", "Fortune 101-250", "Fortune 251-500" |
| ACCOUNT\_ACTIVITIES | Specifies recent account activities, such as leadership changes or funding events. | types: [in] | "Senior leadership changes in last 3 months", "Funding events in past 12 months" |
| JOB\_OPPORTUNITIES | Specifies job opportunities available at the company. | types: [in] | "Hiring on Linkedin” |
| COMPANY\_HEADCOUNT\_GROWTH | Specifies the growth of the company's headcount. | allowed\_without\_sub\_filter, types: [between] | N/A |
| ANNUAL\_REVENUE | Specifies the annual revenue of the company. | types: [between] | "USD", "AED", "AUD", "BRL", "CAD", "CNY", "DKK", "EUR", "GBP", "HKD", "IDR", "ILS", "INR", "JPY", "NOK", "NZD", "RUB", "SEK", "SGD", "THB", "TRY", "TWD" |
| DEPARTMENT\_HEADCOUNT | Specifies the headcount of specific departments within the company. | types: [between] | "Accounting", "Administrative", "Arts and Design", "Business Development", "Community and Social Services", "Consulting", "Education", "Engineering", "Entrepreneurship", "Finance", "Healthcare Services", "Human Resources", "Information Technology", "Legal", "Marketing", "Media and Communication", "Military and Protective Services", "Operations", "Product Management", "Program and Project Management", "Purchasing", "Quality Assurance", "Real Estate", "Research", "Sales", "Customer Success and Support" |
| DEPARTMENT\_HEADCOUNT\_GROWTH | Specifies the growth of headcount in specific departments. | types: [between] | "Accounting", "Administrative", "Arts and Design", "Business Development", "Community and Social Services", "Consulting", "Education", "Engineering", "Entrepreneurship", "Finance", "Healthcare Services", "Human Resources", "Information Technology", "Legal", "Marketing", "Media and Communication", "Military and Protective Services", "Operations", "Product Management", "Program and Project Management", "Purchasing", "Quality Assurance", "Real Estate", "Research", "Sales", "Customer Success and Support" |
| KEYWORD | Filters based on specific keywords related to the company. | types: [in] | List of strings (max length 1) Supports boolean filters. Example: "'sales' or 'marketing' or 'gtm'" will match either of these 3 words across the full LinkedIn profile of the company |

Filter Dictionary for Person Search

| Filter Type | Description | Properties | Value/Sub-filter |
| --- | --- | --- | --- |
| CURRENT\_COMPANY | Specifies the current company of the person. | types: [in, not in] | List of strings. You can specify names, domains or LinkedIn url of the companies. Example: ”Serve Robotics”, “serverobotics.com”, “https://www.linkedin.com/company/serverobotics” |
| CURRENT\_TITLE | Specifies the current title of the person. | types: [in, not in] | List of strings. Case in-sensitive contains matching for each of the strings. Example: ["ceo", "founder", "director"] will match all the profiles with any current job title(s) having any of the 3 strings (”ceo” or “founder” or “director”) |
| PAST\_TITLE | Specifies the past titles held by the person. | types: [in, not in] | List of strings. Case in-sensitive contains matching for each of the strings. Example: ["ceo", "founder", "director"] will match all the profiles with any past job title(s) having any of the 3 strings (”ceo” or “founder” or “director”) |
| COMPANY\_HEADQUARTERS | Specifies the headquarters of the person's company. | types: [in, not in] | [region\_values](https://jsonhero.io/j/mjVQGjJEJr8i) |
| COMPANY\_HEADCOUNT | Specifies the size of the company based on the number of employees. | types: [in] | "Self-employed", "1-10", "11-50", "51-200", "201-500", "501-1,000", "1,001-5,000", "5,001-10,000", "10,001+" |
| REGION | Specifies the geographical region of the person. | types: [in, not in] | [region\_values](https://crustdata-docs-region-json.s3.us-east-2.amazonaws.com/updated_regions.json) |
| INDUSTRY | Specifies the industry of the person's company. | types: [in, not in] | [industry\_values](https://crustdata-docs-region-json.s3.us-east-2.amazonaws.com/industry_values.json) |
| PROFILE\_LANGUAGE | Specifies the language of the person's profile. | types: [in] | "Arabic", "English", "Spanish", "Portuguese", "Chinese", "French", "Italian", "Russian", "German", "Dutch", "Turkish", "Tagalog", "Polish", "Korean", "Japanese", "Malay", "Norwegian", "Danish", "Romanian", "Swedish", "Bahasa Indonesia", "Czech" |
| SENIORITY\_LEVEL | Specifies the seniority level of the person. | types: [in, not in] | "Owner / Partner", "CXO", "Vice President", "Director", "Experienced Manager", "Entry Level Manager", "Strategic", "Senior", "Entry Level", "In Training" |
| YEARS\_AT\_CURRENT\_COMPANY | Specifies the number of years the person has been at their current company. | types: [in] | "Less than 1 year", "1 to 2 years", "3 to 5 years", "6 to 10 years", "More than 10 years" |
| YEARS\_IN\_CURRENT\_POSITION | Specifies the number of years the person has been in their current position. | types: [in] | "Less than 1 year", "1 to 2 years", "3 to 5 years", "6 to 10 years", "More than 10 years" |
| YEARS\_OF\_EXPERIENCE | Specifies the total years of experience the person has. | types: [in] | "Less than 1 year", "1 to 2 years", "3 to 5 years", "6 to 10 years", "More than 10 years" |
| FIRST\_NAME | Specifies the first name of the person. | types: [in] | List of strings (max length 1) |
| LAST\_NAME | Specifies the last name of the person. | types: [in] | List of strings (max length 1) |
| FUNCTION | Specifies the function or role of the person. | types: [in, not in] | "Accounting", "Administrative", "Arts and Design", "Business Development", "Community and Social Services", "Consulting", "Education", "Engineering", "Entrepreneurship", "Finance", "Healthcare Services", "Human Resources", "Information Technology", "Legal", "Marketing", "Media and Communication", "Military and Protective Services", "Operations", "Product Management", "Program and Project Management", "Purchasing", "Quality Assurance", "Real Estate", "Research", "Sales", "Customer Success and Support" |
| PAST\_COMPANY | Specifies the past companies the person has worked for. | types: [in, not in] | List of strings You can specify names, domains or LinkedIn url of the companies. Example: ”Serve Robotics”, “serverobotics.com”, “https://www.linkedin.com/company/serverobotics” |
| COMPANY\_TYPE | Specifies the type of company the person works for. | types: [in] | "Public Company", "Privately Held", "Non Profit", "Educational Institution", "Partnership", "Self Employed", "Self Owned", "Government Agency" |
| POSTED\_ON\_LINKEDIN | Specifies if the person has posted on LinkedIn. | N/A | N/A |
| RECENTLY\_CHANGED\_JOBS | Specifies if the person has recently changed jobs. | N/A | N/A |
| IN\_THE\_NEWS | Specifies if the person has been mentioned in the news. | N/A | N/A |
| KEYWORD | Filters based on specific keywords related to the company. | types: [in] | List of strings (max length 1) Supports boolean filters. Example: "'sales' or 'gtm' or 'marketer'" will match either of these 3 words across the full LinkedIn profile of the person |

#### Making Requests

Request:
#### Request Body:

The request body can have the following keys (atleast one of them is required)linkedin\_sales\_navigator\_search\_url (optional): URL of the Sales Navigator Accounts search from the browserfilters (optional): JSON dictionary defining the search criteria as laid out by the [Crustdata filter schema](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#116e4a7d95b180528ce4f6c485a76c40).page (optiona): Only valid when filters is not empty. When passing linkedin\_sales\_navigator\_search\_url, page should be specified in linkedin\_sales\_navigator\_search\_url itself
#### Examples

Via LinkedIn Sales Navigator URL:BashCopycurl --location 'https://api.crustdata.com/screener/company/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--data '{
"linkedin\_sales\_navigator\_search\_url": "https://www.linkedin.com/sales/search/company?query=(filters%3AList((type%3ACOMPANY\_HEADCOUNT%2Cvalues%3AList((id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A103323778%2Ctext%3AMexico%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A25%2Ctext%3AManufacturing%2CselectionType%3AINCLUDED)))))&sessionId=8TR8HMz%2BTVOYaeivK9p%2Bpg%3D%3D&viewAllFilters=true"
}'
​Via Custom Search Filters:Refer [Building the Company/People Search Criteria Filter](https://crustdata.notion.site/Building-the-Company-People-Search-Criteria-Filter-c66d5236e8ea40df8af114f6d447ab48?pvs=24#116e4a7d95b180528ce4f6c485a76c40) to build the custom search filter for your query and pass it in the filters key. Each element of filters is a JSON object which defines a filter on a specific field. All the elements of filters are joined with a logical “AND” operation when doing the search.Example:This query retrieves people from companies with a headcount between 1,001-5,000 or more than 10,001+, with annual revenue between 1 and 500 million USD, excluding those located in the United States, and returns the second page of results.BashCopycurl --location 'https://api.crustdata.com/screener/company/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--data '{
"filters": [
{
"filter\_type": "COMPANY\_HEADCOUNT",
"type": "in",
"value": ["10,001+", "1,001-5,000"]
},
{
"filter\_type": "ANNUAL\_REVENUE",
"type": "between",
"value": {"min": 1, "max": 500},
"sub\_filter": "USD"
},
{
"filter\_type": "REGION",
"type": "not in",
"value": ["United States"]
}
],
"page": 2
}'
​Response:[![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/zn02zfopXQas)​Key points:Credits: Each page request costs 25 creditsPagination: If the total number of results for the query is more than 25 (value of total\_display\_count param), you can paginate the response in the following ways (depending on your request)When passing linkedin\_sales\_navigator\_search\_url :adding page query param to linkedin\_sales\_navigator\_search\_url . For example, to get data on n th page, linkedin\_sales\_navigator\_search\_url would become https://www.linkedin.com/sales/search/company?page=n&query=... .Example request with page=2BashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--data '{
"linkedin\_sales\_navigator\_search\_url": "https://www.linkedin.com/sales/search/company?page=2&query=(filters%3AList((type%3ACOMPANY\_HEADCOUNT%2Cvalues%3AList((id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A25%2Ctext%3AManufacturing%2CselectionType%3AINCLUDED)))))&sessionId=8TR8HMz%2BTVOYaeivK9p%2Bpg%3D%3D"
}'
​When passing filters :provide page as one of the keys in the payload itseflExample request with page=2BashCopycurl --location 'https://api.crustdata.com/screener/company/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--data '{
"filters": [
{
"filter\_type": "COMPANY\_HEADCOUNT",
"type": "in",
"value": ["10,001+", "1,001-5,000"]
},
{
"filter\_type": "ANNUAL\_REVENUE",
"type": "between",
"value": {"min": 1, "max": 500},
"sub\_filter": "USD"
},
{
"filter\_type": "REGION",
"type": "not in",
"value": ["United States"]
}
],
"page": 2
}'
​Each page returns upto 25 results. To fetch all the results from a query, you should keep on iterating over pages until you cover the value of total\_display\_count in the response from first page.Latency: The data is fetched in real-time from Linkedin and the latency for this endpoint is between 10 to 30 seconds.Response schema: Because the data is fetched realtime, and the results may not be in Crustdata’s database already, the response schema will be different from c[ompany data enrichment endpoint](/116e4a7d95b180bc9dd0d9acac03ddd4?pvs=25) screener/company . But all the results will be added to Crustdata’s database in 60 min of your query and the data for a specific company profile can be enriched via [company enrichment endpoint](/116e4a7d95b180bc9dd0d9acac03ddd4?pvs=25)
### LinkedIn Posts by Company API (real-time)

Overview: This endpoint retrieves recent LinkedIn posts and related engagement metrics for a specified company.Each request returns up-to 5 results per page. To paginate, increment the page query param.Required: authentication token auth\_token for authorization.Request Use Case: Ideal for users who want to fetch recent LinkedIn posts and engagement data for a specific company.Note: You can provide one company LinkedIn URL per request.Request Parameters:company\_name (optional): Company namecompany\_domain (optional): Company domaincompany\_id (optional): Company IDcompany\_linkedin\_url (optional): Company LinkedIn URLfields (optional): comma separated list of fields which you want to get in response.all possible values:total\_reactionstotal\_commentstextshare\_urnshare\_urlreactorsreactions\_by\_type.PRAISEreactions\_by\_type.LIKEreactions\_by\_type.INTERESTreactions\_by\_type.ENTERTAINMENTreactions\_by\_type.EMPATHYreactions\_by\_type.CURIOUSreactions\_by\_type.APPRECIATIONreactions\_by\_typenum\_shareshyperlinks.person\_linkedin\_urlshyperlinks.other\_urlshyperlinks.company\_linkedin\_urlshyperlinksdate\_postedbackend\_urnactor\_nameyear\_foundeddefault: All fields except reactors :total\_reactions,total\_comments,text,share\_urn,share\_url,reactions\_by\_type\_PRAISE,reactions\_by\_type\_LIKE,reactions\_by\_type\_INTEREST,reactions\_by\_type\_ENTERTAINMENT,reactions\_by\_type\_EMPATHY,reactions\_by\_type\_CURIOUS,reactions\_by\_type\_APPRECIATION,reactions\_by\_type,num\_shares,hyperlinks\_person\_linkedin\_urls,hyperlinks\_other\_urls,hyperlinks\_company\_linkedin\_urls,hyperlinks,date\_posted,backend\_urn,actor\_name,year\_foundedpage (optional, default: 1): Page number for paginationlimit (optional, default: 5): Limit the number of posts in a pagepost\_types (optional, default: repost, original) All post typesoriginal: only original posts are returnedrepost : only reposted posts are returnedNote: Provide only one of the company identifiers.Example Request:With default fieldsBashCopycurl 'https://api.crustdata.com/screener/linkedin\_posts?company\_domain=https://crustdata.com&page=1' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​With default fields + reactorsBashCopycurl 'https://api.crustdata.com/screener/linkedin\_posts?company\_domain=https://crustdata.com&page=1&fields=reactors' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​With default post\_types BashCopycurl 'https://api.crustdata.com/screener/linkedin\_posts?company\_domain=https://crustdata.com&page=1&post\_types=repost%2C%20original' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​ResponseThe response provides a list of recent LinkedIn posts for the specified company, including post content, engagement metrics, and information about users who interacted with the posts.Full sample: [jsonhero.io](https://jsonhero.io/j/8O15yo2SVBHD)​Response Structure:JSONCopy{
"posts": [
{
"backend\_urn": "urn:li:activity:7236812027275419648",
"share\_urn": "urn:li:share:7236812026038083584",
"share\_url": "https://www.linkedin.com/posts/crustdata\_y-combinators-most-popular-startups-from-activity-7236812027275419648-4fyw?utm\_source=combined\_share\_message&utm\_medium=member\_desktop",
"text": "Y Combinator’s most popular startups.\nFrom the current S24 batch.\n\nHow do you gauge the buzz around these startups when most are pre-product?\n\nWe’ve defined web traffic as the metric to go by.\n\nHere are the most popular startups from YC S24: \n\n𝟭. 𝗡𝗲𝘅𝘁𝗨𝗜: Founded by Junior Garcia\n𝟮. 𝗪𝗼𝗿𝗱𝘄𝗮𝗿𝗲: Filip Kozera, Robert Chandler\n𝟯. 𝗨𝗻𝗿𝗶𝗱𝗱𝗹𝗲: Naveed Janmohamed\n𝟰. 𝗨𝗻𝗱𝗲𝗿𝗺𝗶𝗻𝗱: Thomas Hartke, Joshua Ramette\n𝟱. 𝗖𝗼𝗺𝗳𝘆𝗱𝗲𝗽𝗹𝗼𝘆: Nick Kao, Benny Kok\n𝟲. 𝗕𝗲𝗲𝗯𝗲𝘁𝘁𝗼𝗿: Jordan Murphy, Matthew Wolfe\n𝟳. 𝗠𝗲𝗿𝘀𝗲: Kumar A., Mark Rachapoom\n𝟴. 𝗟𝗮𝗺𝗶𝗻𝗮𝗿: Robert Kim, Din Mailibay, Temirlan Myrzakhmetov\n𝟵. 𝗠𝗶𝘁𝗼𝗛𝗲𝗮𝗹𝘁𝗵: Kenneth Lou, Tee-Ming C., Joel Kek, Ryan Ware\n𝟭𝟬. 𝗔𝘂𝘁𝗮𝗿𝗰: Etienne-Noel Krause,Thies Hansen, Marius Seufzer\n\n🤔 Interested in reading more about the YC S24 batch?\n\nRead our full breakdown from the link in the comments 👇",
"actor\_name": "Crustdata",
"date\_posted": "2024-09-03",
"hyperlinks": {
"company\_linkedin\_urls": [],
"person\_linkedin\_urls": [
"https://www.linkedin.com/in/ACoAAAKoldoBqSsiXY\_DHsXdSk1slibabeTvDDY"
],
"other\_urls": []
},
"total\_reactions": 37,
"total\_comments": 7,
"reactions\_by\_type": {
"LIKE": 28,
"EMPATHY": 4,
"PRAISE": 4,
"INTEREST": 1
},
"num\_shares": 5,
"is\_repost\_without\_thoughts": false,
"reactors": [
{
"name": "Courtney May",
"linkedin\_profile\_url": "https://www.linkedin.com/in/ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
"reaction\_type": "LIKE",
"profile\_image\_url": "https://media.licdn.com/dms/image/v2/D5603AQF-8vL\_c5H9Zg/profile-displayphoto-shrink\_100\_100/profile-displayphoto-shrink\_100\_100/0/1690558480623?e=1730937600&v=beta&t=Lm2hHLTFiEVlHWdTt-Vh3vDYevK8U8SlPqaFdNu3R6A",
"title": "GTM @ Arc (YC W22)",
"additional\_info": "3rd+",
"location": "San Francisco, California, United States",
"linkedin\_profile\_urn": "ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
"default\_position\_title": "GTM @ Arc (YC W22)",
"default\_position\_company\_linkedin\_id": "74725230",
"default\_position\_is\_decision\_maker": false,
"flagship\_profile\_url": "https://www.linkedin.com/in/courtney-may-8a178b172",
"profile\_picture\_url": "https://media.licdn.com/dms/image/v2/D5603AQF-8vL\_c5H9Zg/profile-displayphoto-shrink\_400\_400/profile-displayphoto-shrink\_400\_400/0/1690558480623?e=1730937600&v=beta&t=vHg233746zA00m3q2vHKSFcthL3YKiagTtVEZt1qqJI",
"headline": "GTM @ Arc (YC W22)",
"summary": null,
"num\_of\_connections": 786,
"related\_colleague\_company\_id": 74725230,
"skills": [
"Marketing Strategy",
"Product Support",
"SOC 2",
...
],
"employer": [
{
"title": "GTM @ Arc (YC W22)",
"company\_name": "Arc",
"company\_linkedin\_id": "74725230",
"start\_date": "2024-07-01T00:00:00",
"end\_date": null,
"description": null,
"location": "San Francisco, California, United States",
"rich\_media": []
},
{
"title": "Product Marketing & Operations Lead",
"company\_name": "Bits of Stock™",
"company\_linkedin\_id": "10550545",
"start\_date": "2023-03-01T00:00:00",
"end\_date": "2024-07-01T00:00:00",
"description": "● Spearheaded SOC 2 Certification and oversaw compliance organization for internal and external needs.\n● Leads a weekly operations call to manage customer support, new user onboarding, and other outstanding operational matters.\n● Wrote & launched: Product Blog with 6 different featured pieces; 2 Pricing Thought-Leadership pieces; & 2 Partner Press Releases; two of which were featured in the WSJ.\n● Managed marketing and logistics for 11 conferences and events all over the world, producing over 150 B2B qualified leads.\n● Created a company-wide marketing strategy and implemented it across the blog, LinkedIn, & Twitter leading to a 125% increased engagement rate & a 29% increase in followers.\n● Aided in sales and partner relations by preparing a Partner Marketing Guide, creating the user support section of the website and inbound email system, and investing education guide.",
"location": "San Francisco Bay Area",
"rich\_media": []
},
...
],
"education\_background": [
{
"degree\_name": "Bachelor of Applied Science - BASc",
"institute\_name": "Texas Christian University",
"field\_of\_study": "Economics",
"start\_date": "2016-01-01T00:00:00",
"end\_date": "2020-01-01T00:00:00"
}
],
"emails": [
"email@example.com"
],
"websites": [],
"twitter\_handle": null,
"languages": [],
"pronoun": null,
"current\_title": "GTM @ Arc (YC W22)"
}, ...
]
}
]
}
​Each item in the posts array contains the following fields:backend\_urn (string): Unique identifier for the post in LinkedIn's backend system.share\_urn (string): Unique identifier for the shared content.share\_url (string): Direct URL to the post on LinkedIn.text (string): The full content of the post.actor\_name (string): Name of the company or person who created the post.hyperlinks (object): Contains the external links and Company/Person LinkedIn urls mentioned in the postcompany\_linkedin\_urls (array): List of Company LinkedIn urls mentioned in the postperson\_linkedin\_urls (array): List of Person LinkedIn urls mentioned in the postdate\_posted (string): Date when the post was published, in "YYYY-MM-DD" format.total\_reactions (integer): Total number of reactions on the post.total\_comments (integer): Total number of comments on the post.reactions\_by\_type (object): Breakdown of reactions by type.Possible types include: "LIKE", "EMPATHY", "PRAISE", "INTEREST", etc.Each type is represented by its count (integer).num\_shares (integer): Number of times the post has been shared.reactors (array): List of users who reacted to the post. Each reactor object contains:name (string): Full name of the person who reacted.linkedin\_profile\_url (string): URL to the reactor's LinkedIn profile.reaction\_type (string): Type of reaction given (e.g., "LIKE", "EMPATHY").profile\_image\_url (string): URL to the reactor's profile image (100x100 size).title (string): Current professional title of the reactor.additional\_info (string): Additional information, often indicating connection degree.location (string): Geographic location of the reactor.linkedin\_profile\_urn (string): Unique identifier for the reactor's LinkedIn profile.default\_position\_title (string): Primary job title.default\_position\_company\_linkedin\_id (string): LinkedIn ID of the reactor's primary company.default\_position\_is\_decision\_maker (boolean): Indicates if the reactor is in a decision-making role.flagship\_profile\_url (string): Another form of the reactor's LinkedIn profile URL.profile\_picture\_url (string): URL to a larger version of the profile picture (400x400 size).headline (string): Professional headline from the reactor's LinkedIn profile.summary (string or null): Brief professional summary, if available.num\_of\_connections (integer): Number of LinkedIn connections the reactor has.related\_colleague\_company\_id (integer): LinkedIn ID of a related company, possibly current employer.skills (array of strings): List of professional skills listed on the reactor's profile.employer (array of objects): Employment history, each containing:title (string): Job title.company\_name (string): Name of the employer.company\_linkedin\_id (string or null): LinkedIn ID of the company.start\_date (string): Start date of employment in ISO format.end\_date (string or null): End date of employment in ISO format, or null if current.description (string or null): Job description, if available.location (string or null): Job location.rich\_media (array): Currently empty, may contain media related to the job.education\_background (array of objects): Educational history, each containing:degree\_name (string): Type of degree obtained.institute\_name (string): Name of the educational institution.field\_of\_study (string): Area of study.start\_date (string): Start date of education in ISO format.end\_date (string): End date of education in ISO format.emails (array of strings): Known email addresses associated with the reactor.websites (array): Currently empty, may contain personal or professional websites.twitter\_handle (string or null): Twitter username, if available.languages (array): Currently empty, may contain languages spoken.pronoun (string or null): Preferred pronouns, if specified.current\_title (string): Current job title, often identical to default\_position\_title.Key PointsCredits: Without reactors (default): Each successful page request costs 5 creditsWith reactors: Each successful page request costs 25 creditsPagination: Increment the value of page query param to fetch the next set of posts. Most recent posts will be in first page and then so on. Currently, you can only fetch only upto 20 pages of latest posts. In case you want to fetch more, contact Crustdata team at [info@crustdata.com](mailto:info@crustdata.com) .External urls or Company/Person LinkedIn urls mentioned in text:hyperlinks contains list of links (categorized as company\_linkedin\_urls , person\_linkedin\_urls and other\_urls ) mentioned in the postLatency: The data is fetched in real-time from Linkedin and the latency for this endpoint is between 30 to 60 seconds depending on number of reactions for all the posts in the page
### LinkedIn Posts Keyword Search (real-time)

Overview: This endpoint retrieves LinkedIn posts containing specified keywords along with related engagement metrics.Each request returns 5 posts per page. To paginate, increment the page in the payload.Required: authentication token auth\_token for authorization.Request Request Body Overview The request body is a JSON object that contains the following parameters:

| Parameter | Description | Default | Required |
| --- | --- | --- | --- |
| keyword | The keyword or phrase to search for in LinkedIn posts. |  | Yes |
| page | Page number for pagination | 1 | Yes |
| limit | Limit the number of posts in a page | 5 | No |
| sort\_by | Defines the sorting order of the results Can be either of the following: 1. “relevance” - to sort on top match 2. “date\_posted” - to sort on latest posts | “date\_posted” | No |
| date\_posted | Filters posts by the date they were posted. Can be one of the following: 1. “past-24h” - Posts from last 24 hours 2. “past-week” - Post from last 7 days 3. “past-month” - Post from last 30 days 4. “past-quarter” - Post from last 3 months 5. “past-year” - Post from last 1 year | “past-24h” | No |

 \* limit can not exceed 5 when page is provided in the payload. To retrieve posts in bulk, use the limit parameter (with value over 5 allowed here) without the page parameter.In the example below, we get LinkedIn posts that meet the following criteria:Get all the posts with “LLM evaluation”  keyword Posted in last 3 monthscURLBashCopycurl 'https://api.crustdata.com/screener/linkedin\_posts/keyword\_search/' \
-H 'Accept: application/json, text/plain, /' \
-H 'Accept-Language: en-US,en;q=0.9' \
-H 'Authorization: Token $auth\_token' \
-H 'Connection: keep-alive' \
-H 'Content-Type: application/json' \
-H 'Origin: https://crustdata.com' \
--data-raw '{
"keyword":"LLM Evaluation",
"page":1,
"sort\_by":"relevance",
"date\_posted":"past-quarter"
}' \
--compressed
​PythonPythonCopyimport requests
headers = {
'Accept': 'application/json, text/plain, /',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Token $auth\_token', # replace $auth\_token
'Connection': 'keep-alive',
'Content-Type': 'application/json',
'Origin': 'https://crustdata.com'
}
json\_data = {
"keyword":"LLM Evaluation",
"page":1,
"sort\_by":"relevance",
"date\_posted":"past-quarter"
}
response = requests.post('https://api.crustdata.com/screener/linkedin\_posts/keyword\_search/', headers=headers, json=json\_data)
​Response:The response provides a list of recent LinkedIn posts for the specified company, including post content, engagement metrics, and information about users who interacted with the posts.Refer to actor\_type field to identify if the post is published by a person or a company Full sample: <https://jsonhero.io/j/XIqoVuhe2x9w>Key PointsCredits: Each successful page request costs 5 credits.Pagination: Increment the value of page query param to fetch the next set of posts. Each page has 5 posts. limit can not exceed 5 when page is provided in the payload. To retrieve posts in bulk, use the limit parameter (with value over 5 allowed here) without the page parameter.Latency: The data is fetched in real-time from Linkedin and the latency for this endpoint is between 5 to 10 seconds depending on number of posts fetched in a request.
## People Endpoints

### Enrichment: People Profile(s) API

Overview: Enrich data for one or more individuals using LinkedIn profile URLs or business email addresses. This API allows you to retrieve enriched person data from Crustdata’s database or perform a real-time search from the web if the data is not available.Key Features:Enrich data using LinkedIn profile URLs or business email addresses (3 credit per profile/email)Option to perform a real-time search if data is not present in the database (5 credit per profile/email)Retrieve data for up to 25 profiles or emails in a single request.Required: authentication token auth\_token for authorization.Request:Query Parameterslinkedin\_profile\_url (optional): Comma-separated list of LinkedIn profile URLs.Example: linkedin\_profile\_url=https://www.linkedin.com/in/johndoe/,https://www.linkedin.com/in/janedoe/PythonCopycurl 'https://api.crustdata.com/screener/person/enrich?linkedin\_profile\_url=https://www.linkedin.com/in/dtpow/,https://www.linkedin.com/in/janedoe/' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​business\_email (optional): Person business email address.Note:- You can only provide one business email address per requestExample: business\_email=john.doe@example.comPythonCopycurl 'https://api.crustdata.com/screener/person/enrich?business\_email=john.doe@example.com' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​enrich\_realtime (optional): Boolean (True or False). If set to True, performs a real-time search from the web if data is not found in the database.Default: FalseExample:PythonCopycurl 'https://api.crustdata.com/screener/person/enrich?linkedin\_profile\_url=https://www.linkedin.com/in/dtpow/,https://www.linkedin.com/in/janedoe/&enrich\_realtime=True' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​fields (optional): string (comma-separated list of fields). Specifies the fields you want to include in the response. Possible Valueslinkedin\_profile\_url: stringlinkedin\_flagship\_url: stringname: stringlocation: stringemail: stringtitle: stringlast\_updated: stringheadline: stringsummary: stringnum\_of\_connections: stringskills: array of stringsprofile\_picture\_url: stringtwitter\_handle: string languages: array of strings linkedin\_open\_to\_cards: array of strings all\_employers: array of objects past\_employers: array of objectscurrent\_employers: array of objectseducation\_background.degree\_name: key with string value in array of objectseducation\_background.end\_date: key with string value in array of objectseducation\_background.field\_of\_study: key with string value in array of objectseducation\_background.institute\_linkedin\_id: key with string value in array of objectseducation\_background.institute\_linkedin\_url: key with string value in array of objectseducation\_background.institute\_logo\_url: key with string value in array of objectseducation\_background.institute\_name: key with string value in array of objectseducation\_background.start\_date: key with string value in array of objectseducation\_background.activities\_and\_societies: key with string value in array of objectscertifications: array of objectshonors: array of objectsall\_employers\_company\_id: array of integersall\_titles: array of stringsall\_schools: array of stringsall\_degrees: array of stringsall\_connections: array of stringsExample: fields=all\_degrees,education\_backgroundNotes:Mandatory Parameters: You must provide either linkedin\_profile\_url or business\_email. Do not include both in the same request.Formatting: Multiple URLs or emails should be comma-separated. Extra spaces or tabs before or after commas are ignored.Multiple LinkedIn profile URLs should be separated by commas. Extra spaces or tabs before or after commas will be ignored.FieldsIf you don’t use fields, you will get all the fields in response except all\_connections, linkedin\_open\_to\_cards,certifications  , honors & education\_background.activities\_and\_societiesAccess to certain fields may be restricted based on your user permissions. If you request fields you do not have access to, the API will return an error indicating unauthorized access.Top level non-object fields are present in response irrespective of fields.Don’t include metadata fields : enriched\_realtime, score and query\_linkedin\_profile\_urn\_or\_slug in fieldsExamples1. Request with all fields:Usecase: Ideal for users who wants to access all fields which are not provided by defaultBashCopycurl -X GET "https://api.crustdata.com/screener/person/enrich?linkedin\_profile\_url=https://www.linkedin.com/in/sasikumarm00&enrich\_realtime=true&fields=linkedin\_profile\_url,linkedin\_flagship\_url,name,location,email,title,last\_updated,headline,summary,num\_of\_connections,skills,profile\_picture\_url,twitter\_handle,languages,linkedin\_open\_to\_cards,all\_employers,past\_employers,current\_employers,education\_background.degree\_name,education\_background.end\_date,education\_background.field\_of\_study,education\_background.institute\_linkedin\_id,education\_background.institute\_linkedin\_url,education\_background.institute\_logo\_url,education\_background.institute\_name,education\_background.start\_date,education\_background.activities\_and\_societies,certifications,honors,all\_employers\_company\_id,all\_titles,all\_schools,all\_degrees,all\_connections" \
-H "Authorization: Token auth\_token" \,
-H "Content-Type: application/json"
​2. Request with all default fields AND education\_background.activities\_and\_societies:BashCopycurl -X GET "https://api.crustdata.com/screener/person/enrich?linkedin\_profile\_url=https://www.linkedin.com/in/sasikumarm00&enrich\_realtime=true&fields=linkedin\_profile\_url,linkedin\_flagship\_url,name,location,email,title,last\_updated,headline,summary,num\_of\_connections,skills,profile\_picture\_url,twitter\_handle,languages,all\_employers,past\_employers,current\_employers,education\_background.degree\_name,education\_background.end\_date,education\_background.field\_of\_study,education\_background.institute\_linkedin\_id,education\_background.institute\_linkedin\_url,education\_background.institute\_logo\_url,education\_background.institute\_name,education\_background.start\_date,education\_background.activities\_and\_societies,all\_employers\_company\_id,all\_titles,all\_schools,all\_degrees" \
-H "Authorization: Token auth\_token" \
-H "Content-Type: application/json"
​3. Request with all default fields AND certifications , honors and linkedin\_open\_to\_cards :BashCopycurl -X GET "https://api.crustdata.com/screener/person/enrich?linkedin\_profile\_url=https://www.linkedin.com/in/sasikumarm00&enrich\_realtime=true&fields=linkedin\_profile\_url,linkedin\_flagship\_url,name,location,email,title,last\_updated,headline,summary,num\_of\_connections,skills,profile\_picture\_url,twitter\_handle,languages,all\_employers,past\_employers,current\_employers,education\_background.degree\_name,education\_background.end\_date,education\_background.field\_of\_study,education\_background.institute\_linkedin\_id,education\_background.institute\_linkedin\_url,education\_background.institute\_logo\_url,education\_background.institute\_name,education\_background.start\_date,all\_employers\_company\_id,all\_titles,all\_schools,all\_degrees,linkedin\_open\_to\_cards,certifications,honors" \
-H "Authorization: Token auth\_token" \
-H "Content-Type: application/json"
​4. Request without fields:BashCopycurl -X GET "https://api.crustdata.com/screener/person/enrich?linkedin\_profile\_url=https://www.linkedin.com/in/sasikumarm00&enrich\_realtime=true" \
-H "Authorization: Token auth\_token" \
-H "Content-Type: application/json"
​5. Request with business email:BashCopycurl -X GET "https://api.crustdata.com/screener/person/enrich?business\_email=shubham.joshi@coindcx.com&enrich\_realtime=true" \
-H "Authorization: Token auth\_token" \
-H "Content-Type: application/json"
​Response:When LinkedIn profiles are present in Crustdata’s database:Response will include the enriched data for each profile. [JSON Hero](https://jsonhero.io/j/UEyFru4RDLoI)When one or more LinkedIn profiles are not present in Crustdata’s database:An error message will be returned for each profile not found, along with instructions to query again after 60 minutes. [![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/kwdasun8HdqM)​Response with all possible fields: [![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/zenKXWh36HsM)​NotesIf some profiles or emails are not found in the database and enrich\_realtime=False, an empty response for those entries is returned, and they will be auto-enriched in the background. Query again after at least 60 minutes to retrieve the data.If enrich\_realtime=True and the profile or email cannot be found even via real-time search, an error message is returned for those entries.Key points:LatencyDatabase Search: Less than 10 seconds per profile.Real-Time Search: May take longer due to fetching data from the web.LimitsProfiles/Emails per Request: Up to 25.Exceeding Limits: Requests exceeding this limit will be rejected with an error message.CreditsDatabase Enrichment:3 credits per LinkedIn profile or email.Real-Time Enrichment (enrich\_realtime=True):5 credits per LinkedIn profile or email.ConstraintsValid Input: Ensure all LinkedIn URLs and email addresses are correctly formatted.Invalid inputs result in validation errors.Mutually Exclusive Parameters: Do not include both linkedin\_profile\_url and business\_email in the same request.Independent Processing: Each profile or email is processed independently.Found entries are returned immediatelyNot found entries trigger the enrichment process (if enrich\_realtime=False)
### Search: LinkedIn People Search API (real-time)

Overview: Search for people profiles based on either a direct LinkedIn Sales Navigator search URL or a custom search criteria as a filter. This endpoint allows you to retrieve detailed information about individuals matching specific criteria.Each request returns upto 25 results. To paginate, update the page number of the Sales Navigator search URL and do the request again.In the request payload, either set the url of the Sales Navigator Leads search from your browser in the parameter linkedin\_sales\_navigator\_search\_url or specify the search criteria as a JSON object in the parameter filtersRequired: authentication token auth\_token for authorization.
#### Making Requests

Request:
#### Request Body:

The request body can have the following keys (atleast one of them is required)linkedin\_sales\_navigator\_search\_url (optional): URL of the Sales Navigator Leads search from the browserfilters (optional): JSON dictionary defining the search criteria as laid out by the [Crustdata filter schema](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#116e4a7d95b180528ce4f6c485a76c40).page (optional): Page number for pagination (used only with filters)preview (optional): Boolean field to get the preview of profiles. When using preview don’t use page. 
#### Examples

Via LinkedIn Sales Navigator URL:Plain TextCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--data '{
"linkedin\_sales\_navigator\_search\_url": "https://www.linkedin.com/sales/search/people?query=(recentSearchParam%3A(id%3A3940840412%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3ACOMPANY\_HEADCOUNT%2Cvalues%3AList((id%3AC%2Ctext%3A11-50%2CselectionType%3AINCLUDED)%2C(id%3AB%2Ctext%3A1-10%2CselectionType%3AINCLUDED)%2C(id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)%2C(id%3AE%2Ctext%3A201-500%2CselectionType%3AINCLUDED)%2C(id%3AF%2Ctext%3A501-1000%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A41%2Ctext%3ABanking%2CselectionType%3AINCLUDED)%2C(id%3A43%2Ctext%3AFinancial%20Services%2CselectionType%3AINCLUDED)))%2C(type%3ACOMPANY\_HEADQUARTERS%2Cvalues%3AList((id%3A105912732%2Ctext%3ABelize%2CselectionType%3AINCLUDED)%2C(id%3A101739942%2Ctext%3ACosta%20Rica%2CselectionType%3AINCLUDED)%2C(id%3A106522560%2Ctext%3AEl%20Salvador%2CselectionType%3AINCLUDED)%2C(id%3A100877388%2Ctext%3AGuatemala%2CselectionType%3AINCLUDED)%2C(id%3A101937718%2Ctext%3AHonduras%2CselectionType%3AINCLUDED)%2C(id%3A105517145%2Ctext%3ANicaragua%2CselectionType%3AINCLUDED)%2C(id%3A100808673%2Ctext%3APanama%2CselectionType%3AINCLUDED)%2C(id%3A100270819%2Ctext%3AAntigua%20and%20Barbuda%2CselectionType%3AINCLUDED)%2C(id%3A106662619%2Ctext%3AThe%20Bahamas%2CselectionType%3AINCLUDED)%2C(id%3A102118611%2Ctext%3ABarbados%2CselectionType%3AINCLUDED)%2C(id%3A106429766%2Ctext%3ACuba%2CselectionType%3AINCLUDED)%2C(id%3A105057336%2Ctext%3ADominican%20Republic%2CselectionType%3AINCLUDED)%2C(id%3A100720695%2Ctext%3ADominica%2CselectionType%3AINCLUDED)%2C(id%3A104579260%2Ctext%3AGrenada%2CselectionType%3AINCLUDED)%2C(id%3A100993490%2Ctext%3AHaiti%2CselectionType%3AINCLUDED)%2C(id%3A105126983%2Ctext%3AJamaica%2CselectionType%3AINCLUDED)%2C(id%3A102098694%2Ctext%3ASaint%20Kitts%20and%20Nevis%2CselectionType%3AINCLUDED)%2C(id%3A104022923%2Ctext%3ASaint%20Lucia%2CselectionType%3AINCLUDED)%2C(id%3A104703990%2Ctext%3ASaint%20Vincent%20and%20the%20Grenadines%2CselectionType%3AINCLUDED)%2C(id%3A106947126%2Ctext%3ATrinidad%20and%20Tobago%2CselectionType%3AINCLUDED)%2C(id%3A107592510%2Ctext%3ABelize%20City%2C%20Belize%2C%20Belize%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY\_LEVEL%2Cvalues%3AList((id%3A110%2Ctext%3AEntry%20Level%2CselectionType%3AEXCLUDED)%2C(id%3A100%2Ctext%3AIn%20Training%2CselectionType%3AEXCLUDED)%2C(id%3A200%2Ctext%3AEntry%20Level%20Manager%2CselectionType%3AEXCLUDED)%2C(id%3A130%2Ctext%3AStrategic%2CselectionType%3AEXCLUDED)%2C(id%3A300%2Ctext%3AVice%20President%2CselectionType%3AINCLUDED)%2C(id%3A220%2Ctext%3ADirector%2CselectionType%3AINCLUDED)%2C(id%3A320%2Ctext%3AOwner%20%2F%20Partner%2CselectionType%3AINCLUDED)%2C(id%3A310%2Ctext%3ACXO%2CselectionType%3AINCLUDED)))))&sessionId=UQyc2xY6ROisdd%2F%2B%2BsxmJA%3D%3D"
}'​Via Custom Search Filters:Refer [Building the Company/People Search Criteria Filter](https://crustdata.notion.site/Building-the-Company-People-Search-Criteria-Filter-c66d5236e8ea40df8af114f6d447ab48?pvs=24#116e4a7d95b180528ce4f6c485a76c40) to build the custom search filter for your query and pass it in the filters key. Each element of filters is a JSON object which defines a filter on a specific field. All the elements of filters are joined with a logical “AND” operation when doing the search.Example:This query retrieves people working at Google or Microsoft, excluding those with the titles Software Engineer or Data Scientist, based in companies headquartered in United States or Canada, from the Software Development or Hospitals and Health Care industries, while excluding people located in California, United States or New York, United StatesBashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--data '{
"filters": [
{
"filter\_type": "CURRENT\_COMPANY",
"type": "in",
"value": ["Google", "Microsoft"]
},
{
"filter\_type": "CURRENT\_TITLE",
"type": "not in",
"value": ["Software Engineer", "Data Scientist"]
},
{
"filter\_type": "COMPANY\_HEADQUARTERS",
"type": "in",
"value": ["United States", "Canada"]
},
{
"filter\_type": "INDUSTRY",
"type": "in",
"value": ["Software Development", "Hospitals and Health Care"]
},
{
"filter\_type": "REGION",
"type": "not in",
"value": ["California, United States", "New York, United States"]
}
],
"page": 1
}'
​More Examples1. People with specific first name from a specific company given company’s domainBashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--data '{
"filters": [
{
"filter\_type": "FIRST\_NAME",
"type": "in",
"value": ["steve"]
},
{
"filter\_type": "CURRENT\_COMPANY",
"type": "in",
"value": ["buzzbold.com"]
}
],
"page": 1
}'
​2. People with specific first name from a specific company given company’s linkedin urlBashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--data '{
"filters": [
{
"filter\_type": "FIRST\_NAME",
"type": "in",
"value": ["Ali"]
},
{
"filter\_type": "CURRENT\_COMPANY",
"type": "in",
"value": ["https://www.linkedin.com/company/serverobotics"]
}
],
"page": 1
}'
​3. Preview list of people given filter criteriaBashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Authorization: Token $token' \
--data '{"filters":[
{
"filter\_type": "CURRENT\_COMPANY",
"type": "in",
"value": ["serverobotics.com"]
},
{
"filter\_type": "REGION",
"type": "in",
"value": ["United States"]
}
],
"preview": true
}'
​4. People that recently changed jobs and are currently working at a specific companyBashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Authorization: Token $token' \
--data '{"filters":[
{
"filter\_type": "CURRENT\_COMPANY",
"type": "in",
"value": ["serverobotics.com"]
},
{
"filter\_type": "RECENTLY\_CHANGED\_JOBS"
}
]
}'
​5. All people working at a specific company (upto 2500)BashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Authorization: Token $token' \
--data '{"filters":[
{
"filter\_type": "CURRENT\_COMPANY",
"type": "in",
"value": ["serverobotics.com"]
}
],
"limit": 200
}'
​Response:Default (without preview=True): [![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/t2CJ3nG7Xymv)​With preview=True : [![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/yDSFQui0BKx8)​Response with preview[![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/V2VkhY4KrHSF)​Key points:Credits: Each successful page request costs 25 credits. With preview , a successful request costs 5 credits.Pagination: If the total number of results for the query is more than 25 (value of total\_display\_count param), you can paginate the response in the following ways (depending on your request)When passing linkedin\_sales\_navigator\_search\_url :adding page query param to linkedin\_sales\_navigator\_search\_url . For example, to get data on nth page, linkedin\_sales\_navigator\_search\_url would become https://www.linkedin.com/sales/search/people?page=n&query=... .Example request with page=2BashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--data '{
"linkedin\_sales\_navigator\_search\_url": "https://www.linkedin.com/sales/search/people?page=2&query=(recentSearchParam%3A(id%3A3940840412%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3ACOMPANY\_HEADCOUNT%2Cvalues%3AList((id%3AC%2Ctext%3A11-50%2CselectionType%3AINCLUDED)%2C(id%3AB%2Ctext%3A1-10%2CselectionType%3AINCLUDED)%2C(id%3AD%2Ctext%3A51-200%2CselectionType%3AINCLUDED)%2C(id%3AE%2Ctext%3A201-500%2CselectionType%3AINCLUDED)%2C(id%3AF%2Ctext%3A501-1000%2CselectionType%3AINCLUDED)))%2C(type%3AINDUSTRY%2Cvalues%3AList((id%3A41%2Ctext%3ABanking%2CselectionType%3AINCLUDED)%2C(id%3A43%2Ctext%3AFinancial%20Services%2CselectionType%3AINCLUDED)))%2C(type%3ACOMPANY\_HEADQUARTERS%2Cvalues%3AList((id%3A105912732%2Ctext%3ABelize%2CselectionType%3AINCLUDED)%2C(id%3A101739942%2Ctext%3ACosta%20Rica%2CselectionType%3AINCLUDED)%2C(id%3A106522560%2Ctext%3AEl%20Salvador%2CselectionType%3AINCLUDED)%2C(id%3A100877388%2Ctext%3AGuatemala%2CselectionType%3AINCLUDED)%2C(id%3A101937718%2Ctext%3AHonduras%2CselectionType%3AINCLUDED)%2C(id%3A105517145%2Ctext%3ANicaragua%2CselectionType%3AINCLUDED)%2C(id%3A100808673%2Ctext%3APanama%2CselectionType%3AINCLUDED)%2C(id%3A100270819%2Ctext%3AAntigua%20and%20Barbuda%2CselectionType%3AINCLUDED)%2C(id%3A106662619%2Ctext%3AThe%20Bahamas%2CselectionType%3AINCLUDED)%2C(id%3A102118611%2Ctext%3ABarbados%2CselectionType%3AINCLUDED)%2C(id%3A106429766%2Ctext%3ACuba%2CselectionType%3AINCLUDED)%2C(id%3A105057336%2Ctext%3ADominican%20Republic%2CselectionType%3AINCLUDED)%2C(id%3A100720695%2Ctext%3ADominica%2CselectionType%3AINCLUDED)%2C(id%3A104579260%2Ctext%3AGrenada%2CselectionType%3AINCLUDED)%2C(id%3A100993490%2Ctext%3AHaiti%2CselectionType%3AINCLUDED)%2C(id%3A105126983%2Ctext%3AJamaica%2CselectionType%3AINCLUDED)%2C(id%3A102098694%2Ctext%3ASaint%20Kitts%20and%20Nevis%2CselectionType%3AINCLUDED)%2C(id%3A104022923%2Ctext%3ASaint%20Lucia%2CselectionType%3AINCLUDED)%2C(id%3A104703990%2Ctext%3ASaint%20Vincent%20and%20the%20Grenadines%2CselectionType%3AINCLUDED)%2C(id%3A106947126%2Ctext%3ATrinidad%20and%20Tobago%2CselectionType%3AINCLUDED)%2C(id%3A107592510%2Ctext%3ABelize%20City%2C%20Belize%2C%20Belize%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY\_LEVEL%2Cvalues%3AList((id%3A110%2Ctext%3AEntry%20Level%2CselectionType%3AEXCLUDED)%2C(id%3A100%2Ctext%3AIn%20Training%2CselectionType%3AEXCLUDED)%2C(id%3A200%2Ctext%3AEntry%20Level%20Manager%2CselectionType%3AEXCLUDED)%2C(id%3A130%2Ctext%3AStrategic%2CselectionType%3AEXCLUDED)%2C(id%3A300%2Ctext%3AVice%20President%2CselectionType%3AINCLUDED)%2C(id%3A220%2Ctext%3ADirector%2CselectionType%3AINCLUDED)%2C(id%3A320%2Ctext%3AOwner%20%2F%20Partner%2CselectionType%3AINCLUDED)%2C(id%3A310%2Ctext%3ACXO%2CselectionType%3AINCLUDED)))))&sessionId=UQyc2xY6ROisdd%2F%2B%2BsxmJA%3D%3D"
}'
​When passing filters :provide page as one of the keys in the payload itselfExample request with page=1 BashCopycurl --location 'https://api.crustdata.com/screener/person/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--data '{
"filters": [
{
"filter\_type": "CURRENT\_COMPANY",
"type": "in",
"value": ["Google", "Microsoft"]
},
{
"filter\_type": "CURRENT\_TITLE",
"type": "not in",
"value": ["Software Engineer", "Data Scientist"]
},
{
"filter\_type": "COMPANY\_HEADQUARTERS",
"type": "in",
"value": ["United States", "Canada"]
},
{
"filter\_type": "INDUSTRY",
"type": "in",
"value": ["Software Development", "Hospitals and Health Care"]
},
{
"filter\_type": "REGION",
"type": "not in",
"value": ["California, United States", "New York, United States"]
}
],
"page": 1
}'
​Each page returns upto 25 results. To fetch all the results from a query, you should keep on iterating over pages until you cover the value of total\_display\_count in the response from first page.Latency: The data is fetched in real-time from Linkedin and the latency for this endpoint is between 10 to 30 seconds.Response schema: Because the data is fetched realtime, and the results may not be in Crustdata’s database already, the response schema will be different from [person enrichment endpoint](/116e4a7d95b180bc9dd0d9acac03ddd4?pvs=25) screener/people/enrich . But all the results will be added to Crustdata’s database in 10 min of your query and the data for a specific person profile can be enriched via [person enrichment endpoint](/116e4a7d95b180bc9dd0d9acac03ddd4?pvs=25) 
### LinkedIn Posts by Person API (real-time)

Overview: This endpoint retrieves recent LinkedIn posts and related engagement metrics for a specified person.Each request returns up-to 5 results per page. To paginate, increment the page query param.Required: authentication token auth\_token for authorization.Request Use Case: Ideal for users who want to fetch recent LinkedIn posts and engagement data for a specific company.Note: You can provide one company LinkedIn URL per request.Request Parameters:person\_linkedin\_url (required): LinkedIn profile url of the person. For example, any of these formats work <https://linkedin.com/in/abhilash-chowdhary> (flagship url) or <https://linkedin.com/in/ACoAAAAsKtMBHQPJ9rgxpUs8M6pSxrAYCXIX8oY> (fsd\_profile url)fields (optional): comma separated list of fields which you want to get in response.all possible values:total\_reactionstotal\_commentstextshare\_urnshare\_urlreactorsreactions\_by\_type.PRAISEreactions\_by\_type.LIKEreactions\_by\_type.INTERESTreactions\_by\_type.ENTERTAINMENTreactions\_by\_type.EMPATHYreactions\_by\_type.CURIOUSreactions\_by\_type.APPRECIATIONreactions\_by\_typenum\_shareshyperlinks.person\_linkedin\_urlshyperlinks.other\_urlshyperlinks.company\_linkedin\_urlshyperlinksdate\_postedbackend\_urnactor\_nameyear\_foundeddefault: All fields except reactors :total\_reactions,total\_comments,text,share\_urn,share\_url,reactions\_by\_type\_PRAISE,reactions\_by\_type\_LIKE,reactions\_by\_type\_INTEREST,reactions\_by\_type\_ENTERTAINMENT,reactions\_by\_type\_EMPATHY,reactions\_by\_type\_CURIOUS,reactions\_by\_type\_APPRECIATION,reactions\_by\_type,num\_shares,hyperlinks\_person\_linkedin\_urls,hyperlinks\_other\_urls,hyperlinks\_company\_linkedin\_urls,hyperlinks,date\_posted,backend\_urn,actor\_name,year\_foundedpage (optional, default: 1): Page number for paginationlimit (optional, default: 5): Limit the number of posts in a pagepost\_types (optional, default: repost, original) All post typesoriginal: only original posts are returnedrepost : only reposted posts are returnedExample Request:With default fields (without reactors)BashCopycurl 'https://api.crustdata.com/screener/linkedin\_posts?person\_linkedin\_url=https://linkedin.com/in/abhilash-chowdhary&page=1' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​With default fields and reactorsBashCopycurl 'https://api.crustdata.com/screener/linkedin\_posts?person\_linkedin\_url=https://linkedin.com/in/abhilash-chowdhary&page=1&fields=reactors' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​With default post\_types BashCopycurl 'https://api.crustdata.com/screener/linkedin\_posts?person\_linkedin\_url=https://linkedin.com/in/abhilash-chowdhary&page=1&post\_types=post\_types=repost%2C%20original' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​ResponseThe response provides a list of recent LinkedIn posts for the specified company, including post content, engagement metrics, and information about users who interacted with the posts.Full sample: [jsonhero.io](https://jsonhero.io/j/lGFH6zi5y9rP)​Response Structure:JSONCopy{
"posts": [
{
"backend\_urn": "urn:li:activity:7236812027275419648",
"share\_urn": "urn:li:share:7236812026038083584",
"share\_url": "https://www.linkedin.com/posts/crustdata\_y-combinators-most-popular-startups-from-activity-7236812027275419648-4fyw?utm\_source=combined\_share\_message&utm\_medium=member\_desktop",
"text": "Y Combinator’s most popular startups.\nFrom the current S24 batch.\n\nHow do you gauge the buzz around these startups when most are pre-product?\n\nWe’ve defined web traffic as the metric to go by.\n\nHere are the most popular startups from YC S24: \n\n𝟭. 𝗡𝗲𝘅𝘁𝗨𝗜: Founded by Junior Garcia\n𝟮. 𝗪𝗼𝗿𝗱𝘄𝗮𝗿𝗲: Filip Kozera, Robert Chandler\n𝟯. 𝗨𝗻𝗿𝗶𝗱𝗱𝗹𝗲: Naveed Janmohamed\n𝟰. 𝗨𝗻𝗱𝗲𝗿𝗺𝗶𝗻𝗱: Thomas Hartke, Joshua Ramette\n𝟱. 𝗖𝗼𝗺𝗳𝘆𝗱𝗲𝗽𝗹𝗼𝘆: Nick Kao, Benny Kok\n𝟲. 𝗕𝗲𝗲𝗯𝗲𝘁𝘁𝗼𝗿: Jordan Murphy, Matthew Wolfe\n𝟳. 𝗠𝗲𝗿𝘀𝗲: Kumar A., Mark Rachapoom\n𝟴. 𝗟𝗮𝗺𝗶𝗻𝗮𝗿: Robert Kim, Din Mailibay, Temirlan Myrzakhmetov\n𝟵. 𝗠𝗶𝘁𝗼𝗛𝗲𝗮𝗹𝘁𝗵: Kenneth Lou, Tee-Ming C., Joel Kek, Ryan Ware\n𝟭𝟬. 𝗔𝘂𝘁𝗮𝗿𝗰: Etienne-Noel Krause,Thies Hansen, Marius Seufzer\n\n🤔 Interested in reading more about the YC S24 batch?\n\nRead our full breakdown from the link in the comments 👇",
"actor\_name": "Crustdata",
"hyperlinks": {
"company\_linkedin\_urls": [],
"person\_linkedin\_urls": [
"https://www.linkedin.com/in/ACoAAAKoldoBqSsiXY\_DHsXdSk1slibabeTvDDY"
],
"other\_urls": []
},
"date\_posted": "2024-09-03",
"total\_reactions": 37,
"total\_comments": 7,
"reactions\_by\_type": {
"LIKE": 28,
"EMPATHY": 4,
"PRAISE": 4,
"INTEREST": 1
},
"num\_shares": 5,
"is\_repost\_without\_thoughts": false,
"reactors": [
{
"name": "Courtney May",
"linkedin\_profile\_url": "https://www.linkedin.com/in/ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
"reaction\_type": "LIKE",
"profile\_image\_url": "https://media.licdn.com/dms/image/v2/D5603AQF-8vL\_c5H9Zg/profile-displayphoto-shrink\_100\_100/profile-displayphoto-shrink\_100\_100/0/1690558480623?e=1730937600&v=beta&t=Lm2hHLTFiEVlHWdTt-Vh3vDYevK8U8SlPqaFdNu3R6A",
"title": "GTM @ Arc (YC W22)",
"additional\_info": "3rd+",
"location": "San Francisco, California, United States",
"linkedin\_profile\_urn": "ACwAACkMyzkBYncrCuM2rzhc06iz6oj741NL-98",
"default\_position\_title": "GTM @ Arc (YC W22)",
"default\_position\_company\_linkedin\_id": "74725230",
"default\_position\_is\_decision\_maker": false,
"flagship\_profile\_url": "https://www.linkedin.com/in/courtney-may-8a178b172",
"profile\_picture\_url": "https://media.licdn.com/dms/image/v2/D5603AQF-8vL\_c5H9Zg/profile-displayphoto-shrink\_400\_400/profile-displayphoto-shrink\_400\_400/0/1690558480623?e=1730937600&v=beta&t=vHg233746zA00m3q2vHKSFcthL3YKiagTtVEZt1qqJI",
"headline": "GTM @ Arc (YC W22)",
"summary": null,
"num\_of\_connections": 786,
"related\_colleague\_company\_id": 74725230,
"skills": [
"Marketing Strategy",
"Product Support",
"SOC 2",
...
],
"employer": [
{
"title": "GTM @ Arc (YC W22)",
"company\_name": "Arc",
"company\_linkedin\_id": "74725230",
"start\_date": "2024-07-01T00:00:00",
"end\_date": null,
"description": null,
"location": "San Francisco, California, United States",
"rich\_media": []
},
{
"title": "Product Marketing & Operations Lead",
"company\_name": "Bits of Stock™",
"company\_linkedin\_id": "10550545",
"start\_date": "2023-03-01T00:00:00",
"end\_date": "2024-07-01T00:00:00",
"description": "● Spearheaded SOC 2 Certification and oversaw compliance organization for internal and external needs.\n● Leads a weekly operations call to manage customer support, new user onboarding, and other outstanding operational matters.\n● Wrote & launched: Product Blog with 6 different featured pieces; 2 Pricing Thought-Leadership pieces; & 2 Partner Press Releases; two of which were featured in the WSJ.\n● Managed marketing and logistics for 11 conferences and events all over the world, producing over 150 B2B qualified leads.\n● Created a company-wide marketing strategy and implemented it across the blog, LinkedIn, & Twitter leading to a 125% increased engagement rate & a 29% increase in followers.\n● Aided in sales and partner relations by preparing a Partner Marketing Guide, creating the user support section of the website and inbound email system, and investing education guide.",
"location": "San Francisco Bay Area",
"rich\_media": []
},
...
],
"education\_background": [
{
"degree\_name": "Bachelor of Applied Science - BASc",
"institute\_name": "Texas Christian University",
"field\_of\_study": "Economics",
"start\_date": "2016-01-01T00:00:00",
"end\_date": "2020-01-01T00:00:00"
}
],
"emails": [
"email@example.com"
],
"websites": [],
"twitter\_handle": null,
"languages": [],
"pronoun": null,
"current\_title": "GTM @ Arc (YC W22)"
}, ...
]
}
]
}
​Each item in the posts array contains the following fields:backend\_urn (string): Unique identifier for the post in LinkedIn's backend system.share\_urn (string): Unique identifier for the shared content.share\_url (string): Direct URL to the post on LinkedIn.text (string): The full content of the post.actor\_name (string): Name of the company or person who created the post.date\_posted (string): Date when the post was published, in "YYYY-MM-DD" format.hyperlinks (object): Contains the external links and Company/Person LinkedIn urls mentioned in the postcompany\_linkedin\_urls (array): List of Company LinkedIn urls mentioned in the postperson\_linkedin\_urls (array): List of Person LinkedIn urls mentioned in the posttotal\_reactions (integer): Total number of reactions on the post.total\_comments (integer): Total number of comments on the post.reactions\_by\_type (object): Breakdown of reactions by type.Possible types include: "LIKE", "EMPATHY", "PRAISE", "INTEREST", etc.Each type is represented by its count (integer).linkedin\_headcount\_and\_glassdoor\_ceo\_approval\_and\_g2num\_shares (integer): Number of times the post has been shared.reactors (array): List of users who reacted to the post. Each reactor object contains:name (string): Full name of the person who reacted.linkedin\_profile\_url (string): URL to the reactor's LinkedIn profile.reaction\_type (string): Type of reaction given (e.g., "LIKE", "EMPATHY").profile\_image\_url (string): URL to the reactor's profile image (100x100 size).title (string): Current professional title of the reactor.additional\_info (string): Additional information, often indicating connection degree.location (string): Geographic location of the reactor.linkedin\_profile\_urn (string): Unique identifier for the reactor's LinkedIn profile.default\_position\_title (string): Primary job title.default\_position\_company\_linkedin\_id (string): LinkedIn ID of the reactor's primary company.default\_position\_is\_decision\_maker (boolean): Indicates if the reactor is in a decision-making role.flagship\_profile\_url (string): Another form of the reactor's LinkedIn profile URL.profile\_picture\_url (string): URL to a larger version of the profile picture (400x400 size).headline (string): Professional headline from the reactor's LinkedIn profile.summary (string or null): Brief professional summary, if available.num\_of\_connections (integer): Number of LinkedIn connections the reactor has.related\_colleague\_company\_id (integer): LinkedIn ID of a related company, possibly current employer.skills (array of strings): List of professional skills listed on the reactor's profile.employer (array of objects): Employment history, each containing:title (string): Job title.company\_name (string): Name of the employer.company\_linkedin\_id (string or null): LinkedIn ID of the company.start\_date (string): Start date of employment in ISO format.end\_date (string or null): End date of employment in ISO format, or null if current.description (string or null): Job description, if available.location (string or null): Job location.rich\_media (array): Currently empty, may contain media related to the job.education\_background (array of objects): Educational history, each containing:degree\_name (string): Type of degree obtained.institute\_name (string): Name of the educational institution.field\_of\_study (string): Area of study.start\_date (string): Start date of education in ISO format.end\_date (string): End date of education in ISO format.emails (array of strings): Known email addresses associated with the reactor.websites (array): Currently empty, may contain personal or professional websites.twitter\_handle (string or null): Twitter username, if available.languages (array): Currently empty, may contain languages spoken.pronoun (string or null): Preferred pronouns, if specified.current\_title (string): Current job title, often identical to default\_position\_title.Key PointsCredits: Without reactors (default): Each successful page request costs 5 creditsWith reactors: Each successful page request costs 25 creditsPagination: Increment the value of page query param to fetch the next set of posts. Most recent posts will be in first page and then so on. Currently, you can only fetch only upto 20 pages of latest posts. In case you want to fetch more, contact Crustdata team at [info@crustdata.com](mailto:info@crustdata.com) .External urls or Company/Person LinkedIn urls mentioned in text:hyperlinks contains list of links (categorized as company\_linkedin\_urls , person\_linkedin\_urls and other\_urls ) mentioned in the postLatency: The data is fetched in real-time from Linkedin and the latency for this endpoint is between 30 to 60 seconds depending on number of reactions for all the posts in the page
### [LinkedIn Posts Keyword Search (real-time)](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#13ce4a7d95b1802fbd92f9e99c4c0530)

## API Usage Endpoints

### Get remaining credits

Request A plain GET request without any query params.Required: authentication token auth\_token for user identification.JSONCopycurl --location 'https://api.crustdata.com/user/credits' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--header 'Content-Type: application/json'
​ResponseReturns the remaining credits for the current billing periodJSONCopy{
"credits": 1000000
}
​