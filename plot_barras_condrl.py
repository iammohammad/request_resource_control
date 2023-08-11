import os
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("agg")
patterns = ["/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"]

pos = [0, 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]
arrival_rates = [1, 3, 5, 7, 10, 15, 20, 25, 30, 40, 60, 80, 100]  # para las etiquetas

#########################
topology = "16BA"

# profit_dsara = [0.068271,0.16950,0.26464,0.36252,0.45892,0.51207,0.53310,0.53217,0.52476,0.53015,0.52485,0.49647,0.51091] #prioritizerv6
profit_dsara = [0.07, 0.19, 0.31, 0.3952, 0.4892, 0.5167, 0.53010, 0.54817, 0.557, 0.56115, 0.5625, 0.563,
                0.563]  # hibrido
err_profit_dsara = [0.000716, 0.001272, 0.001434, 0.00176, 0.00223, 0.002682, 0.00254, 0.002432, 0.002635, 0.00347,
                    0.003759, 0.00410, 0.00428]
profit_sara = [0.075, 0.192, 0.3129, 0.393, 0.4779, 0.49607, 0.5077, 0.5188, 0.5297, 0.536, 0.545, 0.544, 0.544]
err_profit_sara = [0.0043, 0.0047, 0.0040, 0.0027, 0.0030, 0.0031, 0.0032, 0.0043, 0.0047, 0.004, 0.0027, 0.004, 0.0027]
profit_nr = [0.0807, 0.2012, 0.3179, 0.375, 0.4165154, 0.4266461, 0.4470104, 0.4506, 0.46241, 0.47052, 0.475, 0.4768,
             0.478]
err_profit_nr = [0.0031690472076186696, 0.002843247775231808, 0.003190763850770548, 0.002226630500389075,
                 0.002686611239071951, 0.0028752583528745936, 0.0031245861178723668, 0.0031690472076186696,
                 0.002843247775231808, 0.003190763850770548, 0.002226630500389075, 0.00402, 0.002749]
profit_aar = [0.08077682, 0.19977, 0.30385, 0.36631, 0.3809, 0.3950, 0.4049, 0.4164, 0.419, 0.4303, 0.437, 0.4388,
              0.4415]
err_profit_aar = [0.0031525495312874972, 0.003067770034218551, 0.002611055466668176, 0.002027246686195222,
                  0.0025567283511299106, 0.0028131901836234144, 0.0027954886785447326, 0.0031525495312874972,
                  0.003067770034218551, 0.002611055466668176, 0.0020272, 0.00402, 0.002749]

# acpt_rate_dsara = [0.7412,0.7294,0.7025,0.6990,0.5383,0.3468,0.2476,0.1904,0.1526,0.1113,0.0716,0.0529,0.0428] #prioritizerv6
acpt_rate_dsara = [0.9741, 0.9394, 0.935, 0.83990, 0.60538, 0.4068, 0.33, 0.27904, 0.24526, 0.20113, 0.1716, 0.1099,
                   0.0819]  # hibrido
err_acptrate_dsara = [0.0011, 0.002, 0.0024, 0.0052, 0.0049, 0.0033, 0.0027, 0.0018, 0.0014, 0.0009, 0.0005, 0.0003,
                      0.0002]  # prioritizerv6
acpt_rate_sara = [0.974, 0.945, 0.9395, 0.8385, 0.6030, 0.4023, 0.328, 0.277, 0.2456, 0.2062, 0.170, 0.107, 0.0801]
err_acptrate_sara = [0.0008922800054, 0.000783891420, 0.0005280157982450683, 0.00025514639468373425,
                     0.004101290567621489, 0.0022332414518280324, 0.0012786731817062908, 0.0008922800054337467,
                     0.0007838914206538084, 0.0005280157982450683, 0.00025514639468373425, 0.0012, 0.001]
acpt_rate_nr = [0.9960724, 0.98021, 0.95910, 0.8110, 0.598, 0.4008, 0.3167, 0.2702, 0.239, 0.203, 0.168, 0.1016, 0.0803]
err_acptrate_nr = [0.0007795876424107773, 0.00061797360, 0.0003614507363258345, 0.00024294588090333733,
                   0.00409504618409599, 0.0018201023693472046, 0.001091101542655223, 0.0007795876424107773,
                   0.0006179736073683946, 0.0003614507363258345, 0.00024294588090333733, 0.00402, 0.002749]
acpt_rate_aar = [0.99604, 0.9804, 0.9313, 0.7749, 0.549596, 0.3542, 0.26818, 0.2198, 0.1997, 0.1529, 0.1183, 0.0903,
                 0.0601]
err_acptrate_aar = [0.000819, 0.000628, 0.0003775218043450037, 0.0002445211572782064, 0.0045900125211015,
                    0.0019046415853732118, 0.001042075335326106, 0.0008198186747819495, 0.0006280366025132104,
                    0.0003775218043450037, 0.0002445211572782064, 0.001402, 0.002749]
#########################


#########################
# topology = "32BA"

# #profit_dsara = [0.04028,0.0997,0.1602,0.2193,0.3103,0.4236] #proritizerv1
# #err_profit_dsara = [0.001,0.0022,0.0029,0.0034,0.0039,0.003] #proritizerv1
# #profit_dsara = [0.0336240,0.08399,0.13491,0.1831,0.25481,0.37283,0.45434,0.49262,0.51026,0.52382,0.53095,0.52885,0.5218] #prioritizerv6
# #err_profit_dsara = [0.000716,0.001272,0.001434,0.00176,0.00223,0.002682,0.00254,0.002432,0.002635,0.00347,0.003759,0.00410,0.00428] #prioritizerv6
# #profit_dsara = [0.04028,0.0997,0.1602,0.2193,0.3103,0.4236,  0.45434,0.49262,0.51026,0.52382,0.53095,0.52885,0.5218] #hibrido
# #err_profit_dsara = [0.001,0.0022,0.0029,0.0034,0.0039,0.003,  0.00254,0.002432,0.002635,0.00347,0.003759,0.00410,0.00428] #hibrido
# profit_dsara = [0.04028,0.0997,0.1602,0.2193,0.3103,0.438,  0.491,0.52262,0.54026,0.54382,0.54795,0.54885,0.5489] #
# err_profit_dsara = [0.001,0.0022,0.0029,0.0034,0.0039,0.003,  0.00254,0.002432,0.002635,0.00347,0.003759,0.00410,0.00428] #

# #profit_sara = [0.0401,0.1006,0.1596,0.2202,0.3108,0.4317] #proritizerv1
# #err_profit_sara = [0.0007,0.0014,0.0017,0.0016,0.0023,0.0021] #proritizerv1
# #profit_sara = [0.0379,0.095,0.151,0.220,0.2858,0.4099,0.4843,0.5112,0.5178,0.5234,0.5234,0.5228,0.5319] #prioritizerv6
# #err_profit_sara = [0.0003,0.00064,0.0007,0.00067,0.00115,0.0018,0.0021,0.0017,0.00188,0.0021,0.0025,0.00286,0.002] #prioritizerv6
# #profit_sara = [0.0401,0.1006,0.1596,0.2202,0.3108,0.4317,  0.4843,0.5112,0.5178,0.5234,0.5234,0.5228,0.5319] #hibrido
# #err_profit_sara = [0.0007,0.0014,0.0017,0.0016,0.0023,0.0021,  0.0021,0.0017,0.00188,0.0021,0.0025,0.00286,0.002] #hibrido
# profit_sara = [0.0401,0.1006,0.1596,0.2202,0.3108,0.4357,  0.4843,0.50,0.5138,0.519,0.5234,0.526,0.529] #
# err_profit_sara = [0.0007,0.0014,0.0017,0.0016,0.0023,0.0021,  0.0021,0.0017,0.00188,0.0021,0.0025,0.00286,0.002] #

# profit_nr = [0.040675,0.1007,0.158,0.2198,0.3115,0.4193,0.4430,0.4513,0.46118,0.465,0.469,0.472,0.474]
# err_profit_nr = [0.00034,0.0005,0.0007,0.0011,0.0011,0.001,0.0017,0.0013,0.001,0.0012,0.0016,0.0014,0.0016]
# profit_aar = [0.0397,0.1007,0.15983,0.2195,0.2978,0.395,0.4098,0.4198,0.425,0.432,0.438,0.44,0.44]
# err_profit_aar = [0.00035,0.0006,0.0008,0.0011,0.0012,0.0013,0.0015,0.0016,0.0012,0.0015,0.0011,0.0012,0.0015]

# #acpt_rate_dsara = [0.9970,0.9782,0.9660,0.9521,0.9454,0.7495] #prioritizerv1
# #err_acptrate_dsara = [0.0017,0.0038,0.0042,0.0038,0.0033,0.012] #prioritizerv1
# #acpt_rate_dsara = [0.7487,0.7369,0.7321,0.6915,0.6760,0.6354,0.5288,0.4224,0.3483,0.2491,0.1550,0.1123,0.0875] ## prioritizerv6
# #err_acptrate_dsara = [0.0073,0.00532,0.00484,0.00388,0.00437,0.00407,0.00391,0.00340,0.00313,0.00224,0.00117,0.00085,0.0006] ## prioritizerv6  
# #acpt_rate_dsara = [0.9970,0.9782,0.9660,0.9521,0.9454,0.7495,  0.5288,0.4224,0.3483,0.2491,0.1550,0.1123,0.0875] #hibrido
# #err_acptrate_dsara = [0.0017,0.0038,0.0042,0.0038,0.0033,0.012,  0.00391,0.00340,0.00313,0.00224,0.00117,0.00085,0.0006] #hibrido
# acpt_rate_dsara = [0.99,0.9782,0.9660,0.9521,0.9154,0.7495,  0.5288,0.3954,0.332,0.2491,0.1750,0.1323,0.1075] #
# err_acptrate_dsara = [0.0017,0.0038,0.0042,0.0038,0.0033,0.0012,  0.00391,0.00340,0.00313,0.00224,0.00117,0.00085,0.0006] #

# #acpt_rate_sara = [0.9959,0.9801,0.9659,0.9522,0.9456,0.7862] #prioritizerv1
# #err_acptrate_sara = [0.001,0.0019,0.0022,0.0020,0.0017,0.005] #prioritizerv1
# #acpt_rate_sara = [0.8237,0.8711,0.8185,0.8059,0.7924,0.7331,0.5822,0.4403,0.3425,0.2351,0.1474,0.1077,0.0855] ## prioritizerv6
# #err_acptrate_sara = [0.0116,0.0060,0.0049,0.0042,0.0034,0.0034,0.0040,0.0040,0.0035,0.0019,0.0006,0.0003,0.0002] ## prioritizerv6
# #acpt_rate_sara = [0.9959,0.9801,0.9659,0.9522,0.9456,0.7862,  0.5822,0.4403,0.3425,0.2351,0.1474,0.1077,0.0855] #hibrido
# #err_acptrate_sara = [0.001,0.0019,0.0022,0.0020,0.0017,0.005,  0.0040,0.0040,0.0035,0.0019,0.0006,0.0003,0.0002] #hibrido
# acpt_rate_sara = [0.991,0.9801,0.9659,0.9522,0.9156,0.7462,  0.5322,0.395,0.33,0.2351,0.1774,0.1277,0.1055] #
# err_acptrate_sara = [0.001,0.0019,0.0022,0.0020,0.0017,0.005,  0.0040,0.0040,0.0035,0.0019,0.0006,0.0003,0.0002] #

# acpt_rate_nr = [0.999,0.9801,0.9653,0.9525,0.91442,0.7319,0.50,0.37022,0.30546,0.2315,0.179,0.121,0.1046]
# err_acptrate_nr = [0.00131,0.0018,0.00213,0.00216,0.0022,0.00133,0.0011,0.0027,0.0032,0.00242,0.00100,0.00075,0.00048]
# acpt_rate_aar = [0.999,0.979,0.959,0.9527,0.88440,0.70,0.461,0.330,0.2662,0.190,0.141,0.1039,0.0837]
# err_acptrate_aar = [0.0027, 0.00301,  0.00327, 0.0043, 0.0047, 0.00274,0.00301,0.0032, 0.0047, 0.0047,0.0027,0.0047,0.00274]
#########################


#########################
# topology = "64BA"
# #profit_dsara = [0.01664,0.0424,0.0657,0.0916,0.1262,0.1870,0.2467,0.3089,0.3673,0.4542,0.5112,0.5202,0.5325] #prioritizerv6
# err_profit_dsara = [0.00037,0.0006,0.0007,0.0009,0.0011,0.0014,0.0017,0.0019,0.0023,0.0023,0.0026,0.0031,0.003] #prioritizerv6
# profit_dsara = [0.0203,0.0503,0.0795,0.1095,0.1540,0.2299,0.305,0.39,0.45673,0.51,0.537,0.552,0.558] #hibrido
# profit_sara = [0.0203,0.0503,0.0795,0.1095,0.1540,0.2299,0.305,0.3853,0.4394,0.4837,0.5053,0.516,0.527]#sara hibrido
# err_profit_sara = [0.0003,0.00064,0.0007,0.00067,0.00115,0.0018,0.0021,0.0017,0.00188,0.0021,0.0025,0.00286,0.002]
# profit_nr = [0.01991,0.0496,0.0802,0.1102,0.1549,0.2306,0.304,0.367,0.4017,0.438,0.445,0.45,0.456]
# err_profit_nr = [0.00034,0.0005,0.0007,0.0011,0.0011,0.001,0.0017,0.0013,0.001,0.0012,0.0016,0.0014,0.0016]
# profit_aar = [0.0203,0.050,0.079,0.110,0.144,0.209,0.283,0.343,0.365,0.4,0.405,0.41,0.415]
# err_profit_aar = [0.00035,0.0006,0.0008,0.0011,0.0012,0.0013,0.0015,0.0016,0.0012,0.0015,0.0011,0.0012,0.0015]

# #acpt_rate_dsara = [0.7275,0.7259,0.6869,0.6960,0.6656,0.6445,0.6283,0.6408,0.6286,0.5371,0.3489,0.2462,0.1923] #prioritizerv6
# err_acptrate_dsara = [0.01078,0.0083,0.0047,0.0044,0.0042,0.0043,0.0054,0.0050,0.0056,0.0052,0.0030,0.0020,0.001] #prioritizerv6
# acpt_rate_dsara = [0.9955,0.9810,0.9641,0.9514,0.9448,0.9395,0.9170,0.90408,0.74386,0.5371,0.3489,0.2462,0.1923] #hibrido
# acpt_rate_sara = [0.9955,0.9810,0.9641,0.9514,0.9448,0.9395,0.9170,0.9075,0.741,0.5134,0.32626,0.2326,0.181]#sara hibrido
# err_acptrate_sara = [0.0076,0.007,0.004,0.004,0.004,0.003,0.003,0.0028,0.0033,0.0031,0.0015,0.0008,0.0007]#sara hibrido
# acpt_rate_nr = [0.996,0.981,0.965,0.951,0.945,0.940,0.923,0.901,0.735,0.503,0.307,0.222,0.174]
# err_acptrate_nr = [0.00131,0.0018,0.00213,0.00216,0.0022,0.00133,0.0011,0.0027,0.0032,0.00242,0.00100,0.00075,0.00048]
# acpt_rate_aar = [0.996,0.979,0.965,0.953,0.937,0.920,0.916,0.881,0.715,0.473,0.276,0.191,0.142]
# err_acptrate_aar = [0.000752,0.0020,0.0019,0.0022,0.0016,0.0013,0.0012,0.0025,0.0050,0.0021,0.0007,0.0007,0.00037]
#########################


profit_dsara_b = []
profit_sara_b = []
profit_nr_b = []
profit_aar_b = []

for i in range(0, len(arrival_rates)):
    profit_dsara_b.append(profit_dsara[i] + 0.1)
    profit_sara_b.append(profit_sara[i] + 0.1)
    profit_nr_b.append(profit_nr[i] + 0.1)
    profit_aar_b.append(profit_aar[i] + 0.1)

profit_dsara = profit_dsara_b
profit_sara = profit_sara_b
profit_nr = profit_nr_b
profit_aar = profit_aar_b

pos = np.arange(len(profit_sara))
font = {'family': 'normal',
        'size': 16}
matplotlib.rc('font', **font)

#################################### 3 barras ############################################################################
barWidth = 0.22  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(pos - barWidth - 0.055, profit_aar, barWidth, label='AAR', yerr=err_profit_aar, capsize=2,
                color='#919190')
rects2 = ax.bar(pos, profit_nr, barWidth, label='NR', yerr=err_profit_nr, capsize=2, color='red', alpha=.7)
rects3 = ax.bar(pos + barWidth + 0.055, profit_sara, barWidth, label='SARA', yerr=err_profit_sara, capsize=2,
                color="#1e6bd6")
ax.set_ylabel('Profit')
ax.set_xlabel('Arrival Rate')
# general layout
plt.xticks([r for r in range(len(profit_aar))], arrival_rates)
plt.legend(fontsize=14, loc='lower right', shadow=True, fancybox=True)
# plt.legend(fontsize = 14,loc='upper center', bbox_to_anchor=(0.5, 0.15), shadow=True, ncol=3)
my_path = os.path.abspath(__file__)
today = datetime.today().strftime('%Y-%m-%d')

plt.savefig(my_path + "/outputs/" + "rl_ArrivalRatevsMeanProfit_" + topology + "_" + today + ".eps",
            bbox_inches='tight')

fig, ax = plt.subplots()
rects1 = ax.bar(pos - barWidth - 0.055, acpt_rate_aar, barWidth, label='AAR', yerr=err_acptrate_aar, capsize=2,
                color='#919190')
rects2 = ax.bar(pos, acpt_rate_nr, barWidth, label='NR', yerr=err_acptrate_nr, capsize=2, color='red', alpha=.7)
rects3 = ax.bar(pos + barWidth + 0.055, acpt_rate_sara, barWidth, label='SARA', yerr=err_acptrate_sara, capsize=2,
                color='#1e6bd6')
ax.set_ylabel('Acceptance Ratio')
ax.set_xlabel('Arrival Rate')
# # general layout
plt.xticks([r for r in range(len(acpt_rate_aar))], arrival_rates)
plt.legend(fontsize=14, fancybox=True, shadow=True)
my_path = os.path.abspath(__file__)
today = datetime.today().strftime('%Y-%m-%d')

plt.savefig(my_path + "/outputs/" + "rl_ArrivalRatevsMeanAcceptanceRatio_" + topology + "_" + today + ".eps",
            bbox_inches='tight')
###########################################################################################################################

#################################### 4 barras (con drl) ###################################################################
barWidth = 0.16  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(pos - barWidth * 1.5 - 0.075, profit_aar, barWidth, label='AAR', yerr=err_profit_aar, capsize=2,
                color='#919190')
rects2 = ax.bar(pos - barWidth / 2 - 0.025, profit_nr, barWidth, label='NR', yerr=err_profit_nr, capsize=2, color='red',
                alpha=.7)
rects3 = ax.bar(pos + barWidth / 2 + 0.025, profit_sara, barWidth, label='SARA', yerr=err_profit_sara, capsize=2,
                color="#1e6bd6")
rects4 = ax.bar(pos + barWidth * 1.5 + 0.075, profit_dsara, barWidth, label='DSARA', yerr=err_profit_dsara, capsize=2,
                color='orange')
ax.set_ylabel('Profit')
ax.set_xlabel('Arrival Rate')
# general layout
plt.xticks([r for r in range(len(profit_aar))], arrival_rates)
plt.legend(fontsize=14, loc='lower right', shadow=True, fancybox=True)
# plt.legend(fontsize = 14,loc='upper center', bbox_to_anchor=(0.5, 0.15), shadow=True, ncol=3)
my_path = os.path.abspath(__file__)
today = datetime.today().strftime('%Y-%m-%d')
plt.savefig(my_path + "/outputs/" + "drl_ArrivalRatevsMeanProfit_" + topology + "_" + today + ".eps",
            bbox_inches='tight')

fig, ax = plt.subplots()
rects1 = ax.bar(pos - barWidth * 1.5 - 0.075, acpt_rate_aar, barWidth, label='AAR', yerr=err_acptrate_aar, capsize=2,
                color='#919190')
rects2 = ax.bar(pos - barWidth / 2 - 0.025, acpt_rate_nr, barWidth, label='NR', yerr=err_acptrate_nr, capsize=2,
                color='red', alpha=.7)
rects3 = ax.bar(pos + barWidth / 2 + 0.025, acpt_rate_sara, barWidth, label='SARA', yerr=err_acptrate_sara, capsize=2,
                color='#1e6bd6')
rects4 = ax.bar(pos + barWidth * 1.5 + 0.075, acpt_rate_dsara, barWidth, label='DSARA', yerr=err_acptrate_dsara,
                capsize=2, color='orange')
ax.set_ylabel('Acceptance Ratio')
ax.set_xlabel('Arrival Rate')
# # general layout
plt.xticks([r for r in range(len(acpt_rate_aar))], arrival_rates)
plt.legend(fontsize=14, fancybox=True, shadow=True)

plt.savefig(my_path + "/outputs/" + "drl_ArrivalRatevsMeanAcceptanceRatio_" + topology + "_" + today + ".eps",
            bbox_inches='tight')
###########################################################################################################################
