# Using Start date and End date
import pandas as pd
start_date = '2024-01-01'
end_date = '2024-12-31'
date_index = pd.date_range(start=start_date, end=end_date)
print(date_index)
# Using Start date and Periods
import pandas as pd
start_date = '2024-01-01'
periods = 365  # for a full year
date_index = pd.date_range(start=start_date, periods=periods)
print(date-index)
#Using End dates and Periods
import pandas as pd
end_date = '2024-12-31'
periods = 365  # for a full year
date_index = pd.date_range(end=end_date, periods=periods)
print(date_index)
#Using Frequency
import pandas as pd
start_date = '2024-01-01'
end_date = '2024-12-31'
date_index = pd.date_range(start=start_date, end=end_date, freq='D') # 'D'Generates dates on daily basis
print(date_index)
