from backtester.features.feature import Feature
import math


class ExpMovingAverageFeature(Feature):

    @classmethod
    def computeForInstrument(cls, updateNum, time, featureParams, featureKey, instrumentManager):
        instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()
        data = instrumentLookbackData.getFeatureDf(featureKey)
        if len(data.index) >= 1:
            prev_ema = data.iloc[-1]
        else:
            prev_ema = instrumentLookbackData.getFeatureDf(featureParams['featureName']).iloc[-1]
        halflife = featureParams['period']
        alpha = 1 - math.exp(math.log(0.5) / halflife)
        avg = instrumentLookbackData.getFeatureDf(featureParams['featureName']).iloc[-1] * alpha + prev_ema * (1 - alpha)
        return avg

    @classmethod
    def computeForMarket(cls, updateNum, time, featureParams, featureKey, currentMarketFeatures, instrumentManager):
        lookbackDataDf = instrumentManager.getDataDf()
        data = lookbackDataDf[featureKey]
        if len(data.index) > 1:
            prev_ema = data[-2]
        else:
            prev_ema = lookbackDataDf[featureParams['featureName']].iloc[-1]
        halflife = featureParams['period']
        alpha = 1 - math.exp(math.log(0.5) / halflife)
        avg = lookbackDataDf[featureParams['featureName']].iloc[-1] * alpha + prev_ema * (1 - alpha)
        return avg

    @classmethod
    def computeForInstrumentData(cls, updateNum, featureParams, featureKey, featureManager):
        data = featureManager.getFeatureDf(featureParams['featureName'])
        if data is None:
            logWarn("[%d] instrument data for \"%s\" is not available, can't calculate \"%s\"" % (updateNum, featureParams['featureName'], featureKey))
            return None
<<<<<<< HEAD
        halflife = featureParams['period']
        expMovingAvg = data.ewm(halflife=halflife, adjust=False).mean()
=======
        movingAvg = data.rolling(window=featureParams['period'], min_periods=1).mean()
        expMovingAvg
>>>>>>> rebase with vn_training_model_manager
        return expMovingAvg
