# By B. Javanmardi (https://github.com/behjava)
# Visualising Prevalence of diabetes mellitus (%) in Europe
# data file HFA_379_EN.csv obtained from European Health Information Gateway.
# Years data is available in this file: 1950—2019
# read file skip metadata rows

import os
import pandas as pd
import plotly.express as px


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/HFA_379_EN.csv', sep=',',
                    skiprows=25, skipfooter=26, header=0)

# group by year and average
EURO_mean=round(data.groupby(['YEAR']).mean(),1)

EURO_mean_after_1979 = EURO_mean[EURO_mean.index>1979]

# scatter plot using customized color_continuous_scale
fig=px.scatter(EURO_mean_after_1979, size='value', size_max=30, color='value', color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']])
fig.update_yaxes(title_text='Prevalence of diabetes mellitus (%)')
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(dict(font=dict(color='black',size=10)), x=2012, y=1.3,
            text="©DataDeed.de",
            showarrow=False,
            yshift=1)

# fig.add_annotation(dict(font=dict(color='grey',size=15)), x=2000, y=43,
#             text="Data Source: European Health Information Gateway (WHO)",
#             showarrow=False,
#             yshift=1)

fig.update_layout(modebar_remove=['lasso2d','select2d'])

assure_path_exists('output/')
fig.write_html("output/diabetes_mellitus_Europe_prevalence.html")
fig.write_image("output/diabetes_mellitus_Europe_prevalence.jpg", scale=2.0)

fig.show()
