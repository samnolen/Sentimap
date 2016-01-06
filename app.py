#from TwitterSearch import *
from twitter import *
from flask import Flask, render_template, request, redirect, send_from_directory
import auth
import sent
import sys, csv

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
    max_range = 20 # kilometers
    num_results = 10
    outfile = "output.csv"
    search = request.form['key']
    twitter = Twitter(auth=OAuth(auth.at, auth.ats, auth.ck, auth.cs))
    csvfile = file(outfile, "w")
    csvwriter = csv.writer(csvfile)
    row = ["user", "text", "latitude", "longitude"]
    csvwriter.writerow(row)
    result_count = 0
    last_id = None
    while result_count < num_results:
      query = twitter.search.tweets(q = search, geocode = "%f,%f,%dkm" % (
        app.vars['latitude'], app.vars['longitude'], max_range), count = 100, max_id = last_id)
      for result in query["statuses"]:
        if result["geo"]:
          user = result["user"]["screen_name"]
          text = result["text"]
          text = text.encode('ascii', 'replace')
          latitude = result["geo"]["coordinates"][0]
          longitude = result["geo"]["coordinates"][1]
          row = [user, text, latitude, longitude]
          csvwriter.writerow(row)
          result_count = result_count + 1
        last_id = result["id"]
      print "got %d results" % result_count
    csvfile.close()
    v = 0
    a = 0
    d = 0
    with open('output.csv', 'rb') as csvfile:
      myreader = csv.reader(csvfile)
      for row in myreader:
        sentiment_score = sent.sent(row[1])
        v += sentiment_score[0]
        a += sentiment_score[1]
        d += sentiment_score[2]
    v = v/float(result_count)
    a = a/float(result_count)
    d = d/float(result_count)
    return render_template('result.html', val = v, aro = a, dom = d)


@app.route('/result', methods=['GET'])
def result():
  return render_template('result.html')

if __name__ == '__main__':
  app.run(port=5000, debug=True)