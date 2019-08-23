import os
databricksname="https://eastus.azuredatabricks.net/"
accesstoken="dapi57165fafe83f953de44e61ad26da1fcf"
os.system("python3 databricks_linux/test324.py {} {}".format(databricksname, accesstoken))
