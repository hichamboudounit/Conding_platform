import pandas as pd

title = title.rename(columns={"worker_ref_id":"worker_id"})
workertitle = worker.merge(title, on='worker_id', how='left')

workertitle[(workertitle.salary == workertitle['salary'].max())]['worker_title'].tolist()