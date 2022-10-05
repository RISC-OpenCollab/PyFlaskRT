from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    
    #example simple API call with simple params
    query = {"lat":"45", "lon":"180"}
    headers = {"Content-Type": "application/json; charset=utf-8"}

    # Runtime scanner BEFORE API request
    url = 'https://riscosity.divvyeng.com/api/v1/rtscanner/organizations/31b0b95a-f274-11ec-af7f-42010a1a0104/products/130972d5-44f0-11ed-ad5f-42010a1a0106/repos/2aad8432-44f0-11ed-ad5f-42010a1a0106/ses/2e90e58f-44f0-11ed-ad5f-42010a1a0106/log_service_endpoint_before'
    myobj = {"url": "http://api.open-notify.org/iss-pass.json", "headers": str(headers), "method":"GET", "request_body":str(query)}
    x = requests.post(url, json = myobj)
    
    # Target API request to api.open-notify.org endpoint
    response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
    
    # Runtime scanner AFTER API request
    url = 'https://riscosity.divvyeng.com/api/v1/rtscanner/organizations/31b0b95a-f274-11ec-af7f-42010a1a0104/products/130972d5-44f0-11ed-ad5f-42010a1a0106/repos/2aad8432-44f0-11ed-ad5f-42010a1a0106/ses/2e90e58f-44f0-11ed-ad5f-42010a1a0106/log_service_endpoint_after'
    myobj = {"url": "http://api.open-notify.org/iss-pass.json", "http_response_code": response.status_code, "response":response.text}
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
