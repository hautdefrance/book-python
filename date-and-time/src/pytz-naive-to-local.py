from datetime import datetime
from pytz import timezone


warsaw = timezone('Europe/Warsaw')
bajkonur = timezone('Asia/Almaty')

gagarin = datetime(1961, 4, 12, 14, 7)  # timezone naive


bajkonur.localize(gagarin)
# datetime.datetime(1961, 4, 12, 14, 7,
#                   tzinfo=<DstTzInfo 'Asia/Almaty' +06+6:00:00 STD>)
