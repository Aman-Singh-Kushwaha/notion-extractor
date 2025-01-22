# Crustdata Data Dictionary

Crustdata Data Dictionary[![](/image/https%3A%2F%2Fbeestat.io%2Fimg%2Fnotion%2Fapi.svg?table=block&id=c66d5236-e8ea-40df-8af1-14f6d447ab48&spaceId=7e107e8b-8d78-4070-ade3-738aaa4dc2de&userId=&cache=v2)Crustdata Discovery And Enrichment API](/Crustdata-Discovery-And-Enrichment-API-c66d5236e8ea40df8af114f6d447ab48?pvs=18)/![📔](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)Crustdata Data DictionaryMade with![📔](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)![📔](https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f4d4.svg)
# Crustdata Data Dictionary

## Company

### Firmographics

| Column | Description | Source | Time series available |
| --- | --- | --- | --- |
| company\_name | Name of the company |  |  |
| last\_updated\_date | The timestamp when this information was last updated |  |  |
| hq\_country | The country where the company's headquarters is located | Linkedin |  |
| largest\_headcount\_country | The country with the most employees of the company | Linkedin |  |
| last\_funding\_round\_type | The type of the company's last funding round | Crunchbase |  |
| company\_website | The company's official website URL |  |  |
| company\_website\_domain | The domain of the company's website |  |  |
| valuation\_usd | The current valuation of the company in USD | Tracxn |  |
| valuation\_date | The date when the current valuation was determined | Tracxn |  |
| linkedin\_categories | The categories of the company on LinkedIn | Linkedin |  |
| linkedin\_industries | The industries in which the company operates, according to LinkedIn | Linkedin |  |
| crunchbase\_investors | The investors in the company, according to Crunchbase | Crunchbase |  |
| tracxn\_investors | The investors in the company, according to Tracxn | Tracxn |  |
| crunchbase\_categories | The categories of the company on Crunchbase | Crunchbase |  |
| crunchbase\_total\_investment\_usd | The total amount of investment the company has received, according to Crunchbase | Crunchbase | Yes |
| markets | The markets in which the company operates. Eg: Private/NSE/NASDAQ | Crunchbase |  |
| days\_since\_last\_fundraise | The number of days since the company's last fundraising round | Crunchbase |  |
| linkedin\_profile\_url | The URL of the company's LinkedIn profile | Linkedin |  |
| acquisition\_status | The current acquisition status of the company | Crunchbase |  |
| year\_founded | The year the company was founded | Linkedin |  |
| technology\_domains | The technology domains in which the company operates |  |  |
| twitter\_handle | Twitter handle of the company | Twitter |  |
| linkedin\_id | LinkedIn ID of the company | LinkedIn |  |
| linkedin\_company\_description | Description about the company as put in the “About” section of their LinkedIn page | LinkedIn |  |
| acquisition\_status | “acquired” if the company is acquired. Empty otherwise | Linkedin / Crunchbase |  |
| stock\_symbols | The ticker symbols for publicly traded companies | Crunchbase |  |

### Founder background

| Column Name | Description | Source |
| --- | --- | --- |
| founder\_names\_and\_profile\_urls | Names and Linkedin profile URLs of the company's founders and decision makers (CxO and VP/Head of Sales/Marketing/Engineering/Product) | Linkedin |
| founders\_location | geographical location(s) of the company's and decision makers (CxO and VP/Head of Sales/Marketing/Engineering/Product) | Linkedin |
| founders\_education\_institute | educational institutions attended by the company's founders and decision makers (CxO and VP/Head of Sales/Marketing/Engineering/Product) | Linkedin |
| founders\_degree\_name | degree(s) held by the company's founders and decision makers (CxO and VP/Head of Sales/Marketing/Engineering/Product) | Linkedin |
| founders\_previous\_company | previous company(ies) where the company's founders and decision makers (CxO and VP/Head of Sales/Marketing/Engineering/Product) have worked before | Linkedin |
| founders\_previous\_title | previous job title(s) held by the company's founders and decision makers (CxO and VP/Head of Sales/Marketing/Engineering/Product) | Linkedin |
| founders\_email | business email of founders | Apollo/Proprietary |

### Revenue

| Column Name | Description | Source |
| --- | --- | --- |
| estimated\_revenue\_lower\_bound\_usd | Estimated revenue in USD lower limit | LinkedIn |
| estimated\_revenue\_higher\_bound\_usd | Estimated revenue in USD higher limit | LinkedIn |

### Employee Headcount

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| linkedin\_headcount | The total number of employees at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_followers | The total number of followers of the company's LinkedIn profile | LinkedIn | Yes |
| linkedin\_headcount\_engineering | The total number of engineering employees at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_sales | The total number of sales employees at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_operations | The total number of operations employees at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_human\_resource | The total number of human resources employees at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_india | The total number of employees based in India at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_usa | The total number of employees based in USA at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_engineering\_pct | The percentage of employees that are in engineering roles, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_sales\_pct | The percentage of employees that are in sales roles, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_operations\_pct | The percentage of employees that are in operations roles, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_human\_resource\_pct | The percentage of employees that are in human resources roles, according to LinkedIn | LinkedIn | Yes |
| linkedin\_headcount\_india\_pct | The percentage of employees that are based in India, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_usa\_pct | The percentage of employees that are based in USA, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_mom\_pct | The month-over-month percentage change in headcount, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_qoq\_pct | The quarter-over-quarter percentage change in headcount, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_yoy\_pct | The year-over-year percentage change in headcount, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_mom\_absolute | The month-over-month absolute change in headcount, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_qoq\_absolute | The quarter-over-quarter absolute change in headcount, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_yoy\_absolute | The year-over-year absolute change in headcount, according to LinkedIn | LinkedIn |  |
| linkedin\_followers\_mom\_pct | The month-over-month percentage change in the number of followers, according to LinkedIn | LinkedIn |  |
| linkedin\_followers\_qoq\_pct | The quarter-over-quarter percentage change in the number of followers, according to LinkedIn | LinkedIn |  |
| linkedin\_followers\_yoy\_pct | The year-over-year percentage change in the number of followers, according to LinkedIn | LinkedIn |  |
| linkedin\_headcount\_sales\_six\_months\_growth\_pct | The six months growth percentage in Sales headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_sales\_yoy\_growth\_pct | The one year growth percentage in Sales headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_operations\_six\_months\_growth\_pct | The six months growth percentage in Sales headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_operations\_yoy\_growth\_pct | The one year growth percentage in Operations headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_quality\_assurance\_six\_months\_growth\_pct | The six months growth percentage in Quality Assurance headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_quality\_assurance\_yoy\_growth\_pct | The one year growth percentage in Quality Assurance headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_usa\_six\_months\_growth\_pct | The six months growth percentage in US headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_usa\_yoy\_growth\_pct | The one year growth percentage in US headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_india\_six\_months\_growth\_pct | The six months growth percentage in US headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_india\_yoy\_growth\_pct | The one year growth percentage in US headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_mexico\_six\_months\_growth\_pct | The six months growth percentage in US headcount, according to Linkedin | Linkedin |  |
| linkedin\_headcount\_mexico\_yoy\_growth\_pct | The one year growth percentage in US headcount, according to Linkedin | Linkedin |  |

### Employee Skills

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| linkedin\_all\_employee\_skill\_names | All skill names of employees at the company, according to LinkedIn | LinkedIn |  |
| linkedin\_all\_employee\_skill\_count | Count of each skill among employees at the company, according to LinkedIn | LinkedIn | Yes |
| linkedin\_employee\_skills\_0\_to\_10\_pct | Percentage of employees with 0-10% proficiency in skills, according to LinkedIn | LinkedIn |  |
| linkedin\_employee\_skills\_11\_to\_30\_pct | Percentage of employees with 11-30% proficiency in skills, according to LinkedIn | LinkedIn |  |
| linkedin\_employee\_skills\_31\_to\_50\_pct | Percentage of employees with 31-50% proficiency in skills, according to LinkedIn | LinkedIn |  |
| linkedin\_employee\_skills\_51\_to\_70\_pct | Percentage of employees with 51-70% proficiency in skills, according to LinkedIn | LinkedIn |  |
| linkedin\_employee\_skills\_71\_to\_100\_pct | Percentage of employees with 71-100% proficiency in skills, according to LinkedIn | LinkedIn |  |

### Employee Review and Rating

| Column Name | Description | Source | Time series available |
| --- | --- | --- | --- |
| glassdoor\_overall\_rating | The company's overall rating on Glassdoor | Glassdoor | Yes |
| glassdoor\_culture\_rating | The company's culture rating on Glassdoor | Glassdoor | Yes |
| glassdoor\_diversity\_rating | The company's diversity rating on Glassdoor | Glassdoor | Yes |
| glassdoor\_work\_life\_balance\_rating | The company's work-life balance rating on Glassdoor | Glassdoor | Yes |
| glassdoor\_senior\_management\_rating | The company's senior management rating on Glassdoor | Glassdoor | Yes |
| glassdoor\_compensation\_rating | The company's compensation rating on Glassdoor | Glassdoor | Yes |
| glassdoor\_career\_opportunities\_rating | The company's career opportunities rating on Glassdoor | Glassdoor | Yes |
| glassdoor\_recommend\_to\_friend\_pct | The percentage of Glassdoor reviewers who would recommend the company to a friend | Glassdoor | Yes |
| glassdoor\_ceo\_approval\_pct | The percentage of Glassdoor reviewers who approve of the CEO | Glassdoor | Yes |
| glassdoor\_business\_outlook\_pct | The percentage of Glassdoor reviewers who have a positive business outlook for the company | Glassdoor | Yes |
| glassdoor\_review\_count | The number of reviews of the company on Glassdoor | Glassdoor | Yes |
| glassdoor\_ceo\_approval\_mom\_pct | The month-over-month percentage change in CEO approval rating on Glassdoor | Glassdoor |  |
| glassdoor\_ceo\_approval\_qoq\_pct | The quarter-over-quarter percentage change in CEO approval rating on Glassdoor | Glassdoor |  |
| glassdoor\_ceo\_approval\_mom\_pct | The year-over-year percentage change in CEO approval rating on Glassdoor | Glassdoor |  |
| glassdoor\_review\_count\_mom\_pct | The month-over-month percentage change in the number of reviews on Glassdoor | Glassdoor |  |
| glassdoor\_review\_count\_qoq\_pct | The quarter-over-quarter percentage change in the number of reviews on Glassdoor | Glassdoor |  |
| glassdoor\_review\_count\_yoy\_pct | The year-over-year percentage change in the number of reviews on Glassdoor | Glassdoor |  |

### Product Reviews

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| g2\_review\_count | The number of reviews of the company on G2 | G2 | Yes |
| g2\_average\_rating | The company's average rating on G2 | G2 | Yes |
| g2\_review\_count\_mom\_pct | The month-over-month percentage change in the number of reviews on G2 | G2 |  |
| g2\_review\_count\_qoq\_pct | The quarter-over-quarter percentage change in the number of reviews on G2 | G2 |  |
| g2\_review\_count\_yoy\_pct | The year-over-year percentage change in the number of reviews on G2 | G2 |  |

### Web Traffic

| Column Name | Description | Source | Time series available |
| --- | --- | --- | --- |
| monthly\_visitors | The number of monthly visitors to the company's site as recorded by Similarweb | Similarweb | Yes |
| monthly\_visitor\_mom\_pct | The month-over-month percentage change in the number of monthly visitors to the company's site as recorded by Similarweb | Similarweb |  |
| traffic\_source\_social\_pct | The percentage of the company's site traffic that comes from social media, as recorded by Similarweb | Similarweb |  |
| traffic\_source\_search\_pct | The percentage of the company's site traffic that comes from search engines, as recorded by Similarweb | Similarweb |  |
| traffic\_source\_direct\_pct | The percentage of the company's site traffic that comes directly, as recorded by Similarweb | Similarweb |  |
| traffic\_source\_paid\_referral\_pct | The percentage of the company's site traffic that comes from paid referrals, as recorded by Similarweb | Similarweb |  |
| traffic\_source\_referral\_pct | The percentage of the company's site traffic that comes from non-paid referrals, as recorded by Similarweb | Similarweb |  |

### Job Listing Growth By Function

| Column Name | Description | Source |
| --- | --- | --- |
| job\_openings\_accounting\_qoq\_pct | Quarterly growth percentage of job openings in accounting | LinkedIn |
| job\_openings\_accounting\_six\_months\_growth\_pct | Six months growth percentage of job openings in accounting | LinkedIn |
| job\_openings\_art\_and\_design\_qoq\_pct | Quarterly growth percentage of job openings in art and design | LinkedIn |
| job\_openings\_art\_and\_design\_six\_months\_growth\_pct | Six months growth percentage of job openings in art and design | LinkedIn |
| job\_openings\_business\_development\_qoq\_pct | Quarterly growth percentage of job openings in business development | LinkedIn |
| job\_openings\_business\_development\_six\_months\_growth\_pct | Six months growth percentage of job openings in business development | LinkedIn |
| job\_openings\_engineering\_qoq\_pct | Quarterly growth percentage of job openings in engineering | LinkedIn |
| job\_openings\_engineering\_six\_months\_growth\_pct | Six months growth percentage of job openings in engineering | LinkedIn |
| job\_openings\_finance\_qoq\_pct | Quarterly growth percentage of job openings in finance | LinkedIn |
| job\_openings\_finance\_six\_months\_growth\_pct | Six months growth percentage of job openings in finance | LinkedIn |
| job\_openings\_human\_resource\_qoq\_pct | Quarterly growth percentage of job openings in human resources | LinkedIn |
| job\_openings\_human\_resource\_six\_months\_growth\_pct | Six months growth percentage of job openings in human resources | LinkedIn |
| job\_openings\_information\_technology\_qoq\_pct | Quarterly growth percentage of job openings in information technology | LinkedIn |
| job\_openings\_information\_technology\_six\_months\_growth\_pct | Six months growth percentage of job openings in information technology | LinkedIn |
| job\_openings\_marketing\_qoq\_pct | Quarterly growth percentage of job openings in marketing | LinkedIn |
| job\_openings\_marketing\_six\_months\_growth\_pct | Six months growth percentage of job openings in marketing | LinkedIn |
| job\_openings\_media\_and\_communication\_qoq\_pct | Quarterly growth percentage of job openings in media and communication | LinkedIn |
| job\_openings\_media\_and\_communication\_six\_months\_growth\_pct | Six months growth percentage of job openings in media and communication | LinkedIn |
| job\_openings\_operations\_qoq\_pct | Quarterly growth percentage of job openings in operations | LinkedIn |
| job\_openings\_operations\_six\_months\_growth\_pct | Six months growth percentage of job openings in operations | LinkedIn |
| job\_openings\_research\_qoq\_pct | Quarterly growth percentage of job openings in research | LinkedIn |
| job\_openings\_research\_six\_months\_growth\_pct | Six months growth percentage of job openings in research | LinkedIn |
| job\_openings\_sales\_qoq\_pct | Quarterly growth percentage of job openings in sales | LinkedIn |
| job\_openings\_sales\_six\_months\_growth\_pct | Six months growth percentage of job openings in sales | LinkedIn |
| job\_openings\_product\_management\_qoq\_pct | Quarterly growth percentage of job openings in product management | LinkedIn |
| job\_openings\_product\_management\_six\_months\_growth\_pct | Six months growth percentage of job openings in product management | LinkedIn |
| job\_openings\_overall\_qoq\_pct | Quarterly growth percentage of overall job openings | LinkedIn |
| job\_openings\_overall\_six\_months\_growth\_pct | Six months growth percentage of overall job openings | LinkedIn |

### Total Job Listings

| Column Name | Description | Source |
| --- | --- | --- |
| job\_openings\_title | Current job opening titles at the company | LinkedIn |
| job\_openings\_count | The total count of current job openings at the company | LinkedIn |
| job\_openings\_count\_mom\_pct | The percentage change in the number of job openings at the company on a month-over-month basis | LinkedIn |
| job\_openings\_count\_qoq\_pct | The percentage change in the number of job openings at the company on a quarter-over-quarter basis | LinkedIn |
| job\_openings\_count\_yoy\_pct | The percentage change in the number of job openings at the company on a year-over-year basis | LinkedIn |

### Ads

| Column Name | Description | Source |
| --- | --- | --- |
| meta\_total\_ads | Total Ads during the lifetime of the company | Meta |
| meta\_active\_ads | Currently active Ads by the company | LinkedIn |
| meta\_ad\_url | URL of company’s page on Meta Ads Library | LinkedIn |

### SEO and Google Search Ranking

| Column Name | Description | Source |
| --- | --- | --- |
| average\_organic\_rank | Average rank of company domain on keywords for which it ranks in top 100 results | Spyfu |
| monthly\_paid\_clicks | Estimated number of clicks on website from Google Ads | Spyfu |
| monthly\_organic\_clicks | Estimated number of clicks on website from organic search results | Spyfu |
| average\_ad\_rank | Average position of all the company domain’s ad | Spyfu |
| total\_organic\_results | Number of keywords for which the company domain appears in organic search result | Spyfu |
| monthly\_google\_ads\_budget | Monthly budget in USD of google ads campaigns | Spyfu |
| monthly\_organic\_value | A rollup of all of company domain’s organic keywords and their collective value that their clicks bring in. In USD ​ | Spyfu |
| total\_ads\_purchased | Total number of keywords on which company’s domain has advertised on. | Spyfu |
| lost\_ranks | Number of keywords on which company’s domain dropped its rank this month in search result while still being in top 100 | Spyfu |
| gained\_ranks | Number of keywords on which company’s domain improved its rank this month in search result while still being in top 100 | Spyfu |
| newly\_ranked | Number of keywords on which atleast one of the company’s domain’s page started ranking in top 100 for the first time this month | Spyfu |
| paid\_competitors | Domains that are competing for the same paid keywords/clicks | Spyfu |
| organic\_competitors | Domains that are competing for the same organic keywords | Spyfu |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

### Google Search Impression

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| num\_of\_impressions | Number of times company is searched on Google | Google | Yes |
| num\_of\_impressions\_mom\_growth | Monthly growth of number of times company is searched on Google | Google |  |
| num\_of\_impressions\_qoq\_growth | Quarterly growth of number of times company is searched on Google | Google |  |
| num\_of\_impressions\_yoy\_growth | Yearly growth of number of times company is searched on Google | Google |  |

### Twitter Followers

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| followers | Number of followers on company’s Twitter handle | Twitter | Yes |
| followers\_mom\_growth | Monthly growth of Twitter followers | Twitter |  |
| followers\_qoq\_growth | Quarterly growth of Twitter followers | Twitter |  |
| followers\_yoy\_growth | Yearly growth of Twitter followers | Twitter |  |
| founder\_handles | Twitter handles of founders | Twitter |  |
|  |  |  |  |

### Twitter Posts

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| post\_content | Content of the post on Twitter by the Company | Twitter |  |
| date\_posted | Date of the Twitter post | Twitter | Yes |
| likes | Number of likes of the post | Twitter | Yes |
| retweets | Number of retweets of the post | Twitter | Yes |
| comments | Number of comments on the post | Twitter | Yes |

### LinkedIn Posts

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| post\_content | Content of the post on LinkedIn by the Company | LinkedIn |  |
| date\_posted | Date of the LinkedIn post | LinkedIn | Yes |
| likes | Number of likes of the post | LinkedIn | Yes |
| reposts | Number of reposts of the post | LinkedIn | Yes |
| comments | Number of comments on the post | LinkedIn | Yes |
| reactors | List of full person/company profile of the entity reacting to the post. Each profile covers these [fields](/c265aa415fda41cb871090cbf7275922?pvs=25#86ee5d334f6e478db823cd230fdc980f). | Linkedin |  |

### News Articles

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| title | Title of article | News publisher |  |
| article\_link | Website link of the article | News publisher |  |
| publisher\_name | Name of the news publisher | News publisher |  |
| date\_published | Date the article was first published by the news publisher | News publisher |  |
| one\_line\_description | One line description of the content of the article |  |  |

### Form D Filings

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| total\_amount | Total offering amount in USD | SEC EDGAR | Yes |
| date\_filed | Date FORM D was filed | SEC EDGAR |  |
| date\_of\_first\_sale | Date of sale of the security | SEC EDGAR |  |
| accession\_no | SEC Accession No | SEC EDGAR |  |
| file\_no | SEC File No | SEC EDGAR |  |

## People

### Profile and Background

| Column Name | Description | Source | Time Series Available |
| --- | --- | --- | --- |
| linkedin\_profile\_url | Linkedin profile url of the person. Example: https://www.linkedin.com/in/ACwAAAVhcDEBbTdJtuc-KHsdYfPU1JAdBmHkh8I | LinkedIn |  |
| linkedin\_flagship\_url | Linkedin profile url in readable format. Example: https://www.linkedin.com/in/jon-doe | LinkedIn |  |
| name | Name of the person | LinkedIn |  |
| email | Email of the person | LinkedIn |  |
| title | Title of the person at the current job | LinkedIn |  |
| headline | Headline of the person on their Linkedin profile | LinkedIn |  |
| summary | Summary of the person on their Linkedin profile | LinkedIn |  |
| num\_of\_connections | Number of connections the person has on their LinkedIn profile | LinkedIn |  |
| skills | All the skills the person has listed on their LinkedIn profile | LinkedIn |  |
| twitter\_handle | Twitter handle shared by the person on their Linkedin profile | LinkedIn |  |
| languages | The languages the person speaks as listed on their LinkedIn profile | LinkedIn |  |
| all\_employers | List of all employers the person has worked for | LinkedIn |  |
| all\_employers\_company\_id | Crustdata company IDs corresponding to each employer | LinkedIn |  |
| all\_titles | List of all job titles the person has held | LinkedIn |  |
| all\_schools | List of all schools the person attended | LinkedIn |  |
| all\_degrees | List of all degrees obtained by the person | LinkedIn |  |

