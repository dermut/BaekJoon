from pytz import timezone
from datetime import datetime

UTC = datetime.now(timezone('UTC'))

print(UTC.date())