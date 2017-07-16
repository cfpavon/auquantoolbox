# **Available Features**

Features can be called by specifying config dictionaries. Create one dictionary per feature and return them in a dictionary as market features or instrument features.

Feature config Dictionary has the following keys:
  > *featureId:* a string representing the type of feature you want to use  
  > *featureKey:* {optional} a string representing the key you will use to access the value of this feature  
  >            If not present, will just use featureId  
  > *params:* {optional} A dictionary with which contains other optional params if needed by the feature 
  
Feature ID  | Parameters | Description
:-------------: | ------------- | -------------  
*moving_average*  | 'featureName', 'period' |
*moving_sdev*  | 'featureName', 'period' |
*exponential_moving_average*  | 'featureName', 'period' |
*momentum*  | 'featureName', 'period' |
*bollinger_bands*  | 'featureName', 'period' |
*macd*  | 'featureName', 'period1', 'period2' |
*ratio*  | 'featureName', 'instrumentId1', 'instrumentId2' |
*rsi*  | 'featureName', 'period' |
*vwap*  | - |
*fees*   | 'feesDict', 'price' |
*position*  | - |
*pnl*  | 'fees', 'price' |
*capital*  | 'initial_capital', 'price' |
*portfolio_value*  | 'initial_capital', 'pnl' |