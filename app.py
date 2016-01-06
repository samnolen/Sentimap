#from TwitterSearch import *
from twitter import *
import auth
import sys
import csv

@app.route('/')
def main():
  return redirect('/index')


latitude = 36.5333
longitude = -82.5500
max_range = 300 # kilometers
num_results = 10
outfile = "output.csv"

lst = ['#StarWars']

twitter = Twitter(auth=OAuth(auth.at, auth.ats, auth.ck, auth.cs))

csvfile = file(outfile, "w")
csvwriter = csv.writer(csvfile)
row = ["user", "test", "latitude", "longitude"]
csvwriter.writerow(row)
result_count = 0
last_id = None
while result_count < num_results:
  query = twitter.search.tweets(q = lst[0], geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
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

print "written to %s" % outfile



@app.route('/index', methods=['GET', 'POST'])
def index():
  if request.method == 'GET': 
    return render_template('index.html')
  else: # request.method == 'POST'
    app.vars['stock'] = request.form['ticker']
    app.vars['choice'] = request.form['features']
    #r = Quandl.get("WIKI/"+app.vars['stock'], returns=pandas)
    j = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/' + app.vars['stock'] +'.csv?api_key=sJN4VTedn6CE_mZ-6LrM')
    jprime = j.content
    r = pandas.read_csv(StringIO(jprime))
    now = time.time()
    num_points = r.shape[0]
    dt = 24*3600 # days in seconds
    dates = np.linspace(now, now + num_points*dt, num_points) * 1000 # times in ms
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    #output_file("plot.html", title = app.vars['stock']+" prices")
    f = figure(x_axis_label='date', x_axis_type="datetime",tools=TOOLS)
    f.line(dates, r[app.vars['choice']], color='#1F78B4', legend=app.vars['stock'])
    script, div = components(f)
    return render_template('result.html', script=script, div = div, stock = app.vars['stock'])


@app.route('/result', methods=['GET'])
def result():
  return render_template('result.html')

if __name__ == '__main__':
  app.run(port=5000, debug=True)