#from TwitterSearch import *
from twitter import *
from cartodb import CartoDBAPIKey, CartoDBException, FileImport
from flask import Flask, render_template, request, redirect, send_from_directory
import execjs
import auth
from bokeh.io import hplot, output_file, show
from bokeh.plotting import figure
from bokeh.embed import components
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import scipy.special
import sent
import sys, csv
from subprocess import call

###
### CARTODB API KEY: 24b3f4810d68e1f8e9c3f17c0580181b4e034edb
###


my_cartodb_domain = 'https://samnolen.cartodb.com'
my_cartodb_url = 'https://samnolen.cartodb.com/api/v1/imports/?api_key='
my_cartodb_api_key = '24b3f4810d68e1f8e9c3f17c0580181b4e034edb'
cl = CartoDBAPIKey(my_cartodb_api_key, my_cartodb_domain)


app = Flask(__name__)
app.vars = {}
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
  if request.method == 'GET': 
    return render_template('index.html')
  else:
    cities = [['Seattle', 47.61, -122.333]]
    cities.append(['San Francisco', 37.78, -122.417])
    cities.append(['Los Angeles', 34.05, -118.25])
    cities.append(['Chicago', 41.837, -87.685])
    cities.append(['Dallas', 32.7767, -96.80])
    cities.append(['Atlanta', 33.755, -84.39])
    cities.append(['New York', 40.79, -73.96])
    cities.append(['Washington D.C.', 38.905, -77.016])
    cities.append(['Boston', 42.36, -71.06])
    cities.append(['Miami', 25.775, -80.21])
    app.vars['city'] = request.form['city']
    if app.vars['city'] == 'Chicago':
      app.vars['latitude'] = 41.837
      app.vars['longitude'] = -87.685
    if app.vars['city'] == 'LosAngeles':
      app.vars['latitude'] = 34.05
      app.vars['longitude'] = -118.25
    if app.vars['city'] == 'NewYork':
      app.vars['latitude'] = 40.79
      app.vars['longitude'] = -73.96
    if app.vars['city'] == 'SanFrancisco':
      app.vars['latitude'] = 37.78
      app.vars['longitude'] = -122.417
    max_range = 500 # kilometers
    num_results = 20
    outfile = "outputpa.csv"
    search = request.form['key']
    twitter = Twitter(auth=OAuth(auth.at, auth.ats, auth.ck, auth.cs))
    csvfile = file(outfile, "w")
    csvwriter = csv.writer(csvfile)
    row = ["user", "text", "latitude", "longitude", "v", "a", "d"]
    csvwriter.writerow(row)
    total_result_count = 0
    last_id = None
    
    vlist = []
    alist = []
    dlist = []
    for city in cities:
      result_count = 0
      tried = 0
      while tried == 0:
      #while result_count == 0:
      #while result_count < num_results:
        tried = 1
        app.vars['latitude'] = city[1]
        app.vars['longitude'] = city[2]
        query = twitter.search.tweets(q = search, geocode = "%f,%f,%dkm" % (
          app.vars['latitude'], app.vars['longitude'], max_range), count = 100)
        for result in query["statuses"]:
          if result["geo"]:
            result_count +=1
            total_result_count +=1
            user = result["user"]["screen_name"]
            text = result["text"]
            text = text.encode('ascii', 'replace')
            latitude = result["geo"]["coordinates"][0]
            longitude = result["geo"]["coordinates"][1]
            sentiment_score = sent.sent(text)
            v = sentiment_score[0]
            a = sentiment_score[1]
            d = sentiment_score[2]
            row = [user, text, latitude, longitude, v, a, d]
            vlist.append(v)
            alist.append(a)
            dlist.append(d)
            csvwriter.writerow(row)
            last_id = result["id"]
    print "got %d results" % total_result_count
    csvfile.close()
    #command = 'curl -v -F file=@/Users/samnolen/DataIncubatorProject/outputsw.csv "' + my_cartodb_url + my_cartodb_api_key + '"'
    #call([command], shell=True)
    #print(cl)
    #fi = FileImport("output.csv", cl)
    #fi.run()
    # - now create map - #
    #make_map = execjs.compile("""
    #    var mapconfig = {
    #      "version": "1.3.1",
    #      "layers": [{
    #        "type": "cartodb",
    #        "options": {
    #          "cartocss_version": "2.1.1",
    #          "cartocss": "#layer { polygon-fill: #FFF; }",
    #          "sql": "select * from european_countries_e"
    #        }
    #      }]
    #    }

    #    $.ajax({
    #      crossOrigin: true,
    #      type: 'POST',
    #      dataType: 'json',
    #      contentType: 'application/json',
    #      url: 'https://samnolen.cartodb.com/api/v1/map',
    #      data: JSON.stringify(mapconfig),
    #      success: function(data) {
    #        var templateUrl = 'https://samnolen.cartodb.com/api/v1/map/' + data.layergroupid + '/{z}/{x}/{y}.png'
    #        console.log(templateUrl);
    #      }
    #    })
    #""")
    #make_map.call()
    
    #bins = np.arange(0, 10, 0.25)
    #plt.hist(vlist, bins=bins, alpha=0.5)
    #plt.title('Valence')
    #plt.show()
    p1 = figure(title="Valence",tools="save",
           background_fill="#E8DDCB")
    hist1, edges1 = np.histogram(vlist, density=True, bins=50)
    p1.quad(top=hist1, bottom=0, left=edges1[:-1], right=edges1[1:],
         fill_color="#036564", line_color="#033649")
    p2 = figure(title="Arousal",tools="save",
           background_fill="#E8DDCB")
    hist2, edges2 = np.histogram(vlist, density=True, bins=50)
    p2.quad(top=hist2, bottom=0, left=edges2[:-1], right=edges2[1:],
         fill_color="#036564", line_color="#033649")
    p3 = figure(title="Dominance",tools="save",
           background_fill="#E8DDCB")
    hist3, edges3 = np.histogram(vlist, density=True, bins=50)
    p3.quad(top=hist2, bottom=0, left=edges3[:-1], right=edges3[1:],
         fill_color="#036564", line_color="#033649")
    tri = gridplot([[p1, p2, p3]])
    script, my_plot_div = components(tri)
    return render_template('result.html', script = script, div=my_plot_div)

@app.route('/result', methods=['GET'])
def result():
  return render_template('result.html')

if __name__ == '__main__':
  app.run(port=5000, debug=True)