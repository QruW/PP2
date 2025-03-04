from datetime import datetime, timedelta

today = datetime.now()

fivedaysago = today - timedelta(days=5)

print(fivedaysago)