import dill as dl
import json
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn
import sent
import sklearn.ensemble as en
import sklearn.linear_model as ln
import sklearn.neighbors as knn
import sklearn.pipeline as pipe


usatoday = {}
usatoday['hyundai'] = 6.19 # 6.27, 6.90
usatoday['heinz'] = 6.63
usatoday['doritos'] = 6.60 # 6.48
usatoday['honda'] = 6.13
usatoday['audi'] = 6.04
usatoday['budweiser_helen_mirren'] = 6.01
usatoday['toyota_prius'] = 5.97
usatoday['universal'] = 5.91
usatoday['super_bowl_babies'] = 5.71
usatoday['jeep'] = 5.70
usatoday['amazon_echo'] = 5.63
usatoday['kia_optima'] = 5.61
usatoday['snickers'] = 5.60
usatoday['avocados'] = 5.52
usatoday['marmot'] = 5.40
usatoday['coca-cola'] = 5.38
usatoday['colgate'] = 5.31
usatoday['budweiser'] = 5.30
usatoday['t_mobile'] = 5.28
usatoday['jeep_4x4ever'] = 5.21
usatoday['skittles'] = 5.19
usatoday['jungle_book'] = 5.19
usatoday['budweiser2'] = 5.08
usatoday['apartments'] = 5.06
usatoday['buick'] = 5.04
usatoday['pepsi'] = 4.96
usatoday['t_mobile_drake'] = 4.81
usatoday['lg_oled_tv'] = 4.74
usatoday['independence_day'] = 4.74
usatoday['advil'] = 4.73
usatoday['wix'] = 4.72
usatoday['shock_top'] = 4.63
usatoday['xmen_apocalypse'] = 4.59
usatoday['pokemon'] = 4.47
usatoday['schick_hydro'] = 4.43
usatoday['taco_bell_quesalupa'] = 4.42
usatoday['fitbit'] = 4.39
usatoday['acura'] = 4.37
usatoday['paypal'] = 4.33
usatoday['dollar_shave_club'] = 4.19
usatoday['rocket_mortgage'] = 4.18
usatoday['butterfinger'] = 4.15
usatoday['michelob'] = 4.11
usatoday['kickstart'] = 3.90
usatoday['mobile_strike'] = 3.56
usatoday['squarespace'] = 3.56
usatoday['sofi'] = 3.55
usatoday['xifaxan'] = 3.30
usatoday['jublia'] = 3.22

"""

# 49 total keys

sample = random.sample(xrange(len(usatoday.keys())), 30)

training = {}
test = {}

for i in xrange(0, len(usatoday.keys())):
    if i in sample:
        training[usatoday.keys()[i]] = usatoday[usatoday.keys()[i]]
    else:
        test[usatoday.keys()[i]] = usatoday[usatoday.keys()[i]]
"""


X1 = []
X2 = []
X3 = []
Y = []
big_list = []


company_name_lst = []
for f in os.listdir(os.getcwd() + '/super'):
    filename = f
    company = filename[:-4]
    #company_sentiment = [0,0,0]
    if company in usatoday.keys():
        company_name_lst.append(company)
"""
        Y.append(usatoday[company])
        with open('super/' + filename, 'rb') as file:
            tweets = file.readlines()
            n = 0
            for tweet in tweets:
                try:
                    this_sent = sent.sent(json.loads(tweet)['text'])
                    for i in xrange(0,3):
                        #company_sentiment[i] += this_sent[i]
                        #n += 1
                        # option 1: aggregated
                        # company_sentiment[i] = company_sentiment[i]/float(n)
                        # option 2: full model
                        big_list.append(company)
                        big_list += this_sent
                        big_list.append(usatoday[company])
                except:
                    pass
        print company
        #print company_sentiment
        #if company in usatoday.keys():
        # option 1: aggregated
        X1.append(company_sentiment[0])
        X2.append(company_sentiment[1])
        X3.append(company_sentiment[2])
        Y.append(usatoday[company])
        """
        # option 2: full model



"""
X1 = [4.850191761491301, 5.128784400731498, 5.1073770034309245, 4.807283233148616, 4.841556246273983, 4.62775071256573, 5.824337008297369, 5.120754289304175, 4.9916589987339695, 4.991208733027657, 5.014477513227512, 5.467511436453121, 5.684302736687291, 4.497832266440429, 5.454586392020981, 4.123453963951898, 4.842053369788103, 6.236198589067371, 5.568234414606117, 5.457544244803185, 4.534572529809373, 6.177301552205711, 5.316655901467438, 4.695878697986105, 4.945146355765448, 5.5325363119192374, 5.164189607572461, 5.029341007289669, 5.241457008994326, 5.228400354301234, 4.65795281036625, 5.128078232674456, 5.170862698412699, 4.909989915439558, 4.957860950095578, 5.309125850340137, 4.877081361607132, 5.645921591716988, 5.419178476877809, 5.114095127863422, 5.3618327561327614, 4.6672640913565315, 4.717774003333884]
X2 = [3.6903857520358123, 3.9640117239999313, 3.8291538695439056, 3.8569652993018373, 3.686370380548771, 3.5478118949334094, 3.971656071366781, 3.926333120263641, 3.7694039945197204, 3.7251135453247577, 3.8907159024103475, 3.8996606593953587, 3.9752032269351667, 3.751729521532531, 4.0291869330067005, 3.280225496519816, 3.931495640996426, 4.12058675042192, 4.086889319830975, 4.048529722200373, 3.6534288738621474, 3.854430563575285, 3.874300649988706, 4.0484270189515374, 3.7650716139752443, 3.7489003768060947, 3.9596155019360015, 4.239529615638993, 4.18243026567131, 3.8130796431997593, 3.6265845413010305, 4.180163712497891, 3.9022253968253975, 3.8659072408197948, 3.9321775222305346, 3.8222215136054416, 3.6486023685515896, 3.751946381714359, 3.9709132185769653, 3.9869437807141814, 3.837722842555988, 3.953460313824845, 4.180296334838668]
X3 = [4.602652366571385, 5.070908266521043, 4.840269498043588, 4.7979580437368945, 4.598764871880626, 4.56546996166888, 5.48343390222465, 5.041869101892279, 4.769759610679307, 4.828393589133031, 4.999423029705711, 5.390640680936692, 5.270541681170573, 4.406111513261826, 5.216155231020052, 3.9946997467088736, 4.871716524265209, 5.813545446662127, 5.302818318526564, 5.146299381494493, 4.6465703612385925, 5.476362601231373, 5.2430256512535545, 4.786051780771385, 4.792933966942143, 5.694459960848254, 5.049981534433264, 4.996138429196461, 5.044576627849758, 5.240756416922602, 4.529366028802429, 5.083581455665012, 5.000639417989418, 4.80481321718307, 4.894035818166691, 5.132062925170067, 4.801378624131947, 5.498462309245511, 5.442579739953894, 5.030576302210669, 5.065277889139844, 4.7054141405752, 4.329673604387978]
Y = [4.37, 4.73, 5.63, 5.06, 6.04, 5.52, 5.3, 5.08, 6.01, 5.04, 4.15, 5.31, 4.19, 6.6, 4.39, 6.63, 6.9, 4.74, 5.7, 5.21, 3.22, 5.19, 5.61, 3.9, 4.74, 5.4, 4.11, 3.56, 4.33, 4.96, 4.47, 4.18, 4.43, 5.19, 5.6, 3.55, 3.56, 5.71, 4.81, 5.97, 4.72, 3.3, 4.59]
"""


P1 = []
P2 = []
P3 = []
Q = []


"""
sum_cv_squared_errors = 0
N = len(big_list)
new_array = np.asarray(big_list)
new_array.shape = (len(big_list)/5, 5)
why = np.asarray(new_array[:, [4]])
why.shape = (N/5,)

print len(company_name_lst)
print type(new_array)
print new_array.shape
"""

#for i in xrange(0, len(company_name_lst)):
    # do leave-one-out CV at spot i
    # option 1: aggregated
"""
    new_array = []
    for j in xrange(0, len(X1)):
        if j != i:
            new_array.append(X1[j])
            new_array.append(X2[j])
            new_array.append(X3[j])
            new_array.append(Y[j])          
    new_array = np.asarray(new_array)
    new_array.shape = (len(X1)-1, 4)
    why = np.asarray(new_array[:, [3]])
    why.shape = (42,)
    # option 2: full model
    training_array = new_array[new_array[:,0] != company_name_lst[i]]
    training_target = np.asarray(training_array[:, [4]]).astype(np.float)
    training_target.shape = (training_array.shape[0],)
    training_data = training_array[:, [1,2,3]].astype(np.float)
    test_array = new_array[new_array[:,0] == company_name_lst[i]]
    test_data = test_array[:, [1,2,3]].astype(np.float)
    my_ln = ln.LinearRegression(fit_intercept=True)
    my_ln.fit(training_data, training_target)
    one_out_prediction1 = my_ln.predict(test_data)
    P1.append(np.mean(one_out_prediction1.astype(np.float)))
    my_rand = en.RandomForestRegressor()
    my_rand.fit(training_data, training_target)
    one_out_prediction2 = my_rand.predict(test_data)
    P2.append(np.mean(one_out_prediction2.astype(np.float)))
    my_knn = knn.KNeighborsRegressor()
    my_knn.fit(training_data, training_target)
    one_out_prediction3 = my_knn.predict(test_data)
    P3.append(np.mean(one_out_prediction3.astype(np.float)))
    Q.append(Y[i])
"""
    #sum_cv_squared +=

"""
print 'P1'
print P1
print 'P2'
print P2
print 'P3'
print P3
print 'Q'
print Q
"""


#rev_ar = []
#for elt in X2:
#    rev_ar.append(3*(-elt + 9)-10)

#Z = []
#sum_cv_squared_errors = 0
"""
for i in xrange(0, 43):
    # do leave-one-out CV at spot i
    # option 1: aggregated
    new_array = []
    for j in xrange(0, len(X1)):
        if j != i:
            new_array.append(X1[j])
            new_array.append(X2[j])
            new_array.append(X3[j])
            new_array.append(Y[j])          
    new_array = np.asarray(new_array)
    new_array.shape = (len(X1)-1, 4)
     option 2: full model
    N = len(big_list)
    new_array = np.asarray(big_list)
    new_array.shape = (len(big_list)/4, 4)
    why = np.asarray(new_array[:, [3]])
    why.shape = (N,)
    estimators = [('linear', ln.LinearRegression()), ('random_forest', en.RandomForestRegressor()),
        ('nearest_neighbors', knn.KNeighborsRegressor())]
    est_union = pipe.FeatureUnion(estimators)
    est_union.fit(new_array[:, [0,1,2]], why)
    z = est_union.predict(np.asarray([X1[i], X2[i], X3[i]]))
    """
    
    #Z.append(z)
    #sum_cv_squared +=

#print np.corrcoef(list(Z), list(Y))[0,1]

#for i in xrange(0, len(X1)):


P1 = [5.2381500821338065, 5.2192745020963098, 5.2162306932138405, 5.2150529473157787, 5.1819539800162291, 5.2241942689049052, 5.223764873836072, 5.2236792177710436, 5.1632955368717202, 5.2274388785554669, 5.2175867458677656, 5.2126316324237001, 5.2385877808853651, 5.1854789667208907, 5.2238534297523334, 5.1620657430828816, 5.1991305219601367, 5.2588450576448427, 5.2033526800872947, 5.2229065052946071, 5.2260116591657839, 5.2517190506282923, 5.2087361974350399, 5.2289493468796149, 5.2270344677087364, 5.1895539856521777, 5.2204480710600878, 5.2102016182883846, 5.2227916607978795, 5.2191306818190348, 5.3173720705801486, 5.2452750683798444, 5.220490349155666, 5.2192039999494328, 5.2109982662175893, 5.2235337668957023, 5.2438717347778203, 5.2045490989937315, 5.228318303765584, 5.1487305966281394, 5.2305010481734051, 5.2377367722148866, 5.2597563239824794]
P2 = [5.2868286374296503, 5.1618513346709207, 5.1945448897375508, 5.2472105364008401, 5.1664681975409721, 5.3112032438793584, 5.1413676717100625, 5.3505800963751691, 5.1392957151506122, 5.2274416151643095, 5.2200192238415353, 5.2316560714214262, 5.2159410581459484, 5.2133237637770025, 5.2023390364379303, 5.1853841543624153, 5.1314075167205466, 5.2394950504554574, 5.1696450402889607, 5.3633427409735663, 5.2011793247407665, 5.3489298317343144, 5.205169863759421, 5.2775469724854371, 5.1764260623077218, 5.4815126773808922, 5.24659857425016, 5.0849749822532306, 5.2374354870040607, 5.2136320668257401, 5.3485680192343104, 5.2182386456648375, 5.1932325154876091, 5.180699882044526, 5.2648125203336278, 5.1531497400289208, 5.2623939712360519, 5.1425543008166219, 5.1251457092354729, 5.1360362199281147, 5.2463160707174001, 5.1967221611746863, 5.1374124567089972]
P3 = [5.2992185730464323, 5.1131736954967826, 5.0705700189753324, 5.3208737672583828, 5.0689854545454542, 5.1488297213622296, 5.1403942532576004, 5.2920890145876749, 5.078707544723879, 5.162770098730606, 5.1693246187363835, 5.1630275154004099, 5.1974504249291789, 5.2482452568255429, 5.2254922480620154, 5.1354603409933288, 5.0308400000000004, 5.2602843182875754, 5.1292172824045084, 5.3558647573587912, 5.2051090225563907, 5.2667282084271472, 5.1941698440207977, 5.2658207979071285, 5.0942254545454544, 5.4566867193474389, 5.1936702819956615, 5.0062440476190471, 5.1960537313432829, 5.131562214321991, 5.1577192245248789, 5.2503497522588169, 5.0972333333333335, 5.0856753224419613, 5.2177225130890053, 5.0763214285714282, 5.1844671875000001, 5.0842765249537889, 5.1425735660847876, 5.088956348216513, 5.0723086956521737, 5.2085348837209295, 5.1172102480683206]
Q = [4.37, 4.73, 5.63, 5.06, 6.04, 5.52, 5.3, 5.08, 6.01, 5.04, 4.15, 5.31, 4.19, 6.6, 4.39, 6.63, 6.19, 4.74, 5.7, 5.21, 3.22, 5.19, 5.61, 3.9, 4.74, 5.4, 4.11, 3.56, 4.33, 4.96, 4.47, 4.18, 4.43, 5.19, 5.6, 3.55, 3.56, 5.71, 4.81, 5.97, 4.72, 3.3, 4.59]


# option 1: straight-up
"""
feature_array = np.asarray(P1 + P2 + P3)
feature_array.shape = (len(P1),3)
feature_ln = ln.LinearRegression()
Y = np.asarray(Q)
Y.shape = (len(P1),)
feature_ln.fit(feature_array, Y)
Y_pred = feature_ln.predict(feature_array)
"""

Y_pred = []
tweet_counts = []
# option 2: 1-out CV

for i in xrange(0, len(P1)):
        with open('super/' + company_name_lst[i] + '.txt', 'rb') as file:
            tweets = file.readlines()
        tweet_counts.append(np.log(len(tweets)))

for i in xrange(0, len(P1)):
    #try:
        feature_lst = tweet_counts[:i] + tweet_counts[i+1:] + P1[:i] + P1[i+1:] + P2[:i] + P2[i+1:] + P3[:i] + P3[i+1:]
        feature_array = np.asarray(feature_lst)
        feature_array.shape = (len(P1)-1,4)
        feature_ln = ln.LinearRegression()
        Y = np.asarray(Q[:i] + Q[i+1:])
        Y.shape = (len(P1)-1,)
        feature_ln.fit(feature_array, Y)
        #print feature_ln.score(feature_array, Y)
        test_row = np.asarray([tweet_counts[i], P1[i], P2[i], P3[i]])
        test_row.shape = (4,)
        Y_pred.append(feature_ln.predict(test_row)[0])
    #except:
        #print len(P1)
        #print len(feature_lst)

print np.corrcoef(list(Y_pred),list(Q))[0,1]
#print np.corrcoef(list(P2),list(Q))[0,1]
#print np.corrcoef(list(P3),list(Q))[0,1]
for i in xrange(0, len(P1)):
    x = 0
    #print [company_name_lst[i], tweet_counts[i], Y_pred[i], Q[i]]

# budweiser second commercial 5.71, 5.08
# budweiser helen mirren 6.17, 6.01
# heinz 5.61, 6.63
# independence day 5.47, 4.74
# pokemon 5.90, 4.47


exclude_lst = ['budweiser', 'bud helen mirren', 'heinz', 'independence day', 'pokemon']

Y_prime = []
Q_prime = []
for i in xrange(0, len(company_name_lst)):
    if company_name_lst[i] not in exclude_lst:
        Y_prime.append(list(Y_pred)[i])
        Q_prime.append(list(Q)[i])

#fig = plt.scatter(list(Y_prime), Q_prime)
fig = plt.figure()

fig.suptitle('Model Performance', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

#fig.suptitle('Model performance', fontsize=14, fontweight='bold')

ax.set_xlabel('Prediction')
ax.set_ylabel('USA Today Ad Meter')

#for word in rating_dict.keys():
#    ax.text(float(rating_dict[word][0]), float(rating_dict[word][1]), word)
for i in xrange(0, len(company_name_lst)):
    #print [Y_pred[i], Q[i], company_name_lst[i]]
    if math.fabs(float(Y_pred[i])-5) < 1.3 and math.fabs(float(Q[i])-5) < 1.3:
        ax.text(float(Y_pred[i]), float(Q[i]), str(company_name_lst[i]))

plt.plot(Y_pred, np.poly1d(np.polyfit(Y_pred, Q, 1))(Y_pred))

ax.axis([3.5, 6.5, 3.5, 6.5])
plt.show()


#print np.corrcoef(X1, Y)[0,1]
#print np.corrcoef(X2, Y)[0,1]
#print np.corrcoef(X3, Y)[0,1]
