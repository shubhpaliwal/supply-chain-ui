import sys
import json
import subprocess
import os
from subprocess import call
import subprocess

def main(databricks_instance, databricks_token, scopename):
    clusters_name = "test"
    holtwinter = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.4.x-conda-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,

            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/holtwinter_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/3. Holt-Winter",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }

    arima = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.2.x-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,

            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/arima_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/1. ARIMA",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }

    prophet = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.4.x-conda-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,
            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/prophet_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/2. Prophet",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }

    lstm = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.4.x-conda-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,
            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/lstm_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/4. LSTM",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }

    xgboost = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.4.x-conda-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,
            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/xgboost_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/5. XgBoost",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }

    operational_research = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.4.x-conda-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,
            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/or_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/6. OR",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }
    
    os = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.4.x-conda-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,
            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/or_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/7. OS",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }

    timefence = {
        "name": "SparkPi Python job",
        "new_cluster": {
            "name": clusters_name,
            "spark_version": "5.4.x-conda-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "num_workers": 1,
            "init_scripts": [
                {
                    "dbfs": {
                        "destination": "dbfs:/databricks/init/" + clusters_name + "/or_installation.sh"
                    }
                }
            ]
        },
        "notebook_task": {
            "notebook_path": "/Supply-Chain-Solution/8. Timefence",
            "base_parameters": {           
            "scope": scopename
            
        }
        }
    }

    print(databricks_instance, databricks_token)

    with open('arima.json', 'w') as fp:
        json.dump(arima, fp)

    with open('holtwinter.json', 'w') as fp:
        json.dump(holtwinter, fp)

    with open('prophet.json', 'w') as fp:
        json.dump(prophet, fp)

    with open('xgboost.json', 'w') as fp:
        json.dump(xgboost, fp)

    with open('lstm.json', 'w') as fp:
        json.dump(lstm, fp)

    with open('or.json', 'w') as fp:
        json.dump(operational_research, fp)
        
    with open('os.json', 'w') as fp:
        json.dump(os, fp)
    
    with open('timefence.json', 'w') as fp:
        json.dump(timefence, fp)

    subprocess.getoutput("bash /home/site/wwwroot/azure_blob_app/databricks_linux/main.sh {} {} {}".format(databricks_instance,databricks_token,clusters_name))
    #call(['bash',os.path.join(os.getcwd(),'azure_blob_app/databricks_linux/main.sh'), databricks_instance,
    #          databricks_token,
    #         clusters_name])
    # os.system("bash /home/site/wwwroot/azure_blob_app/databricks_linux/main.sh {} {} {}".format(databricks_instance,
    #                                                                                             databricks_token,
    #                                                                                             clusters_name))



