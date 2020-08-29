Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import tweepy as tw
>>> import pandas as pd
>>> consumer_key = 'QAjGb40CLEPfnbt2ANA6ta6Zj'
>>> consumer_secret = 'e5espzdABbrWCkB3M6fHoj7SCw4E0wFtWfmCx4aYaihErGroWw'
>>> access_token = '1899502472-tms0VwpXgXRHFQJReMTZUMNuxV5I2Nyn0Kj2jgs'
>>> access_token_secret = 'g45ansF59S2GH8f339c3wUNh4k4moEexOoPDJ3zL83wjx'
>>> auth = tw.OAuthHandler(consumer_key, consumer_secret)
>>> auth.set_access_token(access_token, access_token_secret)
>>> api = tw.API(auth, wait_on_rate_limit=True)
>>> search_words = '#caa'
>>> date_since = '2019-12-10'
>>> tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(2000)
>>> users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in tweets]
>>> tweet_text = pd.DataFrame(data=users_locs, 
                   columns=['user', "location", "tweet"])
>>> tweet_text.to_csv(r'C:\Users\srini\Desktop\Sentiment analysis\twt.csv')
>>> import re
>>> import nltk
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> df = pd.read_csv('C:\Users\srini\Desktop\Sentiment analysis\twt.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> df = pd.read_csv('twt.csv')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    df = pd.read_csv('twt.csv')
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 697, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 424, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 890, in __init__
    self._make_engine(self.engine)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1117, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1848, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 387, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 705, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] File b'twt.csv' does not exist: b'twt.csv'
>>> df = pd.read_csv(r'C:\Users\srini\Desktop\Sentiment analysis\twt.csv')
>>> df.head()
   Unnamed: 0  ...                                              tweet
0           0  ...  RT @SwamiGeetika: This is how #CAA Protesters ...
1           1  ...  RT @INCChandigarh: C'mon @narendramodi ji, ple...
2           2  ...  Every Business have to go through 5 stages bef...
3           3  ...  RT @PandaJay: #CAA\nNo explanation is necessar...
4           4  ...  RT @BDUTT: Here is @DilliDurAst in hindi for #...

[5 rows x 4 columns]
>>> def clean_tweet(df):
	df = re.sub('http\S+\s*', '', tweet)  # remove URLs
	df = re.sub('RT|cc', '', tweet)  # remove RT and cc
	df = re.sub('#\S+', '', tweet)  # remove hashtags
	df = re.sub('@\S+', '', tweet)  # remove mentions
	df = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
	df = re.sub('\s+', ' ', tweet)  # remove extra whitespace
	return df

>>> from nltk.sentiment.vader import SentimentIntensityAnalyser
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    from nltk.sentiment.vader import SentimentIntensityAnalyser
ImportError: cannot import name 'SentimentIntensityAnalyser' from 'nltk.sentiment.vader' (C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\nltk\sentiment\vader.py)
>>> from nltk.sentiment.vader import SentimentIntensityAnalyzer
>>> ana = SentimentIntensityAnalyzer()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ana = SentimentIntensityAnalyzer()
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\nltk\sentiment\vader.py", line 334, in __init__
    self.lexicon_file = nltk.data.load(lexicon_file)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\nltk\data.py", line 868, in load
    opened_resource = _open(resource_url)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\nltk\data.py", line 993, in _open
    return find(path_, path + ['']).open()
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\nltk\data.py", line 701, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mvader_lexicon[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('vader_lexicon')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93msentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt[0m

  Searched in:
    - 'C:\\Users\\srini/nltk_data'
    - 'C:\\Users\\srini\\AppData\\Local\\Programs\\Python\\Python37-32\\nltk_data'
    - 'C:\\Users\\srini\\AppData\\Local\\Programs\\Python\\Python37-32\\share\\nltk_data'
    - 'C:\\Users\\srini\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\nltk_data'
    - 'C:\\Users\\srini\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
    - ''
**********************************************************************

>>> import nltk
										      
>>> nltk.download('vader_lexicon')
										      
[nltk_data] Downloading package vader_lexicon to
[nltk_data]     C:\Users\srini\AppData\Roaming\nltk_data...
True
>>> ana = SentimentIntensityAnalyzer()
										      
>>> def clean_tweet(d):
	d = re.sub('http\S+\s*', '', tweet)  # remove URLs
	d = re.sub('RT|cc', '', tweet)  # remove RT and cc
	d = re.sub('#\S+', '', tweet)  # remove hashtags
	d = re.sub('@\S+', '', tweet)  # remove mentions
	d = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
	d = re.sub('\s+', ' ', tweet)  # remove extra whitespace
	return d

										      
>>> df['main_text']= df.tweet.apply(lambda x: clean_tweet(x))
										      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    df['main_text']= df.tweet.apply(lambda x: clean_tweet(x))
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\series.py", line 3591, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas\_libs\lib.pyx", line 2216, in pandas._libs.lib.map_infer
  File "<pyshell#36>", line 1, in <lambda>
    df['main_text']= df.tweet.apply(lambda x: clean_tweet(x))
  File "<pyshell#35>", line 2, in clean_tweet
    d = re.sub('http\S+\s*', '', tweet)  # remove URLs
NameError: name 'tweet' is not defined
>>> ef clean_tweet(d):
	d = re.sub('http\S+\s*', '', d)  # remove URLs
	d = re.sub('RT|cc', '', d)  # remove RT and cc
	d = re.sub('#\S+', '', d)  # remove hashtags
	d = re.sub('@\S+', '', d)  # remove mentions
	d = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', d)  # remove punctuations
	d = re.sub('\s+', ' ', d)  # remove extra whitespace
	return d
										      
SyntaxError: invalid syntax
>>> def clean_tweet(d):
	d = re.sub('http\S+\s*', '', d)  # remove URLs
	d = re.sub('RT|cc', '', d)  # remove RT and cc
	d = re.sub('#\S+', '', d)  # remove hashtags
	d = re.sub('@\S+', '', d)  # remove mentions
	d = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', d)  # remove punctuations
	d = re.sub('\s+', ' ', d)  # remove extra whitespace
	return d

										      
>>> df['main_text']= df.tweet.apply(lambda x: clean_tweet(x))
										      
>>> df['polarity_value'] = df.main_text.apply(lamda x: analyser.polarity_scores(x)['compound'])
										      
SyntaxError: invalid syntax
>>> df['polarity_value'] = df.main_text.apply(lambda x: analyser.polarity_scores(x)['compound'])
										      
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    df['polarity_value'] = df.main_text.apply(lambda x: analyser.polarity_scores(x)['compound'])
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\series.py", line 3591, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas\_libs\lib.pyx", line 2216, in pandas._libs.lib.map_infer
  File "<pyshell#42>", line 1, in <lambda>
    df['polarity_value'] = df.main_text.apply(lambda x: analyser.polarity_scores(x)['compound'])
NameError: name 'analyser' is not defined
>>> df['polarity_value'] = df.main_text.apply(lambda x: ana.polarity_scores(x)['compound'])
										      
>>> df['neutral']=df.main_text.apply(lambda x: ana.polarity_scores(x)['neu'])
										      
>>> df['negative']=df.main_text.apply(lambda x: ana.polarity_scores(x)['neg'])
										      
>>> df['positive']=df.main_text.apply(lambda x: ana.polarity_scores(x)['pos'])
										      
>>> df['sentiment']=''
										      
>>> dataset.loc[dataset.polarity_value>0,'sentiment_type']= 'POSITIVE'
										      
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    dataset.loc[dataset.polarity_value>0,'sentiment_type']= 'POSITIVE'
NameError: name 'dataset' is not defined
>>> df.loc[dataset.polarity_value>0,'sentiment_type']= 'POSITIVE'
										      
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    df.loc[dataset.polarity_value>0,'sentiment_type']= 'POSITIVE'
NameError: name 'dataset' is not defined
>>> df.loc[df.polarity_value>0,'sentiment_type']= 'POSITIVE'
										      
>>> df.loc[df.polarity_value=0,'sentiment_type']= 'NEUTRAL'
										      
SyntaxError: invalid syntax
>>> df.loc[df.polarity_value==0,'sentiment_type']= 'NEUTRAL'
										      
>>> df.loc[df.polarity_value<0,'sentiment_type']= 'NEGATIVE'
										      
>>> df.columns
										      
Index(['Unnamed: 0', 'user', 'location', 'tweet', 'main_text',
       'polarity_value', 'neutral', 'negative', 'positive', 'sentiment',
       'sentiment_type'],
      dtype='object')
>>> df.head()
										      
   Unnamed: 0           user  ... sentiment sentiment_type
0           0   tripathimanu  ...                 NEGATIVE
1           1   pankajbajp16  ...                 POSITIVE
2           2    Rational_me  ...                  NEUTRAL
3           3  Sammy64426029  ...                 NEGATIVE
4           4      rpsingh15  ...                  NEUTRAL

[5 rows x 11 columns]
>>> import seaborn as sns
										      
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
>>> df.sentiment_type.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=['red','yellow','green'])
										      
<matplotlib.axes._subplots.AxesSubplot object at 0x1B2F9510>
>>> %matplotlib inline
										      
SyntaxError: invalid syntax
>>> import matplotlib.pyplot as plt %matplotlib inline
										      
SyntaxError: invalid syntax
>>> import seaborn as sns
										      
>>> sns.set(style='darkgrid')
										      
>>> sns.countplot(x=df['sentiment_type'])
										      
<matplotlib.axes._subplots.AxesSubplot object at 0x1B2F9510>
>>> print(sns.countplot(x=df['sentiment_type']))
										      
AxesSubplot(0.22375,0.11;0.5775x0.77)
>>> sns.barplot(x='sentiment', y='count', data=df['sentiment_type'])
										      
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sns.barplot(x='sentiment', y='count', data=df['sentiment_type'])
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\seaborn\categorical.py", line 3149, in barplot
    errcolor, errwidth, capsize, dodge)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\seaborn\categorical.py", line 1607, in __init__
    order, hue_order, units)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\seaborn\categorical.py", line 155, in establish_variables
    raise ValueError(err)
ValueError: Could not interpret input 'sentiment'
>>> from matplotlib.gridspec import GridSpec
    
>>> targetCounts = dataset.sentiment_type.value_counts()
    
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    targetCounts = dataset.sentiment_type.value_counts()
NameError: name 'dataset' is not defined
>>> targetCounts = df.sentiment_type.value_counts()
    
>>> targetLabels  =['POSITIVE', 'NEGATIVE', 'NEUTRAL']
    
>>> plt.figure(1, figsize=(15,15))
    
<Figure size 640x480 with 1 Axes>
>>> the_grid = GridSpec(2, 2)

>>> cmap = plt.get_cmap('Spectral')
    
>>> colors = [cmap(i) for i in np.linspace(0, 1, 3)]
    
>>> plt.subplot(the_grid[0, 1], aspect=1, title='TWEET DISTRIBUTION')
    
<matplotlib.axes._subplots.AxesSubplot object at 0x11A07BB0>
>>> source_pie = plt.pie(targetCounts, labels=targetLabels, autopct='%1.1f%%', shadow=True, colors=colors)
    
>>> plt.show()
    
>>> a = df.sentiment_type.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=['red','yellow','green'])
    
>>> a.show()
    
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.show()
AttributeError: 'AxesSubplot' object has no attribute 'show'
>>> plt.show()
    
>>> df.sentiment_type.value_counts().plot(kind='bar', autopct='%1.0f%%', colors=['red','yellow','green'])
    

Warning (from warnings module):
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_core.py", line 185
    warnings.warn(("'colors' is being deprecated. Please use 'color'"
UserWarning: 'colors' is being deprecated. Please use 'color'instead of 'colors'
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    df.sentiment_type.value_counts().plot(kind='bar', autopct='%1.0f%%', colors=['red','yellow','green'])
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_core.py", line 2739, in __call__
    **kwds)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_core.py", line 1995, in plot_series
    **kwds)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_core.py", line 1798, in _plot
    plot_obj.generate()
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_core.py", line 251, in generate
    self._make_plot()
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_core.py", line 1261, in _make_plot
    log=self.log, **kwds)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\plotting\_core.py", line 1205, in _plot
    return ax.bar(x, y, w, bottom=start, log=log, **kwds)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2298, in bar
    r.update(kwargs)
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\artist.py", line 916, in update
    ret = [_update_property(self, k, v) for k, v in props.items()]
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\artist.py", line 916, in <listcomp>
    ret = [_update_property(self, k, v) for k, v in props.items()]
  File "C:\Users\srini\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\artist.py", line 912, in _update_property
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property autopct
>>> plt.show()
    
>>> df.sentiment_type.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=['red','yellow','green'])
    
<matplotlib.axes._subplots.AxesSubplot object at 0x11971C50>
>>> plt.show()
