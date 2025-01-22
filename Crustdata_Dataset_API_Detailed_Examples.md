# Crustdata Dataset API Detailed Examples

Crustdata Dataset API Detailed Examples[![](/image/https%3A%2F%2Fbeestat.io%2Fimg%2Fnotion%2Fapi.svg?table=block&id=c66d5236-e8ea-40df-8af1-14f6d447ab48&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)Crustdata Discovery And Enrichment API](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=18)/![](/icons/database_yellow.svg?mode=dark)Crustdata Dataset API Detailed ExamplesMade with![Page icon](/icons/database_yellow.svg?mode=dark)
# Crustdata Dataset API Detailed Examples

Head to [![](/image/https%3A%2F%2Fbeestat.io%2Fimg%2Fnotion%2Fapi.svg?table=block&id=c66d5236-e8ea-40df-8af1-14f6d447ab48&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)Crustdata Discovery And Enrichment API - Company Dataset API](https://crustdata.notion.site/Company-Dataset-API-c66d5236e8ea40df8af114f6d447ab48?pvs=24#a6c3072d9dd2423bb5dda4a37e2666a6) [Dataset API Endpoints](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#2a71be6e962d4d9087ee4392f9fdd231)[1. Job Listings](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#ff964b2e316c49de8770e0bf2cf81f8a)[2. Funding Milestones](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#b64f2bcf91b347d3b577e914bf816222)[3. Decision Makers/People Info](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#fb3bb6ef2444433cb28f67e8f7df2382) [4. LinkedIn Employee Headcount and LinkedIn Follower Count](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#f4590291b0e44b058272695b5ffbbe53)[5. Employee Headcount By Function](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#401279d7dcb54923852587c5c42e9a9c)[6. Glassdoor Profile Metrics](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#54a9cd8958b641f1971ebdef1b0873dd)[7. G2 Profile Metrics](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#aa49c8b2a8ba4a05a49ca380fed4b95b)[8. Web Traffic](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#12de4a7d95b18080a15dc6139ee37b12)[9. Investor Portfolio](/Crustdata-Dataset-API-Detailed-Examples-b83bd0f1ec09452bb0c2cac811bba88c?pvs=25#13de4a7d95b180dba7d2d471933f0cdf)
### Dataset API Endpoints

#### 1. Job Listings

Crustdata’s company\_id is the unique identifier of a company in our database. It is unique and it never changes. It is numeric.Use this request to get job listings that were last updated by the company on 1st Feb, 2024 for all companies with company\_id equal to any one of [680992, 673947, 631280, 636304, 631811]Note:To retrieve all the jobs listings, keep iterating over offset field in the payload. Do not increase limit beyond 100 as the result will be truncated without any ordering.Real-time Fetch (sync\_from\_source): Allows fetching up to 100 jobs in real-time (use background\_task if all the jobs needs to be fetched) Works for 1 company per requestBackground Task (background\_task):Updates job listings for up to 10 companies at a time in the backgroundReturns a task ID in the response. Use this task ID to check the status or results via the endpoint task/result/<task\_id>You need to provide $auth\_token : Your Crustdata API Key/Auth Token. Reach out to support@crustdata.com through your company email if not availableRequest Body Overview The request body is a JSON object that contains the following parameters:
#### Parameters:

| Parameter | Required | Description |
| --- | --- | --- |
| filters | Yes | An object containing the filter conditions. |
| offset | Yes | The starting point of the result set. Default value is 0. |
| limit | Yes | The number of results to return in a single request. Maximum value is 100. Default value is 100. |
| sorts | No | An array of sorting criteria. |
| aggregations | No | [Optional] List of column objects you want to aggregate on with aggregate type |
| functions | No | [Optional] List of functions you want to apply |
| groups | No | [Optional] List of group by you want to apply |
| background\_task | No | [Optional] A boolean flag. If true, triggers a background task to update jobs for up to 10 companies at a time. Returns a task ID that can be used to fetch results later. |
| sync\_from\_source | No | [Optional] A boolean flag. If true, fetches up to 100 jobs in real-time. Requires a filter on company\_id and only allows one company\_id in the filter. |

- `filters` :
  Example: 
  ```JSON
  {
    "op": "and",
    "conditions": [
      {
        "op": "or",
        "conditions": [
          {"largest\_headcount\_country", "type": "(.)", "value": "USA"},
          {"largest\_headcount\_country", "type": "(.)", "value": "IND"}
        ],
      }
      { "column": "title", "type": "in", "value": [ "Sales Development Representative", "SDR", "Business Development Representative", "BDR", "Business Development Manager", "Account Development Representative", "ADR", "Account Development Manager", "Outbound Sales Representative", "Lead Generation Specialist", "Market Development Representative", "MDR", "Inside Sales Representative", "ISR", "Territory Development Representative", "Pipeline Development Representative", "New Business Development Representative", "Customer Acquisition Specialist" ]},
      {"column": "description", "type": "(.)", "value": "Sales Development Representative"}
    ]
  }
  ```

  ​The filters object contains the following parameters:

  | Parameter | Description | Required |
  | --- | --- | --- |
  | op | The operator to apply on the conditions. The value can be "and" or "or". | Yes |
  | conditions | An array of complex filter objects or basic filter objects (see below) | Yes |

- `conditions` parameter: This has two possible types of values
  1. Basic Filter Object: Example: ``` 
    {"column": "crunchbase\_total\_investment\_usd", "type": "=>", "value": "50" } ```The object contains the following parameters
      | Parameter | Description | Required |
      | --- | --- | --- |
      | column | The name of the column to filter. | Yes |
      | type | The filter type. The value can be "=>", "=<", "=", "!=", “in”, “(.)”, “[.]” | Yes |
      | value | The filter value. | Yes |
      | allow\_null | Whether to allow null values. The value can be "true" or "false". Default value is "false". | No |
    - List of all column values:     
      - linkedin\_id
      - company\_website
      - fiscal\_year\_end
      - company\_name
      - markets
      - company\_website\_domain
      - largest\_headcount\_country
      - crunchbase\_total\_investment\_usd
      - acquisition\_status
      - crunchbase\_valuation\_usd
      - crunchbase\_valuation\_lower\_bound\_usd
      - crunchbase\_valuation\_date
      - crunchbase\_profile\_url
      - title
      - category
      - url
      - domain
      - number\_of\_openings
      - description
      - date\_added
      - date\_updated
      - city
      - location\_text
      - workplace\_type
      - reposted\_job
      - dataset\_row\_id
      - pin\_area\_name
      - pincode
      - district
      - district\_geocode
      - wikidata\_id
      - state
      - state\_geo
      - code
      - country
      - country\_code
      - company\_id
    - List of all `type` values:
      | condition type | condition description | applicable column types | example |
      | --- | --- | --- | --- |
      | "=>" | Greater than or equal | number | { "column": "crunchbase\_total\_investment\_usd", "type": "=>", "value": "500000"} |
      | "=<" | Lesser than or equal | number | { "column": "crunchbase\_total\_investment\_usd", "type": "=<", "value": "50"} |
      | "=", | Equal | number | { "column": "crunchbase\_total\_investment\_usd", "type": "=", "value": "50"} |
      | “<” | Lesser than | number | { "column": "crunchbase\_total\_investment\_usd", "type": "<", "value": "50"} |
      | “>” | Greater than | number | { "column": "crunchbase\_total\_investment\_usd", "type": ">", "value": "50"} |
      | “(.)” | Contains, case insensitive | string | { "column": "title", "type": "(.)", "value": "artificial intelligence"} |
      | “[.]” | Contains, case sensitive | string | { "column": "title", "type": "[.]", "value": "Artificial Intelligence"} |
      | "!=" | Not equals | number |  |
      | “in” | Exactly matches atleast one of the elements of list | string, number | { "column": "company\_id", "type": "in", "value": [123, 346. 564]} |

  2. Complex Filter Object: 
    Example: ``` 
    {
      "op": "or",
      "conditions": [
      {"largest\_headcount\_country", "type": "(.)", "value": "USA"},
      {"largest\_headcount\_country", "type": "(.)", "value": "IND"}
      ]
    } 
    ```
​Same schema as the parent [Crustdata Discovery And Enrichment API - filters](https://crustdata.notion.site/filters-c66d5236e8ea40df8af114f6d447ab48?pvs=24#8a72acfe02a5455e895ea9a9dede08c4) parameter 
- Curl ```Bash
curl --request POST \
--url https://api.crustdata.com/data\_lab/job\_listings/Table/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--header 'Origin: https://crustdata.com' \
--header 'User-Agent: Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' \
--data '{
"tickers": [],
"dataset": {
"name": "job\_listings",
"id": "joblisting"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_id", "type": "in", "value": [7576, 680992, 673947, 631280, 636304, 631811]},
{"column": "date\_updated", "type": ">", "value": "2024-02-01"}
]
},
"groups": [],
"aggregations": [],
"functions": [],
"offset": 0,
"limit": 100,
"sorts": []
}'

```
​- Python: 
  ```Python
    import requests
    import json
    url = "https://api.crustdata.com/data\_lab/job\_listings/Table/"
    headers = {
    "Accept": "application/json, text/plain, \*/\*",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "Token $token",
    "Content-Type": "application/json",
    "Origin": "https://crustdata.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    data = {
    "tickers": [],
    "dataset": {
    "name": "job\_listings",
    "id": "joblisting"
    },
    "filters": {
    "op": "and",
    "conditions": [
    {"column": "company\_id", "type": "in", "value": [7576, 680992, 673947, 631280, 636304, 631811]},
    {"column": "date\_updated", "type": ">", "value": "2024-02-01"}
    ]
    },
    "groups": [],
    "aggregations": [],
    "functions": [],
    "offset": 0,
    "limit": 100,
    "sorts": []
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
  ```
​Example requestsGet all job listings that from a list of company domains ANDposted after a specific data ANDhave specific keywords in titleBashCopycurl --location 'https://api.crustdata.com/data\_lab/job\_listings/Table/' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--data '{
"tickers": [],
"dataset": {
"name": "job\_listings",
"id": "joblisting"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_website\_domain", "type": "(.)", "value": "ziphq.com"},
{"column": "date\_updated", "type": ">", "value": "2024-08-01"},
{
"op": "or",
"conditions": [
{"column": "title", "type": "(.)", "value": "Sales Development Representative"},
{"column": "title", "type": "(.)", "value": "SDR"},
{"column": "title", "type": "(.)", "value": "Business Development Representative"}
],
}
]
},
"offset": 0,
"limit": 100,
"sorts": [],
}'
​Get real time job listings from the source for company RipplingBashCopycurl --location 'https://api.crustdata.com/data\_lab/job\_listings/Table/' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--data '{
"tickers": [],
"dataset": {
"name": "job\_listings",
"id": "joblisting"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_id", "type": "in", "value": [634043]}, ]
},
"offset": 0,
"limit": 100,
"sorts": [],
"sync\_from\_source": true
}'
​Fetch job listings for list of company ids from the source in the background Request:BashCopycurl --location 'https://api.crustdata.com/data\_lab/job\_listings/Table/' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--data '{
"tickers": [],
"dataset": {
"name": "job\_listings",
"id": "joblisting"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_id", "type": "in", "value": [631394, 7576, 680992, 673947, 631280, 636304, 631811]},
]
},
"offset": 0,
"limit": 10000,
"sorts": [],
"backgrond\_task": true
}'
​Response would be BashCopy{
"task\_id": "3d729bd0-a113-4b31-b09f-65eff79f06fe",
"task\_type": "job\_listings",
"status": "not\_started",
"completed\_task\_result\_endpoint": "/task/result/3d729bd0-a113-4b31-b09f-65eff79f06fe/",
"created\_at": "2024-12-25T02:32:42.811843Z",
"started\_at": null
}
​Get all job listings that arefrom a list of Crustdata company\_ids ANDposted after a specific data ANDexactly has one of the given titlesBashCopycurl --location 'https://api.crustdata.com/data\_lab/job\_listings/Table/' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--data '{
"tickers": [],
"dataset": {
"name": "job\_listings",
"id": "joblisting"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_id", "type": "in", "value": [631394, 7576, 680992, 673947, 631280, 636304, 631811]},
{"column": "date\_updated", "type": ">", "value": "2024-08-01"},
{
"column": "title",
"type": "in",
"value": [
"Sales Development Representative",
"SDR",
"Business Development Representative",
"BDR",
"Business Development Manager",
"Account Development Representative",
"ADR",
"Account Development Manager",
"Outbound Sales Representative",
"Lead Generation Specialist",
"Market Development Representative",
"MDR",
"Inside Sales Representative",
"ISR",
"Territory Development Representative",
"Pipeline Development Representative",
"New Business Development Representative",
"Customer Acquisition Specialist"
]
}
]
},
"offset": 0,
"count": 100,
"sorts": []
}'
​Get count of job listing meeting a criteriaYou can set "count": 1 . The last value of the first (and the only) row would be the total count of jobs meeting the criteriaBashCopycurl --location 'https://api.crustdata.com/data\_lab/job\_listings/Table/' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--header 'Origin: https://crustdata.com' \
--data '{
"tickers": [],
"dataset": {
"name": "job\_listings",
"id": "joblisting"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_id", "type": "in", "value": [631394]},
{
"column": "title",
"type": "in",
"value": [
"Sales Development Representative",
"SDR",
"Business Development Representative",
"BDR",
"Business Development Manager",
"Account Development Representative",
"ADR",
"Account Development Manager",
"Outbound Sales Representative",
"Lead Generation Specialist",
"Market Development Representative",
"MDR",
"Inside Sales Representative",
"ISR",
"Territory Development Representative",
"Pipeline Development Representative",
"New Business Development Representative",
"Customer Acquisition Specialist"
]
}
]
},
"offset": 0,
"count": 1,
"sorts": []
}'
​Response would be BashCopy{
"fields": [
{
"type": "string",
"api\_name": "linkedin\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"preview\_description": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"preview\_description": "",
"geocode": false
},
...
{
"type": "number",
"api\_name": "total\_rows",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"preview\_description": "",
"geocode": false
}
],
"rows": [
[
"2135371",
"https://stripe.com",
null,
"Stripe",
"stripe",
"PRIVATE",
"stripe.com",
"USA",
9440247725,
null,
50000000000,
10000000000,
"2023-03-15",
"https://crunchbase.com/organization/stripe",
"Sales Development Representative",
"Sales",
"https://www.linkedin.com/jobs/view/3877324263",
"www.linkedin.com",
1,
"Who we are\n\nAbout Stripe\n\nStripe is a financial infrastructure platform for businesses. Millions of companies—from the world’s largest enterprises to the most ambitious startups—use Stripe to accept payments, grow their revenue, and accelerate new business opportunities. Our mission is to increase the GDP of the internet, and we have a staggering amount of work ahead. That means you have an unprecedented opportunity to put the global economy within everyone’s reach while doing the most important work of your career.\n\nAbout The Team\n\nAs a Sales Development Representative (SDR) at Stripe, you will drive Stripe’s future growth engine by working with Demand Gen and the Account Executive team to qualify leads and collaboratively build Stripe’s sales pipeline. You get excited about engaging with prospects to better qualify needs. You are adept at identifying high value opportunities and capable of managing early sales funnel activities.You are used to delivering value in complex situations and are energized by learning about new and existing products. Finally, you enjoy building – you like to actively participate in the development of the demand generation and sales process, the articulation of Stripe’s value proposition, and the creation of key tools and assets. If you’re hungry, smart, persistent, and a great teammate, we want to hear from you!\n\nFor the first months, you’ll be part of the SD Associate program which is designed to accelerate your onboarding and ramp to full productivity as an SDR. This intensive program is built to help you quickly build and develop skills required to be successful in this role. Upon completion, you’ll continue learning and growing in your career as part of Stripe’s Sales Development Academy. These programs are endorsed and supported by sales leaders as an important part of investing in our people.\n\nWe take a data driven, analytical approach to sales development, and are looking for someone who is confident in both prospecting to customers and in helping design our strategy. If you’re hungry, smart, persistent, and a great teammate, we want to hear from you!\n\nWhat you’ll do\n\nResponsibilities\n\nResearch and create outreach materials for high value prospects, in partnership with SDRs and AEsFollow up with Marketing generated leads to qualify as sales opportunities. Move solid leads through the funnel connecting them to a salesperson, and arranging meetingsExecute outbound sales plays created by marketingInitiate contact with potential customers through cold-calling or responding to inquiries generated from MarketingDevelop relationships with prospects to uncover needs through effective questioning to qualify interest and viability to prepare hand-off to salesFollow-up with potential customers who expressed interest but did not initially result in a sales opportunityEffectively work through lead list meeting/exceeding SLAs, consistently update activity and contact information within the CRM system and support weekly reporting effortsCollaborate and provide feedback and insights to Marketing to help improve targeting and messaging\n\n\nWho you are\n\nWe’re looking for someone who meets the minimum requirements to be considered for the role. If you meet these requirements, you are encouraged to apply.\n\nMinimum Requirements\n\nA track record of top performance or prior successSuperior verbal and written communication skillsSelf starter who is able to operate in a hyper growth environmentThis role requires in-office participation three (3) days per week in our Chicago office \n\n\nPreferred Qualifications\n\nProfessional experience\n\n\nHybrid work at Stripe\n\nOffice-assigned Stripes spend at least 50% of the time in a given month in their local office or with users. This hits a balance between bringing people together for in-person collaboration and learning from each other, while supporting flexibility about how to do this in a way that makes sense for individuals and their teams.\n\nPay and benefits\n\nThe annual US base salary range for this role is $65,600 - $98,300. For sales roles, the range provided is the role’s On Target Earnings (\"OTE\") range, meaning that the range includes both the sales commissions/sales bonuses target and annual base salary for the role. This salary range may be inclusive of several career levels at Stripe and will be narrowed during the interview process based on a number of factors, including the candidate’s experience, qualifications, and location. Applicants interested in this role and who are not located in the US may request the annual salary range for their location during the interview process.\n\nAdditional benefits for this role may include: equity, company bonus or sales commissions/bonuses; 401(k) plan; medical, dental, and vision benefits; and wellness stipends.",
"2024-03-29T22:35:22Z",
"2024-12-05T00:00:00Z",
"chicago",
"Chicago, Illinois, United States",
"On-site",
"True",
13385453,
null,
null,
null,
null,
null,
null,
null,
"United States of America (the)",
"USA",
"840",
631394,
3
]
]
}
​And total count of results matching the search query would be: response[rows][0][-1] (-1 refers to last item of the row), which would be 3 in the case aboveResponse[![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/3ZQ16TON5oUV)​[JSON HeroJSON Hero makes reading and understand JSON files easy by giving you a clean and beautiful UI packed with extra features.![](/image/https%3A%2F%2Fjsonhero.io%2Ffavicon.ico?table=block&id=4fada488-a12a-4ab3-bf52-2cdc4efea275&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)https://jsonhero.io/j/gTebm3gqR4em/tree![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://jsonhero.io/j/gTebm3gqR4em/tree)Parsing the responseThe response format is same as that of Company Discovery: Screening API.You refer here on how to parse the response [![](/image/https%3A%2F%2Fbeestat.io%2Fimg%2Fnotion%2Fapi.svg?table=block&id=c66d5236-e8ea-40df-8af1-14f6d447ab48&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)Crustdata Discovery And Enrichment API - Parsing the response](https://crustdata.notion.site/Parsing-the-response-c66d5236e8ea40df8af114f6d447ab48?pvs=24#28de6e16940c4615b5872020a345766a) 
#### 2. Funding Milestones

Use this request to get a time-series of funding milestones with company\_id equal to any one of [637158, 674265, 674657]CurlBashCopycurl --request POST \
--url https://api.crustdata.com/data\_lab/funding\_milestone\_timeseries/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--header 'Content-Type: application/json' \
--header 'Origin: https://crustdata.com' \
--header 'Referer: https://crustdata.com/' \
--data '{"filters":{"op": "or", "conditions": [{"column": "company\_id", "type": "in", "value": [637158,674265,674657]}]},"offset":0,"count":1000,"sorts":[]}'
​PythonPythonCopyimport requests
import json
url = "https://api.crustdata.com/data\_lab/funding\_milestone\_timeseries/"
headers = {
'Accept': 'application/json, text/plain, \*/\*',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': f'Token {auth\_token}', # Ensure the auth\_token variable is defined
'Content-Type': 'application/json',
'Origin': 'https://crustdata.com',
'Referer': 'https://crustdata.com/',
}
data = {
"filters": {
"op": "or",
"conditions": [
{
"column": "company\_id",
"type": "in",
"value": [637158, 674265, 674657]
}
]
},
"offset": 0,
"count": 1000,
"sorts": []
}
response = requests.post(url, headers=headers, data=json.dumps(data))
# Print the response content
print(response.text)
​Response<https://jsonhero.io/j/XDfprlYDbOvf> 
#### 3. Decision Makers/People Info

All decision makers: for a given company\_id=632328Decision makers include the people with following titlesIncluded decision maker titles
#### Founders

CEOFounderCo-founderCo founderCofounderCo-fondateurFondateurCofondateurCofondatriceCo-fondatriceFondatrice
#### Executive Officers

Chief Executive OfficerChief Technical OfficerChief Technology OfficerChief Financial OfficerChief Marketing OfficerChief Sales OfficerChief Marketing and Digital OfficerChief Market Officer
#### Technical Leadership

CTOVP EngineeringVP of EngineeringVice President EngineeringVice President of EngineeringHead EngineeringHead of Engineering
#### Marketing Leadership

CMOChief Marketing OfficerChief Marketing and Digital OfficerChief Market OfficerVP MarketingVP of MarketingVice President MarketingVice President of Marketing
#### Sales Leadership

Chief Sales OfficerVP SalesVP of SalesVice President SalesVice President of SalesVice President (Sales & Pre-Sales)Head SalesHead of Sales
#### Product Leadership

VP ProductVP of ProductVice President ProductVice President of ProductHead of ProductHead Product
#### Software Leadership

VP SoftwareVP of SoftwareVice President SoftwareVice President of Software
#### Financial Leadership

CFOChief Financial OfficerCurlBashCopycurl --request POST \
--url https://api.crustdata.com/data\_lab/decision\_makers/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--header 'Content-Type: application/json' \
--header 'Origin: http://localhost:3000' \
--header 'Referer: http://localhost:3000/' \
--data '{"filters":{"op": "and", "conditions": [{"column": "company\_id", "type": "in", "value": [632328]}] },"offset":0,"count":100,"sorts":[]}'
​PythonPythonCopyimport requests
import json
url = "https://api.crustdata.com/data\_lab/decision\_makers/"
headers = {
'Accept': 'application/json, text/plain, \*/\*',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Token $auth\_token', # Replace with your actual token
'Content-Type': 'application/json',
'Origin': 'http://localhost:3000',
'Referer': 'http://localhost:3000/'
}
data = {
"filters": {
"op": "or",
"conditions": [
{"column": "company\_id", "type": "in", "value": [632328]}
]
},
"offset": 0,
"count": 100,
"sorts": []
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
​Decision makers with specific titles: for a given company\_id=632328For example, get all decision makers “vice president” and “chief” in their titleCurlBashCopycurl --request POST \
--url https://api.crustdata.com/data\_lab/decision\_makers/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--data '{
"filters": {
"op": "or",
"conditions": [
{
"column": "company\_id",
"type": "in",
"value": [632328]
},
{
"column": "title",
"type": "in",
"value": ["vice president", "chief"]
}
]
},
"offset": 0,
"count": 100,
"sorts": []
}'
​PythonPythonCopyimport requests
url = "https://api.crustdata.com/data\_lab/decision\_makers/"
headers = {
"Accept": "application/json, text/plain, \*/\*",
"Accept-Language": "en-US,en;q=0.9",
"Authorization": "Token YOUR\_AUTH\_TOKEN"
}
payload = {
"filters": {
"op": "or",
"conditions": [
{
"column": "company\_id",
"type": "in",
"value": [632328]
},
{
"column": "title",
"type": "in",
"value": ["vice president", "chief"]
}
]
},
"offset": 0,
"count": 100,
"sorts": []
}
response = requests.post(url, headers=headers, json=payload)
# Print the response status and data
print(f"Status Code: {response.status\_code}")
print(f"Response: {response.json()}")
​People profiles by their LinkedIn’s “flagship\_url”For example, decision makers with LinkedIn profile url as "https://www.linkedin.com/in/alikashani"CurlBashCopycurl --request POST \
--url https://api.crustdata.com/data\_lab/decision\_makers/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--header 'Content-Type: application/json' \
--data '{"filters":{"op": "and", "conditions": [{"column": "linkedin\_flagship\_profile\_url", "type": "in", "value": ["https://www.linkedin.com/in/alikashani"]}] },"offset":0,"count":100,"sorts":[]}'
​PythonPythonCopyimport requests
import json
url = "https://api.crustdata.com/data\_lab/decision\_makers/"
headers = {
'Accept': 'application/json, text/plain, \*/\*',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Token $auth\_token', # Replace with your actual token
'Content-Type': 'application/json',
'Origin': 'http://localhost:3000',
'Referer': 'http://localhost:3000/'
}
data = {
"filters": {
"op": "or",
"conditions": [
{"column": "linkedin\_flagship\_profile\_url", "type": "in", "value": ["https://www.linkedin.com/in/alikashani"]}
]
},
"offset": 0,
"count": 100,
"sorts": []
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
​People profiles by their “linkedin\_urn”For example, decision makers with linkedin\_urn as "ACwAAAVhcDEBbTdJtuc-KHsdYfPU1JAdBmHkh8I" . linkedin\_urn is a 30-40 character alphanumeric sequence that includes both uppercase letters and numbersCurlBashCopycurl --request POST \
--url https://api.crustdata.com/data\_lab/decision\_makers/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token' \
--header 'Content-Type: application/json' \
--header 'Origin: http://localhost:3000' \
--header 'Referer: http://localhost:3000/' \
--data '{"filters":{"op": "or", "conditions": [{"column": "linkedin\_profile\_urn", "type": "in", "value": ["ACwAAAVhcDEBbTdJtuc-KHsdYfPU1JAdBmHkh8I"]}] },"offset":0,"count":100,"sorts":[]}'
​PythonPythonCopyimport requests
import json
url = "https://api.crustdata.com/data\_lab/decision\_makers/"
headers = {
'Accept': 'application/json, text/plain, \*/\*',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Token $auth\_token', # Replace with your actual token
'Content-Type': 'application/json',
'Origin': 'http://localhost:3000',
'Referer': 'http://localhost:3000/'
}
data = {
"filters": {
"op": "or",
"conditions": [
{"column": "linkedin\_profile\_urn", "type": "in", "value": ["ACwAAAVhcDEBbTdJtuc-KHsdYfPU1JAdBmHkh8I"]}
]
},
"offset": 0,
"count": 100,
"sorts": []
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
​Response[![](https://jsonhero.io/favicon.ico)json\_heroJSON Hero](https://jsonhero.io/j/QSAlhbuflhie)​
#### 4. LinkedIn Employee Headcount and LinkedIn Follower Count

Use this request to get weekly and monthly timeseries of employee headcount as a JSON blob.You either provide with list a list of Crustdata company\_id or linkedin\_id or company\_website\_domainIn the following example, we request the employee headcount timeseries of companies with company\_id equal to any one of [680992, 673947, 631280, 636304, 631811]CUrlBashCopycurl 'https://api.crustdata.com/data\_lab/headcount\_timeseries/' \
-H 'Accept: application/json, text/plain, \*/\*' \
-H 'Accept-Language: en-US,en;q=0.9' \
-H 'Authorization: Token $auth\_token' \
-H 'Content-Type: application/json' \
-H 'Origin: https://crustdata.com' \
-H 'Referer: https://crustdata.com' \
--data-raw '{
"filters": {
"op": "or",
"conditions": [
{
"column": "company\_id",
"type": "=",
"value": 634995
},
{
"column": "company\_id",
"type": "=",
"value": 680992
},
{
"column": "company\_id",
"type": "=",
"value": 673947
},
{
"column": "company\_id",
"type": "=",
"value": 631811
}
]
},
"offset": 0,
"count": 100,
"sorts": []
}' \
--compressed
​PythonPythonCopyimport requests
headers = {
'Accept': 'application/json, text/plain, \*/\*',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Token $auth\_token',
'Content-Type': 'application/json',
'Origin': 'https://crustdata.com',
'Referer': 'https://crustdata.com',
}
json\_data = {
'filters': {
'op': 'and',
'conditions': [
{
'op': 'or',
'conditions': [
{
'column': 'company\_id',
'type': '=',
'value': 634995,
},
{
'column': 'company\_id',
'type': '=',
'value': 680992,
},
{
'column': 'company\_id',
'type': '=',
'value': 673947,
},
{
'column': 'company\_id',
'type': '=',
'value': 631811,
},
],
},
],
},
'offset': 0,
'count': 100,
'sorts': [],
}
response = requests.post('https://api.crustdata.com/data\_lab/headcount\_timeseries/', headers=headers, json=json\_data)
​Response[JSON HeroJSON Hero makes reading and understand JSON files easy by giving you a clean and beautiful UI packed with extra features.![](/image/https%3A%2F%2Fjsonhero.io%2Ffavicon.ico?table=block&id=48efd1ed-ef16-4c44-ab57-d2d1de8fc648&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)https://jsonhero.io/j/bd2OKMSu8ZQ0/editor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://jsonhero.io/j/bd2OKMSu8ZQ0/editor)JSONCopy{
"fields": [
{
"type": "foreign\_key",
"api\_name": "company\_id",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "linkedin\_id",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website\_domain",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "array",
"api\_name": "headcount\_timeseries",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "total\_rows",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
}
],
"rows": [
[
631280,
"https://www.lacework.com",
"17932068",
"lacework.com",
[
{
"date": "2021-08-01T00:00:00+00:00",
"employee\_count": 643,
"follower\_count": null
},
{
"date": "2021-08-02T00:00:00+00:00",
"employee\_count": 643,
"follower\_count": null
},
{
"date": "2021-08-09T00:00:00+00:00",
"employee\_count": 643,
"follower\_count": null
},
{
"date": "2021-08-16T00:00:00+00:00",
"employee\_count": 643,
"follower\_count": null
},
{
"date": "2021-08-23T00:00:00+00:00",
"employee\_count": 643,
"follower\_count": null
},
{
"date": "2021-08-30T00:00:00+00:00",
"employee\_count": 643,
"follower\_count": null
},
{
"date": "2021-09-01T00:00:00+00:00",
"employee\_count": 687,
"follower\_count": null
},
{
"date": "2021-09-06T00:00:00+00:00",
"employee\_count": 687,
"follower\_count": null
},
{
"date": "2021-09-13T00:00:00+00:00",
"employee\_count": 687,
"follower\_count": null
},
{
"date": "2021-09-20T00:00:00+00:00",
"employee\_count": 687,
"follower\_count": null
},
{
"date": "2021-09-27T00:00:00+00:00",
"employee\_count": 687,
"follower\_count": null
},
{
"date": "2021-10-01T00:00:00+00:00",
"employee\_count": 737,
"follower\_count": null
},
{
"date": "2021-10-04T00:00:00+00:00",
"employee\_count": 737,
"follower\_count": null
},
{
"date": "2021-10-11T00:00:00+00:00",
"employee\_count": 737,
"follower\_count": null
},
{
"date": "2021-10-18T00:00:00+00:00",
"employee\_count": 737,
"follower\_count": null
},
{
"date": "2021-10-25T00:00:00+00:00",
"employee\_count": 737,
"follower\_count": null
},
{
"date": "2021-11-01T00:00:00+00:00",
"employee\_count": 805,
"follower\_count": null
},
{
"date": "2021-11-08T00:00:00+00:00",
"employee\_count": 805,
"follower\_count": null
},
{
"date": "2021-11-15T00:00:00+00:00",
"employee\_count": 805,
"follower\_count": null
},
{
"date": "2021-11-22T00:00:00+00:00",
"employee\_count": 805,
"follower\_count": null
},
{
"date": "2021-11-29T00:00:00+00:00",
"employee\_count": 805,
"follower\_count": null
},
{
"date": "2021-12-01T00:00:00+00:00",
"employee\_count": 853,
"follower\_count": null
},
{
"date": "2021-12-06T00:00:00+00:00",
"employee\_count": 853,
"follower\_count": null
},
{
"date": "2021-12-13T00:00:00+00:00",
"employee\_count": 853,
"follower\_count": null
},
{
"date": "2021-12-20T00:00:00+00:00",
"employee\_count": 853,
"follower\_count": null
},
{
"date": "2021-12-27T00:00:00+00:00",
"employee\_count": 853,
"follower\_count": null
},
{
"date": "2022-01-01T00:00:00+00:00",
"employee\_count": 919,
"follower\_count": null
},
{
"date": "2022-01-03T00:00:00+00:00",
"employee\_count": 919,
"follower\_count": null
},
{
"date": "2022-01-10T00:00:00+00:00",
"employee\_count": 919,
"follower\_count": null
},
{
"date": "2022-01-17T00:00:00+00:00",
"employee\_count": 919,
"follower\_count": null
},
{
"date": "2022-01-24T00:00:00+00:00",
"employee\_count": 919,
"follower\_count": null
},
{
"date": "2022-01-31T00:00:00+00:00",
"employee\_count": 919,
"follower\_count": null
},
{
"date": "2022-02-01T00:00:00+00:00",
"employee\_count": 996,
"follower\_count": null
},
{
"date": "2022-02-07T00:00:00+00:00",
"employee\_count": 996,
"follower\_count": null
},
{
"date": "2022-02-14T00:00:00+00:00",
"employee\_count": 996,
"follower\_count": null
},
{
"date": "2022-02-21T00:00:00+00:00",
"employee\_count": 996,
"follower\_count": null
},
{
"date": "2022-02-28T00:00:00+00:00",
"employee\_count": 996,
"follower\_count": null
},
{
"date": "2022-03-01T00:00:00+00:00",
"employee\_count": 1069,
"follower\_count": null
},
{
"date": "2022-03-07T00:00:00+00:00",
"employee\_count": 1069,
"follower\_count": null
},
{
"date": "2022-03-14T00:00:00+00:00",
"employee\_count": 1069,
"follower\_count": null
},
{
"date": "2022-03-21T00:00:00+00:00",
"employee\_count": 1069,
"follower\_count": null
},
{
"date": "2022-03-28T00:00:00+00:00",
"employee\_count": 1069,
"follower\_count": null
},
{
"date": "2022-04-01T00:00:00+00:00",
"employee\_count": 1121,
"follower\_count": null
},
{
"date": "2022-04-04T00:00:00+00:00",
"employee\_count": 1121,
"follower\_count": null
},
{
"date": "2022-04-11T00:00:00+00:00",
"employee\_count": 1121,
"follower\_count": null
},
{
"date": "2022-04-18T00:00:00+00:00",
"employee\_count": 1121,
"follower\_count": null
},
{
"date": "2022-04-25T00:00:00+00:00",
"employee\_count": 1121,
"follower\_count": null
},
{
"date": "2022-05-01T00:00:00+00:00",
"employee\_count": 1160,
"follower\_count": null
},
{
"date": "2022-05-02T00:00:00+00:00",
"employee\_count": 1160,
"follower\_count": null
},
{
"date": "2022-05-09T00:00:00+00:00",
"employee\_count": 1160,
"follower\_count": null
},
{
"date": "2022-05-16T00:00:00+00:00",
"employee\_count": 1160,
"follower\_count": null
},
{
"date": "2022-05-23T00:00:00+00:00",
"employee\_count": 1160,
"follower\_count": null
},
{
"date": "2022-05-30T00:00:00+00:00",
"employee\_count": 1160,
"follower\_count": null
},
{
"date": "2022-06-01T00:00:00+00:00",
"employee\_count": 1085,
"follower\_count": null
},
{
"date": "2022-06-06T00:00:00+00:00",
"employee\_count": 1085,
"follower\_count": null
},
{
"date": "2022-06-13T00:00:00+00:00",
"employee\_count": 1085,
"follower\_count": null
},
{
"date": "2022-06-20T00:00:00+00:00",
"employee\_count": 1085,
"follower\_count": null
},
{
"date": "2022-06-27T00:00:00+00:00",
"employee\_count": 1085,
"follower\_count": null
},
{
"date": "2022-07-01T00:00:00+00:00",
"employee\_count": 1053,
"follower\_count": null
},
{
"date": "2022-07-04T00:00:00+00:00",
"employee\_count": 1053,
"follower\_count": null
},
{
"date": "2022-07-11T00:00:00+00:00",
"employee\_count": 1053,
"follower\_count": null
},
{
"date": "2022-07-18T00:00:00+00:00",
"employee\_count": 1053,
"follower\_count": null
},
{
"date": "2022-07-25T00:00:00+00:00",
"employee\_count": 1053,
"follower\_count": null
},
{
"date": "2022-08-01T00:00:00+00:00",
"employee\_count": 1008,
"follower\_count": null
},
{
"date": "2022-08-08T00:00:00+00:00",
"employee\_count": 1008,
"follower\_count": null
},
{
"date": "2022-08-15T00:00:00+00:00",
"employee\_count": 1008,
"follower\_count": null
},
{
"date": "2022-08-22T00:00:00+00:00",
"employee\_count": 1008,
"follower\_count": null
},
{
"date": "2022-08-29T00:00:00+00:00",
"employee\_count": 1008,
"follower\_count": null
},
{
"date": "2022-09-01T00:00:00+00:00",
"employee\_count": 994,
"follower\_count": null
},
{
"date": "2022-09-05T00:00:00+00:00",
"employee\_count": 994,
"follower\_count": null
},
{
"date": "2022-09-12T00:00:00+00:00",
"employee\_count": 994,
"follower\_count": null
},
{
"date": "2022-09-19T00:00:00+00:00",
"employee\_count": 994,
"follower\_count": null
},
{
"date": "2022-09-26T00:00:00+00:00",
"employee\_count": 994,
"follower\_count": null
},
{
"date": "2022-10-01T00:00:00+00:00",
"employee\_count": 993,
"follower\_count": null
},
{
"date": "2022-10-03T00:00:00+00:00",
"employee\_count": 993,
"follower\_count": null
},
{
"date": "2022-10-10T00:00:00+00:00",
"employee\_count": 993,
"follower\_count": null
},
{
"date": "2022-10-17T00:00:00+00:00",
"employee\_count": 993,
"follower\_count": null
},
{
"date": "2022-10-24T00:00:00+00:00",
"employee\_count": 993,
"follower\_count": null
},
{
"date": "2022-10-31T00:00:00+00:00",
"employee\_count": 993,
"follower\_count": null
},
{
"date": "2022-11-01T00:00:00+00:00",
"employee\_count": 977,
"follower\_count": null
},
{
"date": "2022-11-07T00:00:00+00:00",
"employee\_count": 977,
"follower\_count": null
},
{
"date": "2022-11-14T00:00:00+00:00",
"employee\_count": 977,
"follower\_count": null
},
{
"date": "2022-11-21T00:00:00+00:00",
"employee\_count": 977,
"follower\_count": null
},
{
"date": "2022-11-28T00:00:00+00:00",
"employee\_count": 977,
"follower\_count": null
},
{
"date": "2022-12-01T00:00:00+00:00",
"employee\_count": 968,
"follower\_count": null
},
{
"date": "2022-12-05T00:00:00+00:00",
"employee\_count": 968,
"follower\_count": null
},
{
"date": "2022-12-12T00:00:00+00:00",
"employee\_count": 968,
"follower\_count": null
},
{
"date": "2022-12-19T00:00:00+00:00",
"employee\_count": 968,
"follower\_count": null
},
{
"date": "2022-12-26T00:00:00+00:00",
"employee\_count": 968,
"follower\_count": null
},
{
"date": "2023-01-01T00:00:00+00:00",
"employee\_count": 975,
"follower\_count": null
},
{
"date": "2023-01-02T00:00:00+00:00",
"employee\_count": 975,
"follower\_count": null
},
{
"date": "2023-01-09T00:00:00+00:00",
"employee\_count": 975,
"follower\_count": null
},
{
"date": "2023-01-16T00:00:00+00:00",
"employee\_count": 975,
"follower\_count": null
},
{
"date": "2023-01-23T00:00:00+00:00",
"employee\_count": 975,
"follower\_count": null
},
{
"date": "2023-01-30T00:00:00+00:00",
"employee\_count": 975,
"follower\_count": null
},
{
"date": "2023-02-01T00:00:00+00:00",
"employee\_count": 979,
"follower\_count": null
},
{
"date": "2023-02-06T00:00:00+00:00",
"employee\_count": 979,
"follower\_count": null
},
{
"date": "2023-02-13T00:00:00+00:00",
"employee\_count": 979,
"follower\_count": null
},
{
"date": "2023-02-20T00:00:00+00:00",
"employee\_count": 979,
"follower\_count": null
},
{
"date": "2023-02-27T00:00:00+00:00",
"employee\_count": 979,
"follower\_count": null
},
{
"date": "2023-03-01T00:00:00+00:00",
"employee\_count": 987,
"follower\_count": null
},
{
"date": "2023-03-06T00:00:00+00:00",
"employee\_count": 987,
"follower\_count": null
},
{
"date": "2023-03-13T00:00:00+00:00",
"employee\_count": 987,
"follower\_count": null
},
{
"date": "2023-03-20T00:00:00+00:00",
"employee\_count": 987,
"follower\_count": null
},
{
"date": "2023-03-27T00:00:00+00:00",
"employee\_count": 987,
"follower\_count": null
},
{
"date": "2023-04-01T00:00:00+00:00",
"employee\_count": 988,
"follower\_count": null
},
{
"date": "2023-04-03T00:00:00+00:00",
"employee\_count": 988,
"follower\_count": null
},
{
"date": "2023-04-10T00:00:00+00:00",
"employee\_count": 988,
"follower\_count": null
},
{
"date": "2023-04-17T00:00:00+00:00",
"employee\_count": 988,
"follower\_count": null
},
{
"date": "2023-04-24T00:00:00+00:00",
"employee\_count": 988,
"follower\_count": null
},
{
"date": "2023-05-01T00:00:00+00:00",
"employee\_count": 1027,
"follower\_count": null
},
{
"date": "2023-05-08T00:00:00+00:00",
"employee\_count": 1027,
"follower\_count": null
},
{
"date": "2023-05-15T00:00:00+00:00",
"employee\_count": 1027,
"follower\_count": null
},
{
"date": "2023-05-22T00:00:00+00:00",
"employee\_count": 1027,
"follower\_count": null
},
{
"date": "2023-05-29T00:00:00+00:00",
"employee\_count": 1027,
"follower\_count": null
},
{
"date": "2023-06-01T00:00:00+00:00",
"employee\_count": 1009,
"follower\_count": null
},
{
"date": "2023-06-05T00:00:00+00:00",
"employee\_count": 1009,
"follower\_count": null
},
{
"date": "2023-06-12T00:00:00+00:00",
"employee\_count": 1009,
"follower\_count": null
},
{
"date": "2023-06-19T00:00:00+00:00",
"employee\_count": 1009,
"follower\_count": null
},
{
"date": "2023-06-26T00:00:00+00:00",
"employee\_count": 1009,
"follower\_count": null
},
{
"date": "2023-07-01T00:00:00+00:00",
"employee\_count": 989,
"follower\_count": null
},
{
"date": "2023-07-03T00:00:00+00:00",
"employee\_count": 989,
"follower\_count": null
},
{
"date": "2023-07-10T00:00:00+00:00",
"employee\_count": 1009,
"follower\_count": 37367
},
{
"date": "2023-07-17T00:00:00+00:00",
"employee\_count": 1005,
"follower\_count": null
},
{
"date": "2023-07-24T00:00:00+00:00",
"employee\_count": 1005,
"follower\_count": 37680
},
{
"date": "2023-07-31T00:00:00+00:00",
"employee\_count": 1005,
"follower\_count": 37680
},
{
"date": "2023-08-01T00:00:00+00:00",
"employee\_count": 994,
"follower\_count": 38148
},
{
"date": "2023-08-07T00:00:00+00:00",
"employee\_count": 983,
"follower\_count": 38303
},
{
"date": "2023-08-14T00:00:00+00:00",
"employee\_count": 973,
"follower\_count": 38583
},
{
"date": "2023-08-21T00:00:00+00:00",
"employee\_count": 966,
"follower\_count": 38780
},
{
"date": "2023-08-28T00:00:00+00:00",
"employee\_count": 956,
"follower\_count": 39043
},
{
"date": "2023-09-01T00:00:00+00:00",
"employee\_count": 955,
"follower\_count": 39072
},
{
"date": "2023-09-04T00:00:00+00:00",
"employee\_count": 955,
"follower\_count": 39072
},
{
"date": "2023-09-11T00:00:00+00:00",
"employee\_count": 946,
"follower\_count": 39307
},
{
"date": "2023-09-18T00:00:00+00:00",
"employee\_count": 939,
"follower\_count": 39543
},
{
"date": "2023-09-25T00:00:00+00:00",
"employee\_count": 939,
"follower\_count": 39543
},
{
"date": "2023-10-01T00:00:00+00:00",
"employee\_count": 905,
"follower\_count": 40190
},
{
"date": "2023-10-02T00:00:00+00:00",
"employee\_count": 905,
"follower\_count": 40190
},
{
"date": "2023-10-09T00:00:00+00:00",
"employee\_count": 905,
"follower\_count": 40385
},
{
"date": "2023-10-16T00:00:00+00:00",
"employee\_count": 894,
"follower\_count": 40732
},
{
"date": "2023-10-23T00:00:00+00:00",
"employee\_count": 878,
"follower\_count": 41285
},
{
"date": "2023-10-30T00:00:00+00:00",
"employee\_count": 878,
"follower\_count": 41507
},
{
"date": "2023-11-01T00:00:00+00:00",
"employee\_count": 878,
"follower\_count": 41616
},
{
"date": "2023-11-06T00:00:00+00:00",
"employee\_count": 863,
"follower\_count": 41025
},
{
"date": "2023-11-13T00:00:00+00:00",
"employee\_count": 854,
"follower\_count": 41048
},
{
"date": "2023-11-20T00:00:00+00:00",
"employee\_count": 845,
"follower\_count": 41259
},
{
"date": "2023-11-27T00:00:00+00:00",
"employee\_count": 843,
"follower\_count": 43498
},
{
"date": "2023-12-01T00:00:00+00:00",
"employee\_count": 843,
"follower\_count": 43498
},
{
"date": "2023-12-04T00:00:00+00:00",
"employee\_count": 832,
"follower\_count": 43685
},
{
"date": "2023-12-11T00:00:00+00:00",
"employee\_count": 829,
"follower\_count": 43805
},
{
"date": "2023-12-18T00:00:00+00:00",
"employee\_count": 826,
"follower\_count": 44118
},
{
"date": "2023-12-25T00:00:00+00:00",
"employee\_count": 826,
"follower\_count": 46066
},
{
"date": "2024-01-01T00:00:00+00:00",
"employee\_count": 823,
"follower\_count": 47044
},
{
"date": "2024-01-08T00:00:00+00:00",
"employee\_count": 818,
"follower\_count": 47582
},
{
"date": "2024-01-15T00:00:00+00:00",
"employee\_count": 811,
"follower\_count": 47646
},
{
"date": "2024-01-22T00:00:00+00:00",
"employee\_count": 808,
"follower\_count": 47917
},
{
"date": "2024-01-29T00:00:00+00:00",
"employee\_count": 804,
"follower\_count": 48116
},
{
"date": "2024-02-01T00:00:00+00:00",
"employee\_count": 799,
"follower\_count": 49145
},
{
"date": "2024-02-05T00:00:00+00:00",
"employee\_count": 799,
"follower\_count": 49145
},
{
"date": "2024-02-12T00:00:00+00:00",
"employee\_count": 791,
"follower\_count": 50425
},
{
"date": "2024-02-19T00:00:00+00:00",
"employee\_count": 778,
"follower\_count": 50568
},
{
"date": "2024-02-26T00:00:00+00:00",
"employee\_count": 770,
"follower\_count": 50849
},
{
"date": "2024-03-01T00:00:00+00:00",
"employee\_count": 769,
"follower\_count": 50972
}
],
5
],
[
631811,
"http://jumpcloud.com",
"3033823",
"jumpcloud.com",
[
{
"date": "2021-08-01T00:00:00+00:00",
"employee\_count": 390,
"follower\_count": null
},
{
"date": "2021-08-02T00:00:00+00:00",
"employee\_count": 390,
"follower\_count": null
},
{
"date": "2021-08-09T00:00:00+00:00",
"employee\_count": 390,
"follower\_count": null
},
{
"date": "2021-08-16T00:00:00+00:00",
"employee\_count": 390,
"follower\_count": null
},
{
"date": "2021-08-23T00:00:00+00:00",
"employee\_count": 390,
"follower\_count": null
},
{
"date": "2021-08-30T00:00:00+00:00",
"employee\_count": 390,
"follower\_count": null
},
{
"date": "2021-09-01T00:00:00+00:00",
"employee\_count": 409,
"follower\_count": null
},
{
"date": "2021-09-06T00:00:00+00:00",
"employee\_count": 409,
"follower\_count": null
},
{
"date": "2021-09-13T00:00:00+00:00",
"employee\_count": 409,
"follower\_count": null
},
{
"date": "2021-09-20T00:00:00+00:00",
"employee\_count": 409,
"follower\_count": null
},
{
"date": "2021-09-27T00:00:00+00:00",
"employee\_count": 409,
"follower\_count": null
},
{
"date": "2021-10-01T00:00:00+00:00",
"employee\_count": 420,
"follower\_count": null
},
{
"date": "2021-10-04T00:00:00+00:00",
"employee\_count": 420,
"follower\_count": null
},
{
"date": "2021-10-11T00:00:00+00:00",
"employee\_count": 420,
"follower\_count": null
},
{
"date": "2021-10-18T00:00:00+00:00",
"employee\_count": 420,
"follower\_count": null
},
{
"date": "2021-10-25T00:00:00+00:00",
"employee\_count": 420,
"follower\_count": null
},
{
"date": "2021-11-01T00:00:00+00:00",
"employee\_count": 477,
"follower\_count": null
},
{
"date": "2021-11-08T00:00:00+00:00",
"employee\_count": 477,
"follower\_count": null
},
{
"date": "2021-11-15T00:00:00+00:00",
"employee\_count": 477,
"follower\_count": null
},
{
"date": "2021-11-22T00:00:00+00:00",
"employee\_count": 477,
"follower\_count": null
},
{
"date": "2021-11-29T00:00:00+00:00",
"employee\_count": 477,
"follower\_count": null
},
{
"date": "2021-12-01T00:00:00+00:00",
"employee\_count": 487,
"follower\_count": null
},
{
"date": "2021-12-06T00:00:00+00:00",
"employee\_count": 487,
"follower\_count": null
},
{
"date": "2021-12-13T00:00:00+00:00",
"employee\_count": 487,
"follower\_count": null
},
{
"date": "2021-12-20T00:00:00+00:00",
"employee\_count": 487,
"follower\_count": null
},
{
"date": "2021-12-27T00:00:00+00:00",
"employee\_count": 487,
"follower\_count": null
},
{
"date": "2022-01-01T00:00:00+00:00",
"employee\_count": 538,
"follower\_count": null
},
{
"date": "2022-01-03T00:00:00+00:00",
"employee\_count": 538,
"follower\_count": null
},
{
"date": "2022-01-10T00:00:00+00:00",
"employee\_count": 538,
"follower\_count": null
},
{
"date": "2022-01-17T00:00:00+00:00",
"employee\_count": 538,
"follower\_count": null
},
{
"date": "2022-01-24T00:00:00+00:00",
"employee\_count": 538,
"follower\_count": null
},
{
"date": "2022-01-31T00:00:00+00:00",
"employee\_count": 538,
"follower\_count": null
},
{
"date": "2022-02-01T00:00:00+00:00",
"employee\_count": 569,
"follower\_count": null
},
{
"date": "2022-02-07T00:00:00+00:00",
"employee\_count": 569,
"follower\_count": null
},
{
"date": "2022-02-14T00:00:00+00:00",
"employee\_count": 569,
"follower\_count": null
},
{
"date": "2022-02-21T00:00:00+00:00",
"employee\_count": 569,
"follower\_count": null
},
{
"date": "2022-02-28T00:00:00+00:00",
"employee\_count": 569,
"follower\_count": null
},
{
"date": "2022-03-01T00:00:00+00:00",
"employee\_count": 600,
"follower\_count": null
},
{
"date": "2022-03-07T00:00:00+00:00",
"employee\_count": 600,
"follower\_count": null
},
{
"date": "2022-03-14T00:00:00+00:00",
"employee\_count": 600,
"follower\_count": null
},
{
"date": "2022-03-21T00:00:00+00:00",
"employee\_count": 600,
"follower\_count": null
},
{
"date": "2022-03-28T00:00:00+00:00",
"employee\_count": 600,
"follower\_count": null
},
{
"date": "2022-04-01T00:00:00+00:00",
"employee\_count": 614,
"follower\_count": null
},
{
"date": "2022-04-04T00:00:00+00:00",
"employee\_count": 614,
"follower\_count": null
},
{
"date": "2022-04-11T00:00:00+00:00",
"employee\_count": 614,
"follower\_count": null
},
{
"date": "2022-04-18T00:00:00+00:00",
"employee\_count": 614,
"follower\_count": null
},
{
"date": "2022-04-25T00:00:00+00:00",
"employee\_count": 614,
"follower\_count": null
},
{
"date": "2022-05-01T00:00:00+00:00",
"employee\_count": 631,
"follower\_count": null
},
{
"date": "2022-05-02T00:00:00+00:00",
"employee\_count": 631,
"follower\_count": null
},
{
"date": "2022-05-09T00:00:00+00:00",
"employee\_count": 631,
"follower\_count": null
},
{
"date": "2022-05-16T00:00:00+00:00",
"employee\_count": 631,
"follower\_count": null
},
{
"date": "2022-05-23T00:00:00+00:00",
"employee\_count": 631,
"follower\_count": null
},
{
"date": "2022-05-30T00:00:00+00:00",
"employee\_count": 631,
"follower\_count": null
},
{
"date": "2022-06-01T00:00:00+00:00",
"employee\_count": 641,
"follower\_count": null
},
{
"date": "2022-06-06T00:00:00+00:00",
"employee\_count": 641,
"follower\_count": null
},
{
"date": "2022-06-13T00:00:00+00:00",
"employee\_count": 641,
"follower\_count": null
},
{
"date": "2022-06-20T00:00:00+00:00",
"employee\_count": 641,
"follower\_count": null
},
{
"date": "2022-06-27T00:00:00+00:00",
"employee\_count": 641,
"follower\_count": null
},
{
"date": "2022-07-01T00:00:00+00:00",
"employee\_count": 659,
"follower\_count": null
},
{
"date": "2022-07-04T00:00:00+00:00",
"employee\_count": 659,
"follower\_count": null
},
{
"date": "2022-07-11T00:00:00+00:00",
"employee\_count": 659,
"follower\_count": null
},
{
"date": "2022-07-18T00:00:00+00:00",
"employee\_count": 659,
"follower\_count": null
},
{
"date": "2022-07-25T00:00:00+00:00",
"employee\_count": 659,
"follower\_count": null
},
{
"date": "2022-08-01T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2022-08-08T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2022-08-15T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2022-08-22T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2022-08-29T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2022-09-01T00:00:00+00:00",
"employee\_count": 654,
"follower\_count": null
},
{
"date": "2022-09-05T00:00:00+00:00",
"employee\_count": 654,
"follower\_count": null
},
{
"date": "2022-09-12T00:00:00+00:00",
"employee\_count": 654,
"follower\_count": null
},
{
"date": "2022-09-19T00:00:00+00:00",
"employee\_count": 654,
"follower\_count": null
},
{
"date": "2022-09-26T00:00:00+00:00",
"employee\_count": 654,
"follower\_count": null
},
{
"date": "2022-10-01T00:00:00+00:00",
"employee\_count": 657,
"follower\_count": null
},
{
"date": "2022-10-03T00:00:00+00:00",
"employee\_count": 657,
"follower\_count": null
},
{
"date": "2022-10-10T00:00:00+00:00",
"employee\_count": 657,
"follower\_count": null
},
{
"date": "2022-10-17T00:00:00+00:00",
"employee\_count": 657,
"follower\_count": null
},
{
"date": "2022-10-24T00:00:00+00:00",
"employee\_count": 657,
"follower\_count": null
},
{
"date": "2022-10-31T00:00:00+00:00",
"employee\_count": 657,
"follower\_count": null
},
{
"date": "2022-11-01T00:00:00+00:00",
"employee\_count": 669,
"follower\_count": null
},
{
"date": "2022-11-07T00:00:00+00:00",
"employee\_count": 669,
"follower\_count": null
},
{
"date": "2022-11-14T00:00:00+00:00",
"employee\_count": 669,
"follower\_count": null
},
{
"date": "2022-11-21T00:00:00+00:00",
"employee\_count": 669,
"follower\_count": null
},
{
"date": "2022-11-28T00:00:00+00:00",
"employee\_count": 669,
"follower\_count": null
},
{
"date": "2022-12-01T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": null
},
{
"date": "2022-12-05T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": null
},
{
"date": "2022-12-12T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": null
},
{
"date": "2022-12-19T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": null
},
{
"date": "2022-12-26T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": null
},
{
"date": "2023-01-01T00:00:00+00:00",
"employee\_count": 620,
"follower\_count": null
},
{
"date": "2023-01-02T00:00:00+00:00",
"employee\_count": 620,
"follower\_count": null
},
{
"date": "2023-01-09T00:00:00+00:00",
"employee\_count": 620,
"follower\_count": null
},
{
"date": "2023-01-16T00:00:00+00:00",
"employee\_count": 620,
"follower\_count": null
},
{
"date": "2023-01-23T00:00:00+00:00",
"employee\_count": 620,
"follower\_count": null
},
{
"date": "2023-01-30T00:00:00+00:00",
"employee\_count": 620,
"follower\_count": null
},
{
"date": "2023-02-01T00:00:00+00:00",
"employee\_count": 626,
"follower\_count": null
},
{
"date": "2023-02-06T00:00:00+00:00",
"employee\_count": 626,
"follower\_count": null
},
{
"date": "2023-02-13T00:00:00+00:00",
"employee\_count": 626,
"follower\_count": null
},
{
"date": "2023-02-20T00:00:00+00:00",
"employee\_count": 626,
"follower\_count": null
},
{
"date": "2023-02-27T00:00:00+00:00",
"employee\_count": 626,
"follower\_count": null
},
{
"date": "2023-03-01T00:00:00+00:00",
"employee\_count": 638,
"follower\_count": null
},
{
"date": "2023-03-06T00:00:00+00:00",
"employee\_count": 638,
"follower\_count": null
},
{
"date": "2023-03-13T00:00:00+00:00",
"employee\_count": 638,
"follower\_count": null
},
{
"date": "2023-03-20T00:00:00+00:00",
"employee\_count": 638,
"follower\_count": null
},
{
"date": "2023-03-27T00:00:00+00:00",
"employee\_count": 638,
"follower\_count": null
},
{
"date": "2023-04-01T00:00:00+00:00",
"employee\_count": 648,
"follower\_count": null
},
{
"date": "2023-04-03T00:00:00+00:00",
"employee\_count": 648,
"follower\_count": null
},
{
"date": "2023-04-10T00:00:00+00:00",
"employee\_count": 648,
"follower\_count": null
},
{
"date": "2023-04-17T00:00:00+00:00",
"employee\_count": 648,
"follower\_count": null
},
{
"date": "2023-04-24T00:00:00+00:00",
"employee\_count": 648,
"follower\_count": null
},
{
"date": "2023-05-01T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2023-05-08T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2023-05-15T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2023-05-22T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2023-05-29T00:00:00+00:00",
"employee\_count": 656,
"follower\_count": null
},
{
"date": "2023-06-01T00:00:00+00:00",
"employee\_count": 663,
"follower\_count": null
},
{
"date": "2023-06-05T00:00:00+00:00",
"employee\_count": 663,
"follower\_count": null
},
{
"date": "2023-06-12T00:00:00+00:00",
"employee\_count": 663,
"follower\_count": null
},
{
"date": "2023-06-19T00:00:00+00:00",
"employee\_count": 663,
"follower\_count": null
},
{
"date": "2023-06-26T00:00:00+00:00",
"employee\_count": 663,
"follower\_count": null
},
{
"date": "2023-07-01T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": null
},
{
"date": "2023-07-03T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": null
},
{
"date": "2023-07-10T00:00:00+00:00",
"employee\_count": 665,
"follower\_count": 23350
},
{
"date": "2023-07-17T00:00:00+00:00",
"employee\_count": 665,
"follower\_count": 23457
},
{
"date": "2023-07-24T00:00:00+00:00",
"employee\_count": 666,
"follower\_count": 23543
},
{
"date": "2023-07-31T00:00:00+00:00",
"employee\_count": 666,
"follower\_count": 23543
},
{
"date": "2023-08-01T00:00:00+00:00",
"employee\_count": 670,
"follower\_count": 24043
},
{
"date": "2023-08-07T00:00:00+00:00",
"employee\_count": 671,
"follower\_count": 24424
},
{
"date": "2023-08-14T00:00:00+00:00",
"employee\_count": 672,
"follower\_count": 24717
},
{
"date": "2023-08-21T00:00:00+00:00",
"employee\_count": 669,
"follower\_count": 24888
},
{
"date": "2023-08-28T00:00:00+00:00",
"employee\_count": 671,
"follower\_count": 25203
},
{
"date": "2023-09-01T00:00:00+00:00",
"employee\_count": 671,
"follower\_count": 25276
},
{
"date": "2023-09-04T00:00:00+00:00",
"employee\_count": 671,
"follower\_count": 25276
},
{
"date": "2023-09-11T00:00:00+00:00",
"employee\_count": 673,
"follower\_count": 25428
},
{
"date": "2023-09-18T00:00:00+00:00",
"employee\_count": 676,
"follower\_count": 25563
},
{
"date": "2023-09-25T00:00:00+00:00",
"employee\_count": 676,
"follower\_count": 25563
},
{
"date": "2023-10-01T00:00:00+00:00",
"employee\_count": 684,
"follower\_count": 25827
},
{
"date": "2023-10-02T00:00:00+00:00",
"employee\_count": 684,
"follower\_count": 25827
},
{
"date": "2023-10-09T00:00:00+00:00",
"employee\_count": 684,
"follower\_count": 25957
},
{
"date": "2023-10-16T00:00:00+00:00",
"employee\_count": 687,
"follower\_count": 26155
},
{
"date": "2023-10-23T00:00:00+00:00",
"employee\_count": 690,
"follower\_count": 26264
},
{
"date": "2023-10-30T00:00:00+00:00",
"employee\_count": 690,
"follower\_count": 26378
},
{
"date": "2023-11-01T00:00:00+00:00",
"employee\_count": 690,
"follower\_count": 26495
},
{
"date": "2023-11-06T00:00:00+00:00",
"employee\_count": 700,
"follower\_count": 26509
},
{
"date": "2023-11-13T00:00:00+00:00",
"employee\_count": 700,
"follower\_count": 26616
},
{
"date": "2023-11-20T00:00:00+00:00",
"employee\_count": 700,
"follower\_count": 26690
},
{
"date": "2023-11-27T00:00:00+00:00",
"employee\_count": 696,
"follower\_count": 26769
},
{
"date": "2023-12-01T00:00:00+00:00",
"employee\_count": 697,
"follower\_count": 26420
},
{
"date": "2023-12-04T00:00:00+00:00",
"employee\_count": 697,
"follower\_count": 26469
},
{
"date": "2023-12-11T00:00:00+00:00",
"employee\_count": 701,
"follower\_count": 26584
},
{
"date": "2023-12-18T00:00:00+00:00",
"employee\_count": 700,
"follower\_count": 28131
},
{
"date": "2023-12-25T00:00:00+00:00",
"employee\_count": 699,
"follower\_count": 28430
},
{
"date": "2024-01-01T00:00:00+00:00",
"employee\_count": 697,
"follower\_count": 28743
},
{
"date": "2024-01-08T00:00:00+00:00",
"employee\_count": 699,
"follower\_count": 29264
},
{
"date": "2024-01-15T00:00:00+00:00",
"employee\_count": 693,
"follower\_count": 29661
},
{
"date": "2024-01-22T00:00:00+00:00",
"employee\_count": 695,
"follower\_count": 29836
},
{
"date": "2024-01-29T00:00:00+00:00",
"employee\_count": 697,
"follower\_count": 29966
},
{
"date": "2024-02-01T00:00:00+00:00",
"employee\_count": 697,
"follower\_count": 30080
},
{
"date": "2024-02-05T00:00:00+00:00",
"employee\_count": 697,
"follower\_count": 30080
},
{
"date": "2024-02-12T00:00:00+00:00",
"employee\_count": 700,
"follower\_count": 30409
},
{
"date": "2024-02-19T00:00:00+00:00",
"employee\_count": 703,
"follower\_count": 30516
},
{
"date": "2024-02-26T00:00:00+00:00",
"employee\_count": 701,
"follower\_count": 30763
}
],
5
],
[
636304,
"http://www.nowsecure.com",
"336243",
"nowsecure.com",
[
{
"date": "2021-10-01T00:00:00+00:00",
"employee\_count": 124,
"follower\_count": null
},
{
"date": "2021-10-04T00:00:00+00:00",
"employee\_count": 124,
"follower\_count": null
},
{
"date": "2021-10-11T00:00:00+00:00",
"employee\_count": 124,
"follower\_count": null
},
{
"date": "2021-10-18T00:00:00+00:00",
"employee\_count": 124,
"follower\_count": null
},
{
"date": "2021-10-25T00:00:00+00:00",
"employee\_count": 124,
"follower\_count": null
},
{
"date": "2021-11-01T00:00:00+00:00",
"employee\_count": 134,
"follower\_count": null
},
{
"date": "2021-11-08T00:00:00+00:00",
"employee\_count": 134,
"follower\_count": null
},
{
"date": "2021-11-15T00:00:00+00:00",
"employee\_count": 134,
"follower\_count": null
},
{
"date": "2021-11-22T00:00:00+00:00",
"employee\_count": 134,
"follower\_count": null
},
{
"date": "2021-11-29T00:00:00+00:00",
"employee\_count": 134,
"follower\_count": null
},
{
"date": "2021-12-01T00:00:00+00:00",
"employee\_count": 141,
"follower\_count": null
},
{
"date": "2021-12-06T00:00:00+00:00",
"employee\_count": 141,
"follower\_count": null
},
{
"date": "2021-12-13T00:00:00+00:00",
"employee\_count": 141,
"follower\_count": null
},
{
"date": "2021-12-20T00:00:00+00:00",
"employee\_count": 141,
"follower\_count": null
},
{
"date": "2021-12-27T00:00:00+00:00",
"employee\_count": 141,
"follower\_count": null
},
{
"date": "2022-01-01T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": null
},
{
"date": "2022-01-03T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": null
},
{
"date": "2022-01-10T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": null
},
{
"date": "2022-01-17T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": null
},
{
"date": "2022-01-24T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": null
},
{
"date": "2022-01-31T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": null
},
{
"date": "2022-02-01T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": null
},
{
"date": "2022-02-07T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": null
},
{
"date": "2022-02-14T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": null
},
{
"date": "2022-02-21T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": null
},
{
"date": "2022-02-28T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": null
},
{
"date": "2022-03-01T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-03-07T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-03-14T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-03-21T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-03-28T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-04-01T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-04-04T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-04-11T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-04-18T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-04-25T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2022-05-01T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2022-05-02T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2022-05-09T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2022-05-16T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2022-05-23T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2022-05-30T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2022-06-01T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2022-06-06T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2022-06-13T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2022-06-20T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2022-06-27T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2022-07-01T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-07-04T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-07-11T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-07-18T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-07-25T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-08-01T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-08-08T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-08-15T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-08-22T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-08-29T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2022-09-01T00:00:00+00:00",
"employee\_count": 165,
"follower\_count": null
},
{
"date": "2022-09-05T00:00:00+00:00",
"employee\_count": 165,
"follower\_count": null
},
{
"date": "2022-09-12T00:00:00+00:00",
"employee\_count": 165,
"follower\_count": null
},
{
"date": "2022-09-19T00:00:00+00:00",
"employee\_count": 165,
"follower\_count": null
},
{
"date": "2022-09-26T00:00:00+00:00",
"employee\_count": 165,
"follower\_count": null
},
{
"date": "2022-10-01T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2022-10-03T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2022-10-10T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2022-10-17T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2022-10-24T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2022-10-31T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2022-11-01T00:00:00+00:00",
"employee\_count": 166,
"follower\_count": null
},
{
"date": "2022-11-07T00:00:00+00:00",
"employee\_count": 166,
"follower\_count": null
},
{
"date": "2022-11-14T00:00:00+00:00",
"employee\_count": 166,
"follower\_count": null
},
{
"date": "2022-11-21T00:00:00+00:00",
"employee\_count": 166,
"follower\_count": null
},
{
"date": "2022-11-28T00:00:00+00:00",
"employee\_count": 166,
"follower\_count": null
},
{
"date": "2022-12-01T00:00:00+00:00",
"employee\_count": 161,
"follower\_count": null
},
{
"date": "2022-12-05T00:00:00+00:00",
"employee\_count": 161,
"follower\_count": null
},
{
"date": "2022-12-12T00:00:00+00:00",
"employee\_count": 161,
"follower\_count": null
},
{
"date": "2022-12-19T00:00:00+00:00",
"employee\_count": 161,
"follower\_count": null
},
{
"date": "2022-12-26T00:00:00+00:00",
"employee\_count": 161,
"follower\_count": null
},
{
"date": "2023-01-01T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2023-01-02T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2023-01-09T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2023-01-16T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2023-01-23T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2023-01-30T00:00:00+00:00",
"employee\_count": 163,
"follower\_count": null
},
{
"date": "2023-02-01T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-02-06T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-02-13T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-02-20T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-02-27T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-03-01T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-03-06T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-03-13T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-03-20T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-03-27T00:00:00+00:00",
"employee\_count": 164,
"follower\_count": null
},
{
"date": "2023-04-01T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2023-04-03T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2023-04-10T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2023-04-17T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2023-04-24T00:00:00+00:00",
"employee\_count": 159,
"follower\_count": null
},
{
"date": "2023-05-01T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2023-05-08T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2023-05-15T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2023-05-22T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2023-05-29T00:00:00+00:00",
"employee\_count": 152,
"follower\_count": null
},
{
"date": "2023-06-01T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2023-06-05T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2023-06-12T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2023-06-19T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2023-06-26T00:00:00+00:00",
"employee\_count": 147,
"follower\_count": null
},
{
"date": "2023-07-01T00:00:00+00:00",
"employee\_count": 145,
"follower\_count": null
},
{
"date": "2023-07-03T00:00:00+00:00",
"employee\_count": 145,
"follower\_count": null
},
{
"date": "2023-07-10T00:00:00+00:00",
"employee\_count": 149,
"follower\_count": 15659
},
{
"date": "2023-07-17T00:00:00+00:00",
"employee\_count": 146,
"follower\_count": 15809
},
{
"date": "2023-07-24T00:00:00+00:00",
"employee\_count": 146,
"follower\_count": 15837
},
{
"date": "2023-07-31T00:00:00+00:00",
"employee\_count": 146,
"follower\_count": 15837
},
{
"date": "2023-08-01T00:00:00+00:00",
"employee\_count": 145,
"follower\_count": 15883
},
{
"date": "2023-08-07T00:00:00+00:00",
"employee\_count": 145,
"follower\_count": 15892
},
{
"date": "2023-08-14T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": 15921
},
{
"date": "2023-08-21T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": 15936
},
{
"date": "2023-08-28T00:00:00+00:00",
"employee\_count": 144,
"follower\_count": 15936
},
{
"date": "2023-09-01T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": 15963
},
{
"date": "2023-09-04T00:00:00+00:00",
"employee\_count": 143,
"follower\_count": 15963
},
{
"date": "2023-09-11T00:00:00+00:00",
"employee\_count": 140,
"follower\_count": 16098
},
{
"date": "2023-09-18T00:00:00+00:00",
"employee\_count": 140,
"follower\_count": 16129
},
{
"date": "2023-09-25T00:00:00+00:00",
"employee\_count": 140,
"follower\_count": 16129
},
{
"date": "2023-10-01T00:00:00+00:00",
"employee\_count": 140,
"follower\_count": 16290
},
{
"date": "2023-10-02T00:00:00+00:00",
"employee\_count": 140,
"follower\_count": 16290
},
{
"date": "2023-10-09T00:00:00+00:00",
"employee\_count": 140,
"follower\_count": 16381
},
{
"date": "2023-10-16T00:00:00+00:00",
"employee\_count": 140,
"follower\_count": 16466
},
{
"date": "2023-10-23T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": null
},
{
"date": "2023-10-30T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16525
},
{
"date": "2023-11-01T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16584
},
{
"date": "2023-11-06T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16133
},
{
"date": "2023-11-13T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16165
},
{
"date": "2023-11-20T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16173
},
{
"date": "2023-11-27T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16179
},
{
"date": "2023-12-01T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16179
},
{
"date": "2023-12-04T00:00:00+00:00",
"employee\_count": 139,
"follower\_count": 16191
},
{
"date": "2023-12-11T00:00:00+00:00",
"employee\_count": 138,
"follower\_count": 16202
},
{
"date": "2023-12-18T00:00:00+00:00",
"employee\_count": 137,
"follower\_count": 16224
},
{
"date": "2023-12-25T00:00:00+00:00",
"employee\_count": 137,
"follower\_count": 16223
},
{
"date": "2024-01-01T00:00:00+00:00",
"employee\_count": 137,
"follower\_count": 16229
},
{
"date": "2024-01-08T00:00:00+00:00",
"employee\_count": 134,
"follower\_count": 16231
},
{
"date": "2024-01-15T00:00:00+00:00",
"employee\_count": 133,
"follower\_count": 16238
},
{
"date": "2024-01-22T00:00:00+00:00",
"employee\_count": 134,
"follower\_count": 16241
},
{
"date": "2024-01-29T00:00:00+00:00",
"employee\_count": 133,
"follower\_count": 16265
},
{
"date": "2024-02-01T00:00:00+00:00",
"employee\_count": 133,
"follower\_count": 16265
},
{
"date": "2024-02-05T00:00:00+00:00",
"employee\_count": 132,
"follower\_count": 16273
},
{
"date": "2024-02-12T00:00:00+00:00",
"employee\_count": 132,
"follower\_count": 16276
},
{
"date": "2024-02-19T00:00:00+00:00",
"employee\_count": 130,
"follower\_count": 16276
},
{
"date": "2024-02-26T00:00:00+00:00",
"employee\_count": 130,
"follower\_count": 16279
}
],
5
],
[
673947,
"https://www.sketch.com/",
"35625249",
"sketch.com",
[
{
"date": "2021-10-01T00:00:00+00:00",
"employee\_count": 243,
"follower\_count": null
},
{
"date": "2021-10-04T00:00:00+00:00",
"employee\_count": 243,
"follower\_count": null
},
{
"date": "2021-10-11T00:00:00+00:00",
"employee\_count": 243,
"follower\_count": null
},
{
"date": "2021-10-18T00:00:00+00:00",
"employee\_count": 243,
"follower\_count": null
},
{
"date": "2021-10-25T00:00:00+00:00",
"employee\_count": 243,
"follower\_count": null
},
{
"date": "2021-11-01T00:00:00+00:00",
"employee\_count": 257,
"follower\_count": null
},
{
"date": "2021-11-08T00:00:00+00:00",
"employee\_count": 257,
"follower\_count": null
},
{
"date": "2021-11-15T00:00:00+00:00",
"employee\_count": 257,
"follower\_count": null
},
{
"date": "2021-11-22T00:00:00+00:00",
"employee\_count": 257,
"follower\_count": null
},
{
"date": "2021-11-29T00:00:00+00:00",
"employee\_count": 257,
"follower\_count": null
},
{
"date": "2021-12-01T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": null
},
{
"date": "2021-12-06T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": null
},
{
"date": "2021-12-13T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": null
},
{
"date": "2021-12-20T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": null
},
{
"date": "2021-12-27T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": null
},
{
"date": "2022-01-01T00:00:00+00:00",
"employee\_count": 268,
"follower\_count": null
},
{
"date": "2022-01-03T00:00:00+00:00",
"employee\_count": 268,
"follower\_count": null
},
{
"date": "2022-01-10T00:00:00+00:00",
"employee\_count": 268,
"follower\_count": null
},
{
"date": "2022-01-17T00:00:00+00:00",
"employee\_count": 268,
"follower\_count": null
},
{
"date": "2022-01-24T00:00:00+00:00",
"employee\_count": 268,
"follower\_count": null
},
{
"date": "2022-01-31T00:00:00+00:00",
"employee\_count": 268,
"follower\_count": null
},
{
"date": "2022-02-01T00:00:00+00:00",
"employee\_count": 277,
"follower\_count": null
},
{
"date": "2022-02-07T00:00:00+00:00",
"employee\_count": 277,
"follower\_count": null
},
{
"date": "2022-02-14T00:00:00+00:00",
"employee\_count": 277,
"follower\_count": null
},
{
"date": "2022-02-21T00:00:00+00:00",
"employee\_count": 277,
"follower\_count": null
},
{
"date": "2022-02-28T00:00:00+00:00",
"employee\_count": 277,
"follower\_count": null
},
{
"date": "2022-03-01T00:00:00+00:00",
"employee\_count": 283,
"follower\_count": null
},
{
"date": "2022-03-07T00:00:00+00:00",
"employee\_count": 283,
"follower\_count": null
},
{
"date": "2022-03-14T00:00:00+00:00",
"employee\_count": 283,
"follower\_count": null
},
{
"date": "2022-03-21T00:00:00+00:00",
"employee\_count": 283,
"follower\_count": null
},
{
"date": "2022-03-28T00:00:00+00:00",
"employee\_count": 283,
"follower\_count": null
},
{
"date": "2022-04-01T00:00:00+00:00",
"employee\_count": 294,
"follower\_count": null
},
{
"date": "2022-04-04T00:00:00+00:00",
"employee\_count": 294,
"follower\_count": null
},
{
"date": "2022-04-11T00:00:00+00:00",
"employee\_count": 294,
"follower\_count": null
},
{
"date": "2022-04-18T00:00:00+00:00",
"employee\_count": 294,
"follower\_count": null
},
{
"date": "2022-04-25T00:00:00+00:00",
"employee\_count": 294,
"follower\_count": null
},
{
"date": "2022-05-01T00:00:00+00:00",
"employee\_count": 298,
"follower\_count": null
},
{
"date": "2022-05-02T00:00:00+00:00",
"employee\_count": 298,
"follower\_count": null
},
{
"date": "2022-05-09T00:00:00+00:00",
"employee\_count": 298,
"follower\_count": null
},
{
"date": "2022-05-16T00:00:00+00:00",
"employee\_count": 298,
"follower\_count": null
},
{
"date": "2022-05-23T00:00:00+00:00",
"employee\_count": 298,
"follower\_count": null
},
{
"date": "2022-05-30T00:00:00+00:00",
"employee\_count": 298,
"follower\_count": null
},
{
"date": "2022-06-01T00:00:00+00:00",
"employee\_count": 303,
"follower\_count": null
},
{
"date": "2022-06-06T00:00:00+00:00",
"employee\_count": 303,
"follower\_count": null
},
{
"date": "2022-06-13T00:00:00+00:00",
"employee\_count": 303,
"follower\_count": null
},
{
"date": "2022-06-20T00:00:00+00:00",
"employee\_count": 303,
"follower\_count": null
},
{
"date": "2022-06-27T00:00:00+00:00",
"employee\_count": 303,
"follower\_count": null
},
{
"date": "2022-07-01T00:00:00+00:00",
"employee\_count": 314,
"follower\_count": null
},
{
"date": "2022-07-04T00:00:00+00:00",
"employee\_count": 314,
"follower\_count": null
},
{
"date": "2022-07-11T00:00:00+00:00",
"employee\_count": 314,
"follower\_count": null
},
{
"date": "2022-07-18T00:00:00+00:00",
"employee\_count": 314,
"follower\_count": null
},
{
"date": "2022-07-25T00:00:00+00:00",
"employee\_count": 314,
"follower\_count": null
},
{
"date": "2022-08-01T00:00:00+00:00",
"employee\_count": 312,
"follower\_count": null
},
{
"date": "2022-08-08T00:00:00+00:00",
"employee\_count": 312,
"follower\_count": null
},
{
"date": "2022-08-15T00:00:00+00:00",
"employee\_count": 312,
"follower\_count": null
},
{
"date": "2022-08-22T00:00:00+00:00",
"employee\_count": 312,
"follower\_count": null
},
{
"date": "2022-08-29T00:00:00+00:00",
"employee\_count": 312,
"follower\_count": null
},
{
"date": "2022-09-01T00:00:00+00:00",
"employee\_count": 316,
"follower\_count": null
},
{
"date": "2022-09-05T00:00:00+00:00",
"employee\_count": 316,
"follower\_count": null
},
{
"date": "2022-09-12T00:00:00+00:00",
"employee\_count": 316,
"follower\_count": null
},
{
"date": "2022-09-19T00:00:00+00:00",
"employee\_count": 316,
"follower\_count": null
},
{
"date": "2022-09-26T00:00:00+00:00",
"employee\_count": 316,
"follower\_count": null
},
{
"date": "2022-10-01T00:00:00+00:00",
"employee\_count": 267,
"follower\_count": null
},
{
"date": "2022-10-03T00:00:00+00:00",
"employee\_count": 267,
"follower\_count": null
},
{
"date": "2022-10-10T00:00:00+00:00",
"employee\_count": 267,
"follower\_count": null
},
{
"date": "2022-10-17T00:00:00+00:00",
"employee\_count": 267,
"follower\_count": null
},
{
"date": "2022-10-24T00:00:00+00:00",
"employee\_count": 267,
"follower\_count": null
},
{
"date": "2022-10-31T00:00:00+00:00",
"employee\_count": 267,
"follower\_count": null
},
{
"date": "2022-11-01T00:00:00+00:00",
"employee\_count": 252,
"follower\_count": null
},
{
"date": "2022-11-07T00:00:00+00:00",
"employee\_count": 252,
"follower\_count": null
},
{
"date": "2022-11-14T00:00:00+00:00",
"employee\_count": 252,
"follower\_count": null
},
{
"date": "2022-11-21T00:00:00+00:00",
"employee\_count": 252,
"follower\_count": null
},
{
"date": "2022-11-28T00:00:00+00:00",
"employee\_count": 252,
"follower\_count": null
},
{
"date": "2022-12-01T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2022-12-05T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2022-12-12T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2022-12-19T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2022-12-26T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2023-01-01T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-01-02T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-01-09T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-01-16T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-01-23T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-01-30T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-02-01T00:00:00+00:00",
"employee\_count": 241,
"follower\_count": null
},
{
"date": "2023-02-06T00:00:00+00:00",
"employee\_count": 241,
"follower\_count": null
},
{
"date": "2023-02-13T00:00:00+00:00",
"employee\_count": 241,
"follower\_count": null
},
{
"date": "2023-02-20T00:00:00+00:00",
"employee\_count": 241,
"follower\_count": null
},
{
"date": "2023-02-27T00:00:00+00:00",
"employee\_count": 241,
"follower\_count": null
},
{
"date": "2023-03-01T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2023-03-06T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2023-03-13T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2023-03-20T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2023-03-27T00:00:00+00:00",
"employee\_count": 242,
"follower\_count": null
},
{
"date": "2023-04-01T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-04-03T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-04-10T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-04-17T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-04-24T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-05-01T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-05-08T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-05-15T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-05-22T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-05-29T00:00:00+00:00",
"employee\_count": 238,
"follower\_count": null
},
{
"date": "2023-06-01T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-06-05T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-06-12T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-06-19T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-06-26T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-07-01T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-07-03T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": null
},
{
"date": "2023-07-10T00:00:00+00:00",
"employee\_count": 292,
"follower\_count": 71247
},
{
"date": "2023-07-17T00:00:00+00:00",
"employee\_count": 291,
"follower\_count": 71299
},
{
"date": "2023-07-24T00:00:00+00:00",
"employee\_count": 290,
"follower\_count": 71338
},
{
"date": "2023-07-31T00:00:00+00:00",
"employee\_count": 290,
"follower\_count": 71338
},
{
"date": "2023-08-01T00:00:00+00:00",
"employee\_count": 276,
"follower\_count": 71429
},
{
"date": "2023-08-07T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": 71453
},
{
"date": "2023-08-14T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": 71453
},
{
"date": "2023-08-21T00:00:00+00:00",
"employee\_count": 258,
"follower\_count": 71453
},
{
"date": "2023-08-28T00:00:00+00:00",
"employee\_count": 253,
"follower\_count": 71577
},
{
"date": "2023-09-01T00:00:00+00:00",
"employee\_count": 254,
"follower\_count": 71580
},
{
"date": "2023-09-04T00:00:00+00:00",
"employee\_count": 254,
"follower\_count": 71580
},
{
"date": "2023-09-11T00:00:00+00:00",
"employee\_count": 254,
"follower\_count": 71612
},
{
"date": "2023-09-18T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": 71677
},
{
"date": "2023-09-25T00:00:00+00:00",
"employee\_count": 240,
"follower\_count": 71677
},
{
"date": "2023-10-01T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 71733
},
{
"date": "2023-10-02T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 71733
},
{
"date": "2023-10-09T00:00:00+00:00",
"employee\_count": 233,
"follower\_count": 71753
},
{
"date": "2023-10-16T00:00:00+00:00",
"employee\_count": 232,
"follower\_count": 71775
},
{
"date": "2023-10-23T00:00:00+00:00",
"employee\_count": 235,
"follower\_count": 71806
},
{
"date": "2023-10-30T00:00:00+00:00",
"employee\_count": 235,
"follower\_count": null
},
{
"date": "2023-11-01T00:00:00+00:00",
"employee\_count": 235,
"follower\_count": 70563
},
{
"date": "2023-11-06T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 70266
},
{
"date": "2023-11-13T00:00:00+00:00",
"employee\_count": 235,
"follower\_count": 70280
},
{
"date": "2023-11-20T00:00:00+00:00",
"employee\_count": 236,
"follower\_count": 70298
},
{
"date": "2023-11-27T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 70295
},
{
"date": "2023-12-01T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 70305
},
{
"date": "2023-12-04T00:00:00+00:00",
"employee\_count": 235,
"follower\_count": 70327
},
{
"date": "2023-12-11T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 70350
},
{
"date": "2023-12-18T00:00:00+00:00",
"employee\_count": 236,
"follower\_count": 70370
},
{
"date": "2023-12-25T00:00:00+00:00",
"employee\_count": 235,
"follower\_count": 70385
},
{
"date": "2024-01-01T00:00:00+00:00",
"employee\_count": 235,
"follower\_count": 70407
},
{
"date": "2024-01-08T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 70456
},
{
"date": "2024-01-15T00:00:00+00:00",
"employee\_count": 234,
"follower\_count": 70494
},
{
"date": "2024-01-22T00:00:00+00:00",
"employee\_count": 230,
"follower\_count": 70574
},
{
"date": "2024-01-29T00:00:00+00:00",
"employee\_count": 230,
"follower\_count": 70616
},
{
"date": "2024-02-01T00:00:00+00:00",
"employee\_count": 228,
"follower\_count": 70636
},
{
"date": "2024-02-05T00:00:00+00:00",
"employee\_count": 228,
"follower\_count": 70636
},
{
"date": "2024-02-12T00:00:00+00:00",
"employee\_count": 223,
"follower\_count": 70626
},
{
"date": "2024-02-19T00:00:00+00:00",
"employee\_count": 224,
"follower\_count": 70643
},
{
"date": "2024-02-26T00:00:00+00:00",
"employee\_count": 223,
"follower\_count": 70643
}
],
5
],
[
680992,
"http://www.microstrategy.com",
"3643",
"microstrategy.com",
[
{
"date": "2021-08-01T00:00:00+00:00",
"employee\_count": 3266,
"follower\_count": null
},
{
"date": "2021-08-02T00:00:00+00:00",
"employee\_count": 3266,
"follower\_count": null
},
{
"date": "2021-08-09T00:00:00+00:00",
"employee\_count": 3266,
"follower\_count": null
},
{
"date": "2021-08-16T00:00:00+00:00",
"employee\_count": 3266,
"follower\_count": null
},
{
"date": "2021-08-23T00:00:00+00:00",
"employee\_count": 3266,
"follower\_count": null
},
{
"date": "2021-08-30T00:00:00+00:00",
"employee\_count": 3266,
"follower\_count": null
},
{
"date": "2021-09-01T00:00:00+00:00",
"employee\_count": 3278,
"follower\_count": null
},
{
"date": "2021-09-06T00:00:00+00:00",
"employee\_count": 3278,
"follower\_count": null
},
{
"date": "2021-09-13T00:00:00+00:00",
"employee\_count": 3278,
"follower\_count": null
},
{
"date": "2021-09-20T00:00:00+00:00",
"employee\_count": 3278,
"follower\_count": null
},
{
"date": "2021-09-27T00:00:00+00:00",
"employee\_count": 3278,
"follower\_count": null
},
{
"date": "2021-10-01T00:00:00+00:00",
"employee\_count": 3305,
"follower\_count": null
},
{
"date": "2021-10-04T00:00:00+00:00",
"employee\_count": 3305,
"follower\_count": null
},
{
"date": "2021-10-11T00:00:00+00:00",
"employee\_count": 3305,
"follower\_count": null
},
{
"date": "2021-10-18T00:00:00+00:00",
"employee\_count": 3305,
"follower\_count": null
},
{
"date": "2021-10-25T00:00:00+00:00",
"employee\_count": 3305,
"follower\_count": null
},
{
"date": "2021-11-01T00:00:00+00:00",
"employee\_count": 3327,
"follower\_count": null
},
{
"date": "2021-11-08T00:00:00+00:00",
"employee\_count": 3327,
"follower\_count": null
},
{
"date": "2021-11-15T00:00:00+00:00",
"employee\_count": 3327,
"follower\_count": null
},
{
"date": "2021-11-22T00:00:00+00:00",
"employee\_count": 3327,
"follower\_count": null
},
{
"date": "2021-11-29T00:00:00+00:00",
"employee\_count": 3327,
"follower\_count": null
},
{
"date": "2021-12-01T00:00:00+00:00",
"employee\_count": 3331,
"follower\_count": null
},
{
"date": "2021-12-06T00:00:00+00:00",
"employee\_count": 3331,
"follower\_count": null
},
{
"date": "2021-12-13T00:00:00+00:00",
"employee\_count": 3331,
"follower\_count": null
},
{
"date": "2021-12-20T00:00:00+00:00",
"employee\_count": 3331,
"follower\_count": null
},
{
"date": "2021-12-27T00:00:00+00:00",
"employee\_count": 3331,
"follower\_count": null
},
{
"date": "2022-01-01T00:00:00+00:00",
"employee\_count": 3359,
"follower\_count": null
},
{
"date": "2022-01-03T00:00:00+00:00",
"employee\_count": 3359,
"follower\_count": null
},
{
"date": "2022-01-10T00:00:00+00:00",
"employee\_count": 3359,
"follower\_count": null
},
{
"date": "2022-01-17T00:00:00+00:00",
"employee\_count": 3359,
"follower\_count": null
},
{
"date": "2022-01-24T00:00:00+00:00",
"employee\_count": 3359,
"follower\_count": null
},
{
"date": "2022-01-31T00:00:00+00:00",
"employee\_count": 3359,
"follower\_count": null
},
{
"date": "2022-02-01T00:00:00+00:00",
"employee\_count": 3366,
"follower\_count": null
},
{
"date": "2022-02-07T00:00:00+00:00",
"employee\_count": 3366,
"follower\_count": null
},
{
"date": "2022-02-14T00:00:00+00:00",
"employee\_count": 3366,
"follower\_count": null
},
{
"date": "2022-02-21T00:00:00+00:00",
"employee\_count": 3366,
"follower\_count": null
},
{
"date": "2022-02-28T00:00:00+00:00",
"employee\_count": 3366,
"follower\_count": null
},
{
"date": "2022-03-01T00:00:00+00:00",
"employee\_count": 3388,
"follower\_count": null
},
{
"date": "2022-03-07T00:00:00+00:00",
"employee\_count": 3388,
"follower\_count": null
},
{
"date": "2022-03-14T00:00:00+00:00",
"employee\_count": 3388,
"follower\_count": null
},
{
"date": "2022-03-21T00:00:00+00:00",
"employee\_count": 3388,
"follower\_count": null
},
{
"date": "2022-03-28T00:00:00+00:00",
"employee\_count": 3388,
"follower\_count": null
},
{
"date": "2022-04-01T00:00:00+00:00",
"employee\_count": 3391,
"follower\_count": null
},
{
"date": "2022-04-04T00:00:00+00:00",
"employee\_count": 3391,
"follower\_count": null
},
{
"date": "2022-04-11T00:00:00+00:00",
"employee\_count": 3391,
"follower\_count": null
},
{
"date": "2022-04-18T00:00:00+00:00",
"employee\_count": 3391,
"follower\_count": null
},
{
"date": "2022-04-25T00:00:00+00:00",
"employee\_count": 3391,
"follower\_count": null
},
{
"date": "2022-05-01T00:00:00+00:00",
"employee\_count": 3409,
"follower\_count": null
},
{
"date": "2022-05-02T00:00:00+00:00",
"employee\_count": 3409,
"follower\_count": null
},
{
"date": "2022-05-09T00:00:00+00:00",
"employee\_count": 3409,
"follower\_count": null
},
{
"date": "2022-05-16T00:00:00+00:00",
"employee\_count": 3409,
"follower\_count": null
},
{
"date": "2022-05-23T00:00:00+00:00",
"employee\_count": 3409,
"follower\_count": null
},
{
"date": "2022-05-30T00:00:00+00:00",
"employee\_count": 3409,
"follower\_count": null
},
{
"date": "2022-06-01T00:00:00+00:00",
"employee\_count": 3414,
"follower\_count": null
},
{
"date": "2022-06-06T00:00:00+00:00",
"employee\_count": 3414,
"follower\_count": null
},
{
"date": "2022-06-13T00:00:00+00:00",
"employee\_count": 3414,
"follower\_count": null
},
{
"date": "2022-06-20T00:00:00+00:00",
"employee\_count": 3414,
"follower\_count": null
},
{
"date": "2022-06-27T00:00:00+00:00",
"employee\_count": 3414,
"follower\_count": null
},
{
"date": "2022-07-01T00:00:00+00:00",
"employee\_count": 3428,
"follower\_count": null
},
{
"date": "2022-07-04T00:00:00+00:00",
"employee\_count": 3428,
"follower\_count": null
},
{
"date": "2022-07-11T00:00:00+00:00",
"employee\_count": 3428,
"follower\_count": null
},
{
"date": "2022-07-18T00:00:00+00:00",
"employee\_count": 3428,
"follower\_count": null
},
{
"date": "2022-07-25T00:00:00+00:00",
"employee\_count": 3428,
"follower\_count": null
},
{
"date": "2022-08-01T00:00:00+00:00",
"employee\_count": 3429,
"follower\_count": null
},
{
"date": "2022-08-08T00:00:00+00:00",
"employee\_count": 3429,
"follower\_count": null
},
{
"date": "2022-08-15T00:00:00+00:00",
"employee\_count": 3429,
"follower\_count": null
},
{
"date": "2022-08-22T00:00:00+00:00",
"employee\_count": 3429,
"follower\_count": null
},
{
"date": "2022-08-29T00:00:00+00:00",
"employee\_count": 3429,
"follower\_count": null
},
{
"date": "2022-09-01T00:00:00+00:00",
"employee\_count": 3442,
"follower\_count": null
},
{
"date": "2022-09-05T00:00:00+00:00",
"employee\_count": 3442,
"follower\_count": null
},
{
"date": "2022-09-12T00:00:00+00:00",
"employee\_count": 3442,
"follower\_count": null
},
{
"date": "2022-09-19T00:00:00+00:00",
"employee\_count": 3442,
"follower\_count": null
},
{
"date": "2022-09-26T00:00:00+00:00",
"employee\_count": 3442,
"follower\_count": null
},
{
"date": "2022-10-01T00:00:00+00:00",
"employee\_count": 3446,
"follower\_count": null
},
{
"date": "2022-10-03T00:00:00+00:00",
"employee\_count": 3446,
"follower\_count": null
},
{
"date": "2022-10-10T00:00:00+00:00",
"employee\_count": 3446,
"follower\_count": null
},
{
"date": "2022-10-17T00:00:00+00:00",
"employee\_count": 3446,
"follower\_count": null
},
{
"date": "2022-10-24T00:00:00+00:00",
"employee\_count": 3446,
"follower\_count": null
},
{
"date": "2022-10-31T00:00:00+00:00",
"employee\_count": 3446,
"follower\_count": null
},
{
"date": "2022-11-01T00:00:00+00:00",
"employee\_count": 3471,
"follower\_count": null
},
{
"date": "2022-11-07T00:00:00+00:00",
"employee\_count": 3471,
"follower\_count": null
},
{
"date": "2022-11-14T00:00:00+00:00",
"employee\_count": 3471,
"follower\_count": null
},
{
"date": "2022-11-21T00:00:00+00:00",
"employee\_count": 3471,
"follower\_count": null
},
{
"date": "2022-11-28T00:00:00+00:00",
"employee\_count": 3471,
"follower\_count": null
},
{
"date": "2022-12-01T00:00:00+00:00",
"employee\_count": 3448,
"follower\_count": null
},
{
"date": "2022-12-05T00:00:00+00:00",
"employee\_count": 3448,
"follower\_count": null
},
{
"date": "2022-12-12T00:00:00+00:00",
"employee\_count": 3448,
"follower\_count": null
},
{
"date": "2022-12-19T00:00:00+00:00",
"employee\_count": 3448,
"follower\_count": null
},
{
"date": "2022-12-26T00:00:00+00:00",
"employee\_count": 3448,
"follower\_count": null
},
{
"date": "2023-01-01T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": null
},
{
"date": "2023-01-02T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": null
},
{
"date": "2023-01-09T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": null
},
{
"date": "2023-01-16T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": null
},
{
"date": "2023-01-23T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": null
},
{
"date": "2023-01-30T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": null
},
{
"date": "2023-02-01T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-02-06T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-02-13T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-02-20T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-02-27T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-03-01T00:00:00+00:00",
"employee\_count": 3467,
"follower\_count": null
},
{
"date": "2023-03-06T00:00:00+00:00",
"employee\_count": 3467,
"follower\_count": null
},
{
"date": "2023-03-13T00:00:00+00:00",
"employee\_count": 3467,
"follower\_count": null
},
{
"date": "2023-03-20T00:00:00+00:00",
"employee\_count": 3467,
"follower\_count": null
},
{
"date": "2023-03-27T00:00:00+00:00",
"employee\_count": 3467,
"follower\_count": null
},
{
"date": "2023-04-01T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-04-03T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-04-10T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-04-17T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-04-24T00:00:00+00:00",
"employee\_count": 3470,
"follower\_count": null
},
{
"date": "2023-05-01T00:00:00+00:00",
"employee\_count": 3479,
"follower\_count": null
},
{
"date": "2023-05-08T00:00:00+00:00",
"employee\_count": 3479,
"follower\_count": null
},
{
"date": "2023-05-15T00:00:00+00:00",
"employee\_count": 3479,
"follower\_count": null
},
{
"date": "2023-05-22T00:00:00+00:00",
"employee\_count": 3479,
"follower\_count": null
},
{
"date": "2023-05-29T00:00:00+00:00",
"employee\_count": 3479,
"follower\_count": null
},
{
"date": "2023-06-01T00:00:00+00:00",
"employee\_count": 3484,
"follower\_count": null
},
{
"date": "2023-06-05T00:00:00+00:00",
"employee\_count": 3484,
"follower\_count": null
},
{
"date": "2023-06-12T00:00:00+00:00",
"employee\_count": 3484,
"follower\_count": null
},
{
"date": "2023-06-19T00:00:00+00:00",
"employee\_count": 3484,
"follower\_count": null
},
{
"date": "2023-06-26T00:00:00+00:00",
"employee\_count": 3484,
"follower\_count": null
},
{
"date": "2023-07-01T00:00:00+00:00",
"employee\_count": 3482,
"follower\_count": null
},
{
"date": "2023-07-03T00:00:00+00:00",
"employee\_count": 3482,
"follower\_count": null
},
{
"date": "2023-07-10T00:00:00+00:00",
"employee\_count": 3472,
"follower\_count": 194951
},
{
"date": "2023-07-17T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": null
},
{
"date": "2023-07-24T00:00:00+00:00",
"employee\_count": 3466,
"follower\_count": 195483
},
{
"date": "2023-07-31T00:00:00+00:00",
"employee\_count": 3466,
"follower\_count": 195483
},
{
"date": "2023-08-01T00:00:00+00:00",
"employee\_count": 3463,
"follower\_count": 196567
},
{
"date": "2023-08-07T00:00:00+00:00",
"employee\_count": 3469,
"follower\_count": 196846
},
{
"date": "2023-08-14T00:00:00+00:00",
"employee\_count": 3473,
"follower\_count": 197196
},
{
"date": "2023-08-21T00:00:00+00:00",
"employee\_count": 3457,
"follower\_count": 197391
},
{
"date": "2023-08-28T00:00:00+00:00",
"employee\_count": 3443,
"follower\_count": 197800
},
{
"date": "2023-09-01T00:00:00+00:00",
"employee\_count": 3443,
"follower\_count": 197842
},
{
"date": "2023-09-04T00:00:00+00:00",
"employee\_count": 3443,
"follower\_count": 197842
},
{
"date": "2023-09-11T00:00:00+00:00",
"employee\_count": 3440,
"follower\_count": 198532
},
{
"date": "2023-09-18T00:00:00+00:00",
"employee\_count": 3431,
"follower\_count": 198877
},
{
"date": "2023-09-25T00:00:00+00:00",
"employee\_count": 3431,
"follower\_count": 198877
},
{
"date": "2023-10-01T00:00:00+00:00",
"employee\_count": 3408,
"follower\_count": 201809
},
{
"date": "2023-10-02T00:00:00+00:00",
"employee\_count": 3408,
"follower\_count": 201809
},
{
"date": "2023-10-09T00:00:00+00:00",
"employee\_count": 3402,
"follower\_count": 202936
},
{
"date": "2023-10-16T00:00:00+00:00",
"employee\_count": 3405,
"follower\_count": 203790
},
{
"date": "2023-10-23T00:00:00+00:00",
"employee\_count": 3397,
"follower\_count": 205640
},
{
"date": "2023-10-30T00:00:00+00:00",
"employee\_count": 3397,
"follower\_count": 207228
},
{
"date": "2023-11-01T00:00:00+00:00",
"employee\_count": 3397,
"follower\_count": 207977
},
{
"date": "2023-11-06T00:00:00+00:00",
"employee\_count": 3399,
"follower\_count": 205522
},
{
"date": "2023-11-13T00:00:00+00:00",
"employee\_count": 3397,
"follower\_count": 204410
},
{
"date": "2023-11-20T00:00:00+00:00",
"employee\_count": 3395,
"follower\_count": 204500
},
{
"date": "2023-11-27T00:00:00+00:00",
"employee\_count": 3399,
"follower\_count": 204605
},
{
"date": "2023-12-01T00:00:00+00:00",
"employee\_count": 3396,
"follower\_count": 204673
},
{
"date": "2023-12-04T00:00:00+00:00",
"employee\_count": 3396,
"follower\_count": 204749
},
{
"date": "2023-12-11T00:00:00+00:00",
"employee\_count": 3394,
"follower\_count": 205277
},
{
"date": "2023-12-18T00:00:00+00:00",
"employee\_count": 3409,
"follower\_count": 206548
},
{
"date": "2023-12-25T00:00:00+00:00",
"employee\_count": 3397,
"follower\_count": 207119
},
{
"date": "2024-01-01T00:00:00+00:00",
"employee\_count": 3405,
"follower\_count": 207810
},
{
"date": "2024-01-08T00:00:00+00:00",
"employee\_count": 3402,
"follower\_count": 208576
},
{
"date": "2024-01-15T00:00:00+00:00",
"employee\_count": 3426,
"follower\_count": 209746
},
{
"date": "2024-01-22T00:00:00+00:00",
"employee\_count": 3415,
"follower\_count": 210596
},
{
"date": "2024-01-29T00:00:00+00:00",
"employee\_count": 3406,
"follower\_count": 211112
},
{
"date": "2024-02-01T00:00:00+00:00",
"employee\_count": 3406,
"follower\_count": 211112
},
{
"date": "2024-02-05T00:00:00+00:00",
"employee\_count": 3398,
"follower\_count": 211743
},
{
"date": "2024-02-12T00:00:00+00:00",
"employee\_count": 3385,
"follower\_count": 211974
},
{
"date": "2024-02-19T00:00:00+00:00",
"employee\_count": 3387,
"follower\_count": 212161
},
{
"date": "2024-02-26T00:00:00+00:00",
"employee\_count": 3391,
"follower\_count": 212385
},
{
"date": "2024-03-01T00:00:00+00:00",
"employee\_count": 3384,
"follower\_count": 212564
}
],
5
]
],
"is\_trial\_user": false
}​
#### 5. Employee Headcount By Function

Use this request to get the headcount by function for the given company.You either provide with a list of Crustdata’s company\_id or company\_website\_domain in the filtersCUrlBashCopycurl --request POST \
--url https://api.crustdata.com/data\_lab/linkedin\_headcount\_by\_facet/Table/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--header 'Origin: https://crustdata.com' \
--data '{
"tickers": [],
"dataset": {
"name": "linkedin\_headcount\_by\_facet",
"id": "linkedinheadcountbyfacet"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_id", "type": "in", "value": [680992, 673947, 631280], "allow\_null": false}
]
},
"groups": [],
"aggregations": [],
"functions": [],
"offset": 0,
"count": 100,
"sorts": []
}'
​Result[JSON HeroJSON Hero makes reading and understand JSON files easy by giving you a clean and beautiful UI packed with extra features.![](/image/https%3A%2F%2Fjsonhero.io%2Ffavicon.ico?table=block&id=e9b46128-c40e-4f3e-ac42-5c91b6e93487&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)https://jsonhero.io/j/SC3GAjKPzkDw/editor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://jsonhero.io/j/SC3GAjKPzkDw/editor)BashCopy{
"fields": [
{
"type": "string",
"api\_name": "linkedin\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_name",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website\_domain",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "facet\_linkedin\_employee\_count",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "date",
"api\_name": "as\_of\_date",
"hidden": false,
"options": [
"-default\_sort"
],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "dataset\_row\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": null,
"company\_profile\_name": null,
"geocode": false
},
{
"type": "string",
"api\_name": "linkedin\_headcount\_facet\_type",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "linkedin\_headcount\_facet\_value",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "linkedin\_headcount\_facet\_name",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "linkedin\_profile\_url",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website\_domain",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "company\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": null,
"company\_profile\_name": null,
"geocode": false
},
{
"type": "number",
"api\_name": "total\_rows",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
}
],
"rows": [
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
6,
"2024-02-28T00:00:00Z",
41260836,
"CURRENT\_FUNCTION",
"5",
"Community and Social Services",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
13,
"2024-02-28T00:00:00Z",
41260818,
"GEO\_REGION",
"106057199",
"Brazil",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
5,
"2024-02-28T00:00:00Z",
41260838,
"CURRENT\_FUNCTION",
"15",
"Marketing",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
4,
"2024-02-28T00:00:00Z",
41260841,
"CURRENT\_FUNCTION",
"14",
"Legal",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
10,
"2024-02-28T00:00:00Z",
41260824,
"GEO\_REGION",
"90009790",
"Greater Madrid Metropolitan Area",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
8,
"2024-02-28T00:00:00Z",
41260826,
"GEO\_REGION",
"105088894",
"Barcelona",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
24,
"2024-02-28T00:00:00Z",
41260829,
"CURRENT\_FUNCTION",
"4",
"Business Development",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
14,
"2024-02-28T00:00:00Z",
41260832,
"CURRENT\_FUNCTION",
"26",
"Customer Success and Support",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
7,
"2024-02-28T00:00:00Z",
41260835,
"CURRENT\_FUNCTION",
"2",
"Administrative",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
4,
"2024-02-28T00:00:00Z",
41260840,
"CURRENT\_FUNCTION",
"12",
"Human Resources",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
62,
"2024-02-28T00:00:00Z",
41260827,
"CURRENT\_FUNCTION",
"3",
"Arts and Design",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
15,
"2024-02-28T00:00:00Z",
41260831,
"CURRENT\_FUNCTION",
"13",
"Information Technology",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
10,
"2024-02-28T00:00:00Z",
41260822,
"GEO\_REGION",
"100994331",
"Madrid",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
11,
"2024-02-28T00:00:00Z",
41260821,
"GEO\_REGION",
"106155005",
"Egypt",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
9,
"2024-02-28T00:00:00Z",
41260825,
"GEO\_REGION",
"90009706",
"The Randstad, Netherlands",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
60,
"2024-02-28T00:00:00Z",
41260828,
"CURRENT\_FUNCTION",
"8",
"Engineering",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
13,
"2024-02-28T00:00:00Z",
41260817,
"GEO\_REGION",
"102299470",
"England, United Kingdom",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
10,
"2024-02-28T00:00:00Z",
41260823,
"GEO\_REGION",
"103335767",
"Community of Madrid, Spain",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
5,
"2024-02-28T00:00:00Z",
41260839,
"CURRENT\_FUNCTION",
"7",
"Education",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
18,
"2024-02-28T00:00:00Z",
41260815,
"GEO\_REGION",
"101165590",
"United Kingdom",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
26,
"2024-02-28T00:00:00Z",
41260812,
"GEO\_REGION",
"102713980",
"India",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
11,
"2024-02-28T00:00:00Z",
41260819,
"GEO\_REGION",
"100358611",
"Minas Gerais, Brazil",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
5,
"2024-02-28T00:00:00Z",
41260837,
"CURRENT\_FUNCTION",
"1",
"Accounting",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
14,
"2024-02-28T00:00:00Z",
41260816,
"GEO\_REGION",
"102890719",
"Netherlands",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
11,
"2024-02-28T00:00:00Z",
41260833,
"CURRENT\_FUNCTION",
"25",
"Sales",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
16,
"2024-02-28T00:00:00Z",
41260830,
"CURRENT\_FUNCTION",
"18",
"Operations",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
26,
"2024-02-28T00:00:00Z",
41260813,
"GEO\_REGION",
"105646813",
"Spain",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
21,
"2024-02-28T00:00:00Z",
41260814,
"GEO\_REGION",
"100364837",
"Portugal",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
9,
"2024-02-28T00:00:00Z",
41260834,
"CURRENT\_FUNCTION",
"16",
"Media and Communication",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
11,
"2024-02-28T00:00:00Z",
41260820,
"GEO\_REGION",
"103644278",
"United States",
"https://www.linkedin.com/company/sketchbv",
"https://sketch.com/",
"sketch.com",
673947,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
95,
"2023-12-22T00:00:00Z",
37687823,
"CURRENT\_FUNCTION",
"19",
"Product Management",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
876,
"2023-12-22T00:00:00Z",
37687802,
"GEO\_REGION",
"102890883",
"China",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
677,
"2023-12-22T00:00:00Z",
37687803,
"GEO\_REGION",
"90000097",
"Washington DC-Baltimore Area",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
1082,
"2023-12-22T00:00:00Z",
37687801,
"GEO\_REGION",
"103644278",
"United States",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
428,
"2023-12-22T00:00:00Z",
37687805,
"GEO\_REGION",
"105072130",
"Poland",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
95,
"2023-12-22T00:00:00Z",
37687824,
"CURRENT\_FUNCTION",
"22",
"Quality Assurance",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
80,
"2023-12-22T00:00:00Z",
37687829,
"CURRENT\_FUNCTION",
"10",
"Finance",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
119,
"2023-12-22T00:00:00Z",
37687822,
"CURRENT\_FUNCTION",
"1",
"Accounting",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
573,
"2023-12-22T00:00:00Z",
37687804,
"GEO\_REGION",
"101630962",
"Virginia, United States",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
335,
"2023-12-22T00:00:00Z",
37687810,
"GEO\_REGION",
"90009563",
"Hangzhou-Shaoxing Metropolitan Area",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
95,
"2023-12-22T00:00:00Z",
37687824,
"CURRENT\_FUNCTION",
"22",
"Quality Assurance",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
85,
"2023-12-22T00:00:00Z",
37687827,
"CURRENT\_FUNCTION",
"12",
"Human Resources",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
321,
"2023-12-22T00:00:00Z",
37687811,
"GEO\_REGION",
"101821877",
"Hangzhou",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
340,
"2023-12-22T00:00:00Z",
37687809,
"GEO\_REGION",
"105076658",
"Warsaw",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
94,
"2023-12-22T00:00:00Z",
37687825,
"CURRENT\_FUNCTION",
"20",
"Program and Project Management",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
91,
"2023-12-22T00:00:00Z",
37687826,
"CURRENT\_FUNCTION",
"7",
"Education",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
428,
"2023-12-22T00:00:00Z",
37687805,
"GEO\_REGION",
"105072130",
"Poland",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
573,
"2023-12-22T00:00:00Z",
37687804,
"GEO\_REGION",
"101630962",
"Virginia, United States",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
75,
"2023-12-22T00:00:00Z",
37687830,
"CURRENT\_FUNCTION",
"2",
"Administrative",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
368,
"2023-12-22T00:00:00Z",
37687806,
"GEO\_REGION",
"102996679",
"Mazowieckie, Poland",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
83,
"2023-12-22T00:00:00Z",
37687828,
"CURRENT\_FUNCTION",
"3",
"Arts and Design",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
94,
"2023-12-22T00:00:00Z",
37687825,
"CURRENT\_FUNCTION",
"20",
"Program and Project Management",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
91,
"2023-12-22T00:00:00Z",
37687826,
"CURRENT\_FUNCTION",
"7",
"Education",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
85,
"2023-12-22T00:00:00Z",
37687827,
"CURRENT\_FUNCTION",
"12",
"Human Resources",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
118,
"2023-12-22T00:00:00Z",
37687813,
"GEO\_REGION",
"101627305",
"Vienna, VA",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
876,
"2023-12-22T00:00:00Z",
37687802,
"GEO\_REGION",
"102890883",
"China",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
677,
"2023-12-22T00:00:00Z",
37687803,
"GEO\_REGION",
"90000097",
"Washington DC-Baltimore Area",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
112,
"2023-12-22T00:00:00Z",
37687814,
"GEO\_REGION",
"103873152",
"Beijing, China",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
142,
"2023-12-22T00:00:00Z",
37687812,
"GEO\_REGION",
"102713980",
"India",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
343,
"2023-12-22T00:00:00Z",
37687808,
"GEO\_REGION",
"106834892",
"Zhejiang, China",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
321,
"2023-12-22T00:00:00Z",
37687811,
"GEO\_REGION",
"101821877",
"Hangzhou",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
335,
"2023-12-22T00:00:00Z",
37687810,
"GEO\_REGION",
"90009563",
"Hangzhou-Shaoxing Metropolitan Area",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
647,
"2023-12-22T00:00:00Z",
37687817,
"CURRENT\_FUNCTION",
"25",
"Sales",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
340,
"2023-12-22T00:00:00Z",
37687809,
"GEO\_REGION",
"105076658",
"Warsaw",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
112,
"2023-12-22T00:00:00Z",
37687814,
"GEO\_REGION",
"103873152",
"Beijing, China",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
480,
"2023-12-22T00:00:00Z",
37687818,
"CURRENT\_FUNCTION",
"13",
"Information Technology",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
768,
"2023-12-22T00:00:00Z",
37687816,
"CURRENT\_FUNCTION",
"8",
"Engineering",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
198,
"2023-12-22T00:00:00Z",
37687820,
"CURRENT\_FUNCTION",
"4",
"Business Development",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
359,
"2023-12-22T00:00:00Z",
37687819,
"CURRENT\_FUNCTION",
"6",
"Consulting",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
134,
"2023-12-22T00:00:00Z",
37687821,
"CURRENT\_FUNCTION",
"18",
"Operations",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
134,
"2023-12-22T00:00:00Z",
37687821,
"CURRENT\_FUNCTION",
"18",
"Operations",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
480,
"2023-12-22T00:00:00Z",
37687818,
"CURRENT\_FUNCTION",
"13",
"Information Technology",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
104,
"2023-12-22T00:00:00Z",
37687815,
"GEO\_REGION",
"100446943",
"Argentina",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
768,
"2023-12-22T00:00:00Z",
37687816,
"CURRENT\_FUNCTION",
"8",
"Engineering",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
118,
"2023-12-22T00:00:00Z",
37687813,
"GEO\_REGION",
"101627305",
"Vienna, VA",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
198,
"2023-12-22T00:00:00Z",
37687820,
"CURRENT\_FUNCTION",
"4",
"Business Development",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
343,
"2023-12-22T00:00:00Z",
37687808,
"GEO\_REGION",
"106834892",
"Zhejiang, China",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
142,
"2023-12-22T00:00:00Z",
37687812,
"GEO\_REGION",
"102713980",
"India",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
119,
"2023-12-22T00:00:00Z",
37687822,
"CURRENT\_FUNCTION",
"1",
"Accounting",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
95,
"2023-12-22T00:00:00Z",
37687823,
"CURRENT\_FUNCTION",
"19",
"Product Management",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
75,
"2023-12-22T00:00:00Z",
37687830,
"CURRENT\_FUNCTION",
"2",
"Administrative",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
647,
"2023-12-22T00:00:00Z",
37687817,
"CURRENT\_FUNCTION",
"25",
"Sales",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
365,
"2023-12-22T00:00:00Z",
37687807,
"GEO\_REGION",
"90009828",
"Warsaw Metropolitan Area",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
1082,
"2023-12-22T00:00:00Z",
37687801,
"GEO\_REGION",
"103644278",
"United States",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
359,
"2023-12-22T00:00:00Z",
37687819,
"CURRENT\_FUNCTION",
"6",
"Consulting",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
368,
"2023-12-22T00:00:00Z",
37687806,
"GEO\_REGION",
"102996679",
"Mazowieckie, Poland",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
104,
"2023-12-22T00:00:00Z",
37687815,
"GEO\_REGION",
"100446943",
"Argentina",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
365,
"2023-12-22T00:00:00Z",
37687807,
"GEO\_REGION",
"90009828",
"Warsaw Metropolitan Area",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
83,
"2023-12-22T00:00:00Z",
37687828,
"CURRENT\_FUNCTION",
"3",
"Arts and Design",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
80,
"2023-12-22T00:00:00Z",
37687829,
"CURRENT\_FUNCTION",
"10",
"Finance",
"https://www.linkedin.com/company/microstrategy",
"http://www.microstrategy.com",
"microstrategy.com",
680992,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
274,
"2023-12-12T00:00:00Z",
37662401,
"CURRENT\_FUNCTION",
"8",
"Engineering",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
29,
"2023-12-12T00:00:00Z",
37662409,
"CURRENT\_FUNCTION",
"3",
"Arts and Design",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
636,
"2023-12-12T00:00:00Z",
37662386,
"GEO\_REGION",
"103644278",
"United States",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
322,
"2023-12-12T00:00:00Z",
37662387,
"GEO\_REGION",
"102095887",
"California, United States",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
201,
"2023-12-12T00:00:00Z",
37662402,
"CURRENT\_FUNCTION",
"25",
"Sales",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
285,
"2023-12-12T00:00:00Z",
37662388,
"GEO\_REGION",
"90000084",
"San Francisco Bay Area",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
17,
"2023-12-12T00:00:00Z",
37662413,
"CURRENT\_FUNCTION",
"20",
"Program and Project Management",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
75,
"2023-12-12T00:00:00Z",
37662389,
"GEO\_REGION",
"101165590",
"United Kingdom",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
97,
"2023-12-12T00:00:00Z",
37662403,
"CURRENT\_FUNCTION",
"13",
"Information Technology",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
61,
"2023-12-12T00:00:00Z",
37662390,
"GEO\_REGION",
"102277331",
"San Francisco, CA",
"https://www.linkedin.com/company/lacework",
"https://www.lacework.com/",
"lacework.com",
631280,
1411
]
],
"is\_trial\_user": false
}​
#### 6. Glassdoor Profile Metrics

Use this request to get the rating of a company on Glassdoor, number of reviews, business outlook, CEO approval rating etc. You either provide with a list of Crustdata’s company\_id or company\_website\_domain in the filtersCUrlBashCopycurl --request POST \
--url https://api.crustdata.com/data\_lab/glassdoor\_profile\_metric/Table/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--header 'Origin: https://crustdata.com' \
--data '{
"tickers": [],
"dataset": {
"name": "glassdoor\_profile\_metric",
"id": "glassdoorprofilemetric"
},
"filters": {
"op": "and",
"conditions": [
{"column": "company\_id", "type": "in", "value": [680992,673947,631280,636304,631811], "allow\_null": false}
]
},
"groups": [],
"aggregations": [],
"functions": [],
"offset": 0,
"count": 100,
"sorts": []
}'
​Result[JSON HeroJSON Hero makes reading and understand JSON files easy by giving you a clean and beautiful UI packed with extra features.![](/image/https%3A%2F%2Fjsonhero.io%2Ffavicon.ico?table=block&id=f0da2283-66de-46e4-bda3-7554591a5917&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)https://jsonhero.io/j/SdGsOnEIJ33x/editor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://jsonhero.io/j/SdGsOnEIJ33x/editor)BashCopy{
"fields": [
{
"type": "string",
"api\_name": "linkedin\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_name",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website\_domain",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "date",
"api\_name": "as\_of\_date",
"hidden": false,
"options": [
"-default\_sort"
],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "overall\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "culture\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "diversity\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "work\_life\_balance\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "senior\_management\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "compensation\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "career\_opportunities\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "recommend\_to\_friend\_pct",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "ceo\_approval\_pct",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "business\_outlook\_pct",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "glassdoor\_profile\_review\_count",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "dataset\_row\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": null,
"company\_profile\_name": null,
"geocode": false
},
{
"type": "string",
"api\_name": "glassdoor\_profile\_url",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "company\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": null,
"company\_profile\_name": null,
"geocode": false
},
{
"type": "number",
"api\_name": "total\_rows",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
}
],
"rows": [
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2024-01-07T00:00:00Z",
3.45124,
3.38798,
3.67852,
3.84519,
3.13893,
3.42953,
3.06081,
53,
82,
48,
null,
10358925,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2024-01-07T00:00:00Z",
3.67224,
3.57151,
3.70108,
3.42699,
3.41481,
4.24173,
3.66685,
64,
68,
59,
null,
10358663,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-12-15T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10351760,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-12-14T00:00:00Z",
3.79139,
3.78391,
4.08457,
3.98375,
3.29903,
3.68142,
3.57313,
72,
44,
52,
null,
10347613,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-12-14T00:00:00Z",
3.35782,
3.25678,
3.43557,
3.20794,
3.0963,
3.72396,
2.7581,
52,
52,
44,
null,
10340407,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-12-14T00:00:00Z",
3.79139,
3.78391,
4.08457,
3.98375,
3.29903,
3.68142,
3.57313,
72,
44,
52,
null,
10347613,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-12-09T00:00:00Z",
3.66592,
3.55772,
3.73303,
3.48027,
3.40452,
4.24256,
3.6359,
64,
69,
59,
null,
10326729,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-12-09T00:00:00Z",
3.45719,
3.39712,
3.68392,
3.85088,
3.14617,
3.43255,
3.07375,
53,
82,
49,
null,
10326947,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-29T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10316287,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-29T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10303197,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-29T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10303661,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-29T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10314166,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-29T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10306852,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-29T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10316287,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-28T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10271730,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-28T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10275385,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-28T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10272194,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-28T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10284819,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-28T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10284819,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-28T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10282698,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-27T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10253095,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-27T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10250974,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-27T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10253095,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-27T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10240005,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-27T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10240469,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-27T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10243660,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-26T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
9422658,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-26T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10222325,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-26T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10228802,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-26T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10222663,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-26T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10228802,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-26T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10224517,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-25T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10192615,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-25T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10195806,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-25T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10205241,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-25T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10205241,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-25T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10203120,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-25T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10192151,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-24T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10173515,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-24T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10160889,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-24T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10171394,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-24T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10173515,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-24T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10160425,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-24T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10164080,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-23T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10129163,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-23T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10128699,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-23T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10139668,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-23T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10132354,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-23T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10141789,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-23T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10141789,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-22T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10107942,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-22T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10110063,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-22T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10097437,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-22T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10100628,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-22T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10110063,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-22T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10096973,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-21T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10076216,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-21T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10065711,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-21T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10078337,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-21T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10065247,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-21T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10068902,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-21T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10078337,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-20T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10046611,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-20T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10037176,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-20T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10033985,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-20T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10044490,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-20T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10033521,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-20T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10046611,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-19T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
10005450,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-19T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
10002259,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-19T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10014885,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-19T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
10001795,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-19T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
10012764,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-19T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
10014885,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-18T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
9981038,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-18T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
9973724,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-18T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9983159,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-18T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
9970069,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-18T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
9970533,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-18T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9983159,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-17T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
9941998,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-17T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
9938807,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-17T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
9949312,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-17T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9951433,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-17T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
9938343,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-17T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9951433,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-16T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9919707,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-16T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
9907081,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-16T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9919707,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-16T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
9917586,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-16T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
9906617,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-16T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
9910272,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-15T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9887981,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-11-15T00:00:00Z",
3.46299,
3.40603,
3.68921,
3.85645,
3.15324,
3.43549,
3.0864,
54,
81,
49,
null,
9875355,
"https://www.glassdoor.co.in/Overview/Working-at-jumpcloud-EI\_IE1446075.htm",
631811,
2512
],
[
"336243",
"http://www.nowsecure.com",
"NowSecure",
"nowsecure.com",
"2023-11-15T00:00:00Z",
3.36071,
3.25607,
3.43968,
3.20678,
3.10027,
3.72756,
2.76508,
52,
53,
45,
null,
9878546,
"https://www.glassdoor.co.in/Overview/Working-at-nowsecure-EI\_IE753560.htm",
636304,
2512
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-11-15T00:00:00Z",
3.78005,
3.77406,
4.15817,
3.95615,
3.29744,
3.71042,
3.56022,
72,
49,
54,
null,
9887981,
"https://www.glassdoor.com/Overview/Working-at-microstrategy-EI\_IE8018.htm",
680992,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-15T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
9885860,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-15T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
9874891,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
],
[
"35625249",
"https://www.sketch.com/",
"Sketch",
"sketch.com",
"2023-11-14T00:00:00Z",
4.81397,
4.82756,
4.60647,
5,
4.58143,
4.7735,
4.24984,
91,
100,
69,
null,
9854134,
"https://www.glassdoor.com/Overview/Working-at-sketch-EI\_IE3068411.htm",
673947,
2512
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-11-14T00:00:00Z",
3.75364,
3.64831,
3.79233,
3.54338,
3.47932,
4.28775,
3.70777,
67,
73,
62,
null,
9843165,
"https://www.glassdoor.co.in/Overview/Working-at-lacework-EI\_IE1373969.htm",
631280,
2512
]
],
"is\_trial\_user": false
}​
#### 7. G2 Profile Metrics

Use this request to get the rating of a company’s product on G2 and number of reviews etc. CUrlBashCopycurl --request POST \
--url http://api.crustdata.com/data\_lab/g2\_profile\_metrics/Table/ \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--header 'Origin: https://crustdata.com' \
--data '{
"tickers": [],
"dataset": {
"name": "g2\_profile\_metrics",
"id": "g2profilemetric"
},
"filters": {
"op": "or",
"conditions": [
{"column": "company\_website\_domain", "type": "=", "value": "microstrategy.com", "allow\_null": false},
{"column": "company\_website\_domain", "type": "=", "value": "lacework.com", "allow\_null": false},
{"column": "company\_website\_domain", "type": "=", "value": "jumpcloud.com", "allow\_null": false}
]
},
"groups": [],
"aggregations": [],
"functions": [],
"offset": 0,
"count": 100,
"sorts": []
}'
​Result[JSON HeroJSON Hero makes reading and understand JSON files easy by giving you a clean and beautiful UI packed with extra features.![](/image/https%3A%2F%2Fjsonhero.io%2Ffavicon.ico?table=block&id=0e567014-6356-4887-a879-8a4554f40c17&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)https://jsonhero.io/j/DUeuNGh42nyO/editor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://jsonhero.io/j/DUeuNGh42nyO/editor)BashCopy{
"fields": [
{
"type": "string",
"api\_name": "linkedin\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_name",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website\_domain",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "date",
"api\_name": "as\_of\_date",
"hidden": false,
"options": [
"-default\_sort"
],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "review\_count",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "average\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "g2\_rating",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "dataset\_row\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": null,
"company\_profile\_name": null,
"geocode": false
},
{
"type": "string",
"api\_name": "title",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "slug",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "profile\_url",
"hidden": false,
"options": [
"url"
],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "vendor\_name",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "description",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "string",
"api\_name": "type",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
},
{
"type": "number",
"api\_name": "company\_id",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": null,
"company\_profile\_name": null,
"geocode": false
},
{
"type": "number",
"api\_name": "total\_rows",
"hidden": true,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"geocode": false
}
],
"rows": [
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-28T00:00:00Z",
464,
8.35345,
8.4,
1234738,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-28T00:00:00Z",
269,
8.82836,
8.8,
1231195,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-28T00:00:00Z",
1802,
9.08657,
9.1,
1231396,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-28T00:00:00Z",
464,
8.35345,
8.4,
1234738,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-27T00:00:00Z",
464,
8.35345,
8.4,
743350,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-27T00:00:00Z",
464,
8.35345,
8.4,
743350,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-27T00:00:00Z",
269,
8.82836,
8.8,
741662,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-27T00:00:00Z",
1802,
9.08657,
9.1,
741746,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-26T00:00:00Z",
219,
8.78539,
8.8,
1227348,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-26T00:00:00Z",
463,
8.34989,
8.3,
1230891,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-26T00:00:00Z",
1667,
9.08578,
9.1,
1227549,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-26T00:00:00Z",
463,
8.34989,
8.3,
1230891,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-25T00:00:00Z",
219,
8.78539,
8.8,
1223762,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-25T00:00:00Z",
1667,
9.08578,
9.1,
1223963,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-25T00:00:00Z",
463,
8.34989,
8.3,
1227305,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-25T00:00:00Z",
463,
8.34989,
8.3,
1227305,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-24T00:00:00Z",
219,
8.78539,
8.8,
1220176,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-24T00:00:00Z",
463,
8.34989,
8.3,
1223719,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-24T00:00:00Z",
1667,
9.08578,
9.1,
1220377,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-24T00:00:00Z",
463,
8.34989,
8.3,
1223719,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-23T00:00:00Z",
463,
8.34989,
8.3,
1220133,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-23T00:00:00Z",
219,
8.78539,
8.8,
1216590,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-23T00:00:00Z",
1667,
9.08578,
9.1,
1216791,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-23T00:00:00Z",
463,
8.34989,
8.3,
1220133,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-22T00:00:00Z",
219,
8.78539,
8.8,
1213004,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-22T00:00:00Z",
463,
8.34989,
8.3,
1216547,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-22T00:00:00Z",
463,
8.34989,
8.3,
1216547,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-22T00:00:00Z",
1667,
9.08578,
9.1,
1213205,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-21T00:00:00Z",
463,
8.34989,
8.3,
1212961,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-21T00:00:00Z",
1667,
9.08578,
9.1,
1209619,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-21T00:00:00Z",
219,
8.78539,
8.8,
1209418,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-21T00:00:00Z",
463,
8.34989,
8.3,
1212961,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-20T00:00:00Z",
1667,
9.08578,
9.1,
1206033,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-20T00:00:00Z",
463,
8.34989,
8.3,
1209375,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-20T00:00:00Z",
463,
8.34989,
8.3,
1209375,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-20T00:00:00Z",
219,
8.78539,
8.8,
1205832,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-19T00:00:00Z",
463,
8.34989,
8.3,
1205789,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-19T00:00:00Z",
463,
8.34989,
8.3,
1205789,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-19T00:00:00Z",
1667,
9.08578,
9.1,
1202447,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-19T00:00:00Z",
219,
8.78539,
8.8,
1202246,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-18T00:00:00Z",
1667,
9.08578,
9.1,
1198861,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-18T00:00:00Z",
219,
8.78539,
8.8,
1198660,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-18T00:00:00Z",
463,
8.34989,
8.3,
1202203,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-18T00:00:00Z",
463,
8.34989,
8.3,
1202203,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-17T00:00:00Z",
219,
8.78539,
8.8,
1195074,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-17T00:00:00Z",
463,
8.34989,
8.3,
1198617,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-17T00:00:00Z",
463,
8.34989,
8.3,
1198617,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-17T00:00:00Z",
1667,
9.08578,
9.1,
1195275,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-16T00:00:00Z",
463,
8.34989,
8.3,
1195031,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-16T00:00:00Z",
463,
8.34989,
8.3,
1195031,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-16T00:00:00Z",
1667,
9.08578,
9.1,
1191689,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-16T00:00:00Z",
219,
8.78539,
8.8,
1191488,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-15T00:00:00Z",
219,
8.78539,
8.8,
1187902,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-15T00:00:00Z",
463,
8.34989,
8.3,
1191445,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-15T00:00:00Z",
463,
8.34989,
8.3,
1191445,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-15T00:00:00Z",
1667,
9.08578,
9.1,
1188103,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-14T00:00:00Z",
463,
8.34989,
8.3,
1187859,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-14T00:00:00Z",
1667,
9.08578,
9.1,
1184517,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-14T00:00:00Z",
463,
8.34989,
8.3,
1187859,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-14T00:00:00Z",
219,
8.78539,
8.8,
1184316,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-13T00:00:00Z",
463,
8.34989,
8.3,
1184273,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-13T00:00:00Z",
463,
8.34989,
8.3,
1184273,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-13T00:00:00Z",
219,
8.78539,
8.8,
1180730,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-13T00:00:00Z",
1667,
9.08578,
9.1,
1180931,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-12T00:00:00Z",
1667,
9.08578,
9.1,
1177345,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-12T00:00:00Z",
463,
8.34989,
8.3,
1180687,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-12T00:00:00Z",
219,
8.78539,
8.8,
1177144,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-12T00:00:00Z",
463,
8.34989,
8.3,
1180687,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-11T00:00:00Z",
463,
8.34989,
8.3,
1177101,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-11T00:00:00Z",
463,
8.34989,
8.3,
1177101,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-11T00:00:00Z",
1667,
9.08578,
9.1,
1173759,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-11T00:00:00Z",
219,
8.78539,
8.8,
1173558,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-10T00:00:00Z",
1667,
9.08578,
9.1,
1170173,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-10T00:00:00Z",
463,
8.34989,
8.3,
1173515,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-10T00:00:00Z",
463,
8.34989,
8.3,
1173515,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-10T00:00:00Z",
219,
8.78539,
8.8,
1169972,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-09T00:00:00Z",
1667,
9.08578,
9.1,
1166587,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-09T00:00:00Z",
463,
8.34989,
8.3,
1169929,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-09T00:00:00Z",
219,
8.78539,
8.8,
1166386,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-09T00:00:00Z",
463,
8.34989,
8.3,
1169929,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-08T00:00:00Z",
1667,
9.08578,
9.1,
1163001,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-08T00:00:00Z",
463,
8.34989,
8.3,
1166343,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-08T00:00:00Z",
463,
8.34989,
8.3,
1166343,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-08T00:00:00Z",
219,
8.78539,
8.8,
1162800,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-07T00:00:00Z",
463,
8.34989,
8.3,
1162757,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-07T00:00:00Z",
463,
8.34989,
8.3,
1162757,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-07T00:00:00Z",
219,
8.78539,
8.8,
1159214,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-07T00:00:00Z",
1667,
9.08578,
9.1,
1159415,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-06T00:00:00Z",
1667,
9.08578,
9.1,
1155829,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-06T00:00:00Z",
463,
8.34989,
8.3,
1159171,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-06T00:00:00Z",
463,
8.34989,
8.3,
1159171,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-06T00:00:00Z",
219,
8.78539,
8.8,
1155628,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-05T00:00:00Z",
1667,
9.08578,
9.1,
1152243,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-05T00:00:00Z",
463,
8.34989,
8.3,
1155585,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-05T00:00:00Z",
463,
8.34989,
8.3,
1155585,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-05T00:00:00Z",
219,
8.78539,
8.8,
1152042,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-04T00:00:00Z",
463,
8.34989,
8.3,
1151999,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
],
[
"3033823",
"http://jumpcloud.com",
"JumpCloud",
"jumpcloud.com",
"2023-07-04T00:00:00Z",
1667,
9.08578,
9.1,
1148657,
"jumpcloud",
"jumpcloud",
"https://www.g2.com/products/jumpcloud/reviews",
"JumpCloud Inc.",
"The JumpCloud Directory Platform reimagines the directory as a complete platform for identity, access, and device management.",
"Software",
631811,
1266
],
[
"17932068",
"https://www.lacework.com",
"Lacework",
"lacework.com",
"2023-07-04T00:00:00Z",
219,
8.78539,
8.8,
1148456,
"lacework",
"lacework",
"https://www.g2.com/products/lacework/reviews",
"Lacework",
"Lacework automates security and compliance across AWS, Azure, GCP, and private clouds, providing a comprehensive view of risks across cloud workloads and containers. Lacework’s unified cloud security platform provides unmatched visibility, automates intrusion detection, delivers one-click investigation, and simplifies cloud compliance.",
"Software",
631280,
1266
],
[
"3643",
"http://www.microstrategy.com",
"MicroStrategy",
"microstrategy.com",
"2023-07-04T00:00:00Z",
463,
8.34989,
8.3,
1151999,
"microstrategy",
"microstrategy",
"https://www.g2.com/products/microstrategy/reviews",
"MicroStrategy",
"MicroStrategy provides a high performance, scalable Business Intelligence platform delivering insight with interactive dashboards and superior analytics.",
"Software",
680992,
1266
]
],
"is\_trial\_user": false
}​
#### 8. Web Traffic

Use this request to get historical web-traffic of a company by domaincURLBashCopycurl --request POST \
--url 'https://api.crustdata.com/data\_lab/webtraffic/' \
--header 'Accept: \*/\*' \
--header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'Authorization: Token $token' \
--header 'Content-Type: application/json' \
--data '{
"filters": {
"op": "or",
"conditions": [
{
"column": "company\_website",
"type": "(.)",
"value": "wefitanyfurniture.com"
}
]
},
"offset": 0,
"count": 100,
"sorts": []
}'
​ResultBashCopy {
"fields": [
{
"type": "foreign\_key",
"api\_name": "company\_id",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"preview\_description": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_website",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"preview\_description": "",
"geocode": false
},
{
"type": "string",
"api\_name": "company\_name",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"preview\_description": "",
"geocode": false
},
{
"type": "array",
"api\_name": "similarweb\_traffic\_timeseries",
"hidden": false,
"options": [],
"summary": "",
"local\_metric": false,
"display\_name": "",
"company\_profile\_name": "",
"preview\_description": "",
"geocode": false
}
],
"rows": [
[
1411045,
"wefitanyfurniture.com",
"WeFitAnyFurniture",
[
{
"date": "2024-07-01T00:00:00+00:00",
"monthly\_visitors": 355,
"traffic\_source\_social\_pct": null,
"traffic\_source\_search\_pct": null,
"traffic\_source\_direct\_pct": null,
"traffic\_source\_paid\_referral\_pct": null,
"traffic\_source\_referral\_pct": null
},
{
"date": "2024-08-01T00:00:00+00:00",
"monthly\_visitors": 1255,
"traffic\_source\_social\_pct": null,
"traffic\_source\_search\_pct": null,
"traffic\_source\_direct\_pct": null,
"traffic\_source\_paid\_referral\_pct": null,
"traffic\_source\_referral\_pct": null
},
{
"date": "2024-09-01T00:00:00+00:00",
"monthly\_visitors": 3728,
"traffic\_source\_social\_pct": 4.1587388254523585,
"traffic\_source\_search\_pct": 48.335395016304005,
"traffic\_source\_direct\_pct": 32.901089596227564,
"traffic\_source\_paid\_referral\_pct": 0.9439998798176015,
"traffic\_source\_referral\_pct": 12.431220453595381
}
]
]
]
}
​Key Points:When querying a website, compute the domain ($domain ) and then pass it in the conditions object of the payload likeBashCopy [{
"column": "company\_website",
"type": "(.)",
"value": "$domain"
}]
​If there is no data for the website, it will be auto-enriched in next 24 hours. Just query again.For parsing the response, please follow:<https://www.notion.so/crustdata/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=4#28de6e16940c4615b5872020a345766a>
#### 9. Investor Portfolio

Retrieve portfolio details for a specified investor. Each investor, as returned in the [company enrichment endpoint](/c66d5236e8ea40df8af114f6d447ab48?pvs=25#10ee4a7d95b1807bb965dad5a67086e3), has a unique identifier (UUID), name, and type. This API allows you to fetch the full portfolio of companies associated with an investor, using either the investor's uuid or name as an identifier.cURLExample 1: query by investor uuid Note: uuid for an investor can be retrieved from /screener/company response. It is available in funding\_and\_investment.crunchbase\_investors\_info\_list[\*].uuid field BashCopycurl 'https://api.crustdata.com/data\_lab/investor\_portfolio?investor\_uuid=ce91bad7-b6d8-e56e-0f45-4763c6c5ca29' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​Example 2: query by investor name Note: uuid for an investor can be retrieved from /screener/company response. It is available in funding\_and\_investment.crunchbase\_investors\_info\_list[\*].uuid field BashCopycurl 'https://api.crustdata.com/data\_lab/investor\_portfolio?investor\_name=Sequoia Capital' \
--header 'Accept: application/json, text/plain, \*/\*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Token $auth\_token'
​ResultFull sample: <https://jsonhero.io/j/hSEHVFgv68pz>