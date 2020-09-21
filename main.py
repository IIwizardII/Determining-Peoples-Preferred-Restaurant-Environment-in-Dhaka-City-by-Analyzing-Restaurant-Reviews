from CleanData import ReadData
from AddFeatures import Attributes
from SeparateReviewType import SeparateData
from AvgAndMedian import CalcAvgAndMedian

# objectCleanData = ReadData()
# objectCleanData.loadDataAndClean()

# objectAddFeatures = Attributes()
# objectAddFeatures.addAttribute()

# objectSeparateData = SeparateData()
# objectSeparateData.dataSeparator()

objectAvgAndMedian = CalcAvgAndMedian()
# objectAvgAndMedian.calcAvgRatingAndChar()
objectAvgAndMedian.calcMedianReviewChar()
