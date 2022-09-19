from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    
    #example simple API call
    query = {'lat':'45', 'lon':'180'}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    
    # Runtime scanner BEFORE API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/58c234e0-35d5-11ed-b99b-028b315293dd/ses/5b34287c-35d5-11ed-b99b-028b315293dd/log_service_endpoint_before'
    myobj = {"url": "http://api.open-notify.org/iss-pass.json", "headers": headers, "method":"GET", "request_body":query}
    x = requests.post(url, json = myobj)

    # Target API request
    response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
    
    # Runtime scanner AFTER API request
    url = 'https://portaleast.riscosity.com/api/v1/rtscanner/organizations/94073c7a-0533-11ec-b635-3dca3bca46fd/products/447e3cb3-35d5-11ed-b99b-028b315293dd/repos/58c234e0-35d5-11ed-b99b-028b315293dd/ses/5b34287c-35d5-11ed-b99b-028b315293dd/log_service_endpoint_after'
    myobj = {"url": "http://api.open-notify.org/iss-pass.json", "headers": headers, "http_response_code": response.status_code, "response":response.text, "request_body":{}}
    x = requests.post(url, json = myobj)
    
    #example variable name, assigned to value in code
    # Enter your API key here
    api_key = "0c0e734e8658fca29d68ceef3cdedb0c"
    # Give city name
    city_name = "Denver"
    # complete_url variable to store
    # complete url address
    complete_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + city_name
    # get method of requests module
    # return response object
    response = requests.get(complete_url)

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
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
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
