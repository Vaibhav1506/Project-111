import statistics;
import plotly.graph_objects as go;
import plotly.figure_factory as ff;
import pandas as pd;
import random;

df = pd.read_csv("medium_data.csv");
readingtimeList = df["reading_time"].tolist();

readingTimeMean = statistics.mean(readingtimeList);
print("Readingtime mean:",readingTimeMean);

def random_mean_set(counter):
  dataSet = [];
  for i in range(0,counter):
    randomIndex = random.randint(0,len(readingtimeList));
    value = readingtimeList[randomIndex];
    dataSet.append(value);
  randomMean = statistics.mean(dataSet);
  return randomMean;

def show_fig(meanList):
  figData = meanList;

  fig = ff.create_distplot([figData],["Reading Time"],show_hist = False);

  samplingMean = statistics.mean(meanList);
  stdev = statistics.stdev(meanList);
  
  stdev1_start,stdev1_end = samplingMean - stdev,samplingMean + stdev;
  stdev2_start,stdev2_end = samplingMean - (2*stdev),samplingMean + (2*stdev);
  stdev3_start,sd3_end = samplingMean - (3*stdev),samplingMean + (3*stdev);
  
  print("Standard Deviation 1:",stdev1_start,stdev1_end);
  print("Standard Deviation 2:",stdev2_start,stdev2_end);
  print("Standard Deviation 3:",stdev3_start,sd3_end);

  fig.add_trace(go.Scatter(x = [stdev1_start,stdev1_start],y = [0,0.8]));
  fig.add_trace(go.Scatter(x = [stdev1_end,stdev1_end],y = [0,0.8]));
  fig.add_trace(go.Scatter(x = [stdev2_start,stdev2_start],y = [0,0.8]));
  fig.add_trace(go.Scatter(x = [stdev2_end,stdev2_end],y = [0,0.8]));
  fig.add_trace(go.Scatter(x = [stdev3_start,stdev3_start],y = [0,0.8]));
  fig.add_trace(go.Scatter(x = [sd3_end,sd3_end],y = [0,0.8]));


  fig.add_trace(go.Scatter(x = [samplingMean,samplingMean],y = [0,0.8]));
  sampleMean = statistics.mean(readingtimeList);
  fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.8]));
  
  zSampTest = (sampleMean - samplingMean)/stdev;
  print("Z Sample Test is:",zSampTest);

  fig.show();

meanList = [];
for i in range(0,1000):
  meanSet = random_mean_set(100)
  meanList.append(meanSet)
show_fig(meanList)