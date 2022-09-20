from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    
    #example simple API call
    query = {"lat":"45", "lon":"180"}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    
    # Runtime scanner BEFORE API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/a2e75629-3853-11ed-b99b-028b315293dd/ses/a5d54d01-3853-11ed-b99b-028b315293dd/log_service_endpoint_before'
    myobj = {"url": "http://api.open-notify.org/iss-pass.json", "headers": str(headers), "method":"GET", "request_body":str(query)}
    x = requests.post(url, json = myobj)

    # Target API request
    response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
    
    # Runtime scanner AFTER API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/a2e75629-3853-11ed-b99b-028b315293dd/ses/a5d54d01-3853-11ed-b99b-028b315293dd/log_service_endpoint_after'
    myobj = {"url": "http://api.open-notify.org/iss-pass.json", "http_response_code": response.status_code, "response":response.text}
    x = requests.post(url, json = myobj)
    
    #example variable name, assigned to value in code
    # Enter your API key here
    api_key = "0c0e734e8658fca29d68ceef3cdedb0c"
    # Give city name
    city_name = "Denver"
    # complete_url variable to store
    # complete url address
    complete_url = "http://api.openweathermap2.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + city_name
    # get method of requests module
    # return response object
    
    # Runtime scanner BEFORE API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/a2e75629-3853-11ed-b99b-028b315293dd/ses/a5ddbd8c-3853-11ed-b99b-028b315293dd/log_service_endpoint_before'
    myobj = {"url": complete_url, "headers": str(headers), "method":"GET", "request_body":"appid=" + api_key + "&q=" + city_name}
    x = requests.post(url, json = myobj)
    
    response = requests.get(complete_url)

    # Runtime scanner AFTER API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/a2e75629-3853-11ed-b99b-028b315293dd/ses/a5ddbd8c-3853-11ed-b99b-028b315293dd/log_service_endpoint_after'
    myobj = {"url": complete_url, "http_response_code": response.status_code, "response":response.text}
    x = requests.post(url, json = myobj)
    
    #example variable name, assigned value in code
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "b006e118ff5b4f2aa356e3a7ee31d802"
    }
    main_url = "https://newsapi.org/v1/articles"
    
    # Runtime scanner BEFORE API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/a2e75629-3853-11ed-b99b-028b315293dd/ses/a5e3fa49-3853-11ed-b99b-028b315293dd/log_service_endpoint_before'
    myobj = {"url": main_url, "headers": str(headers), "method":"GET", "request_body":query_params}
    x = requests.post(url, json = myobj)
    
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    
    # Runtime scanner AFTER API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/a2e75629-3853-11ed-b99b-028b315293dd/ses/a5e3fa49-3853-11ed-b99b-028b315293dd/log_service_endpoint_after'
    myobj = {"url": main_url, "http_response_code": res.status_code, "response":res.text}
    x = requests.post(url, json = myobj)
    
    open_bbc_page = res.json()
    # getting all articles in a string article
    article = open_bbc_page["articles"]
    # empty list which will
    # contain all trending news
    results = []
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])
    
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(ssl_context='adhoc', host='0.0.0.0',port=5000)
