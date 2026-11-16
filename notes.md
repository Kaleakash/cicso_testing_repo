

https://www.google.com ----> URL 

                req(http/https)------->
Client                                      Server 
                <-----res(http/https)               HTML 
                                                    CSS
                                                and framework 
                                                JavaScript 

Frontend                                        Backend 
html,               API                         java with spring boot
css,                                            python with fastapi
js                                              node js with express js 
js library and framework 
react js or angular framework 
                        Web Application 
App1                                             App2 
                        java (req)
Java                    XML/JSON                 Python 
                        python(res)
    SOAP Web Service 
    Rest Full Web Service 

Get method 

URL                 -----> get all resources details 

URL?status=offline    ---> query param 

URL/offline         ----> path param (append value directly )

employees[0].skillSet[1]
employees[0].projects[0].tech 
{
    "employees":[
{
    "id":100,
    "name":"Ravi",
    "age":21,
    "isActive:true,
    "skillSet":["Java","Python","AI"],
    "projects":[
        {"pid":1234,"tech":"Java"},
        {"pid":4567,"tech":"Python"}
    ]
},
{
    "id":101,
    "name":"Reeta",
    "age":22,
    "isActive:false,
    "skillSet":["HTML","CSS","React","Angular Framweork"],
    "projects":[
        {"pid":1237,"tech":"React JS"},
        {"pid":4568,"tech":"Angular Framework"}
    ]
}
]
}