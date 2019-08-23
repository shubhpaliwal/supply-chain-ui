#!/bin/bash
echo "prateek";
apt-get -y install git;
pip3 install wheel;
pip3 install databricks-cli;
apt-get -y install expect;
apt-get -y install jq ;
git clone https://github.com/Prateekagarwal9/supplychain-new;
echo Celebal;
expect /home/site/wwwroot/azure_blob_app/databricks_linux/creds.sh $1 $2;
# sudo databricks workspace import  -f DBC -l SCALA supplychain/ARIMA.dbc /ARIMA;
# sudo databricks workspace import  -f DBC -l SCALA supplychain/Prophet.dbc /Prophet;
# sudo databricks workspace import  -f DBC -l SCALA supplychain/Holt-Winter /Holt-Winter;
databricks workspace import  -f DBC -l SCALA /home/site/wwwroot/supplychain-new/Supply-Chain-Solution.dbc /Supply-Chain-Solution;
databricks fs mkdirs dbfs:/databricks/init/$3/;
databricks fs cp /home/site/wwwroot/azure_blob_app/databricks_linux/arima_installation.sh dbfs:/databricks/init/$3/;
databricks fs cp /home/site/wwwroot/azure_blob_app/databricks_linux/prophet_installation.sh dbfs:/databricks/init/$3/;
databricks fs cp /home/site/wwwroot/azure_blob_app/databricks_linux/holtwinter_installation.sh dbfs:/databricks/init/$3/;
databricks fs cp /home/site/wwwroot/azure_blob_app/databricks_linux/lstm_installation.sh dbfs:/databricks/init/$3/;
databricks fs cp /home/site/wwwroot/azure_blob_app/databricks_linux/xgboost_installation.sh dbfs:/databricks/init/$3/;
databricks fs cp /home/site/wwwroot/azure_blob_app/databricks_linux/or_installation.sh dbfs:/databricks/init/$3/;

runid=$(databricks jobs create --json-file arima.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;

runid=$(databricks jobs create --json-file prophet.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;


runid=$(databricks jobs create --json-file holtwinter.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;

runid=$(databricks jobs create --json-file xgboost.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;

runid=$(databricks jobs create --json-file lstm.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;

runid=$(databricks jobs create --json-file or.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;

runid=$(databricks jobs create --json-file os.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;

runid=$(databricks jobs create --json-file timefence.json);
echo $runid;
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew;
databricks jobs run-now --job-id $runidnew;



#sudo databricks libraries install --maven-coordinates "com.microsoft.azure:azure-eventhubs-spark_2.11:2.3.10" --cluster-id $runidnew
