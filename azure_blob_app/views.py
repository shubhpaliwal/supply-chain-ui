from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from .deployer_file import Deployer
from azure.storage.blob import BlockBlobService
import json
from collections import defaultdict
from .logging_file import get_logger
import random
from supplychain.settings import BASE_DIR
import os
from .models import RandomId
from .django_forms import UserDetails_Form
from .databricks_linux import test324
from threading import Thread


def execute_all_func(form_data):
    logger = get_logger()
    error_flag = False
    try:
        appservicename = form_data["appservicename"]  # should display 'bar' # response to your request.
        appurl = form_data["appserviceurl"]
        datafactoryname = form_data["datafactoryname"]
        accountname = form_data["storageaccountname"]
        accesskey = form_data["accesskey"].replace(" ", "+")
        # sql credentials
        connectstring = form_data["storageconnectionstring"].replace(" ", "+")
        servername = form_data["sqlservername"]
        sqlusername = form_data["sqlserverusername"]
        sqlpass = form_data["sqlserverpassword"]
        sqlcon = form_data["sqlserverconnectionstring"]
        dbname = form_data["sqlserverdatabasename"]
        databricksname = form_data["databricksname"]
        accesstoken = form_data["accesstoken"]
        workspaceurl = form_data["databricksworkspaceurl"]
        databricksscope = form_data["databricksscope"]
        powerbiname = form_data["powerbiembedded"]
        powerbiadmin = form_data["powerbiadmin"]
        keyvaultname = form_data["keyvaultname"]
        subid = form_data["subscriptionid"]
        tenid = form_data["subscriptiontenantid"]
        clientid = form_data["subscriptionclientid"]
        clientsecret = form_data["subscriptionclientsecret"]
        resourcegroup = form_data["subscriptopnresourcegroup"]
        rglocation = form_data["resourcegrouplocation"]
        dflocation = form_data["datafactorylocation"]
        azurefunction = form_data["azurefunctionurl"]
        keyvaultlocation = form_data["keyvaultlocation"]
        rglocation = form_data["resourcegrouplocation"]
        sources = form_data["datafactorysources"]
        # bq project data
        bqproject = form_data["bgprojectname"]
        bqclient = form_data["bqclientid"]
        bqsecret = form_data["bqclientsecret"]
        bqtoken = form_data["bqtoken"]
        bqschema = form_data["bgtableschema"]
        bqtables = form_data["bgtablevalues"]
        # oracle data  oracleservername
        oracleport = form_data["oracleport"]
        oraclesid = form_data["oraclesid"]
        oracleuser = form_data["oracleuser"]
        oraclepassword = form_data["oraclepassword"]
        oracleschema = form_data["oracleschema"]
        oracletable = form_data["oracletables"]
        # sap data
        sapserver = form_data["sapservername"]
        sapusername = form_data["sapusername"]
        sappassword = form_data["sappassword"]
        saptable = form_data["saptables"]
        sapschema = form_data["sapschema"]
        # salesforce data
        salesforceuser = form_data["salesforceusername"]
        salesforcepass = form_data["salesforcepassword"]
        salesforcetoken = form_data["salesforcetoken"]
        salesforceschema = form_data["salesforceschema"]
        salesforcetables = form_data["salesforcetables"]
        datablob = form_data["testblobname"]
        print(datablob)
        resource_group = resourcegroup
        subscription_id = subid
        azure_client_id = clientid
        azure_client_secret = clientsecret
        azure_tenant_id = tenid
        li_salesforce = list()
        li_sap = list()

        if len(salesforceuser) > 0:
            schema_list = salesforceschema.split(",")
            table_list = salesforcetables.split(",")
            li_salesforce = [{"objects_label": schema_list[i], "objects_name": table_list[i]} for i in
                             range(0, len(schema_list))]
        elif len(sapserver) > 0:
            schema_list = sapschema.split(",")
            table_list = saptable.split(",")
            li_sap = [{"table_schema": schema_list[i], "table_name": table_list[i]} for i in
                      range(len(schema_list))]

        dic = dict()
        dic['$schema'] = 'https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#'
        dic['contentVersion'] = '1.0.0.0'
        dic['parameters'] = defaultdict(dict)
        dic['parameters']['DataFactoryName']['value'] = datafactoryname
        dic['parameters']['DataFactoryLocation']['value'] = dflocation
        dic['parameters']['StorageConnectionString']['value'] = connectstring
        dic['parameters']['SQLConnectionString']['value'] = sqlcon
        dic['parameters']['AzureFunctionURL']['value'] = azurefunction
        dic['parameters']['Sources']['value'] = sources
        dic['parameters']['BlobTable']['value'] = datablob
        if len(li_salesforce) != 0:
            dic['parameters']['SalesForceUsername']['value'] = salesforceuser
            dic['parameters']['SalesForcePassword']['value'] = salesforcepass
            dic['parameters']['SalesForceToken']['value'] = salesforcetoken
            dic['parameters']['SalesForceTables']['value'] = li_salesforce
        if len(li_sap) != 0:
            dic['parameters']['SAPServer']['value'] = sapserver
            dic['parameters']['SAPUsername']['value'] = sapusername
            dic['parameters']['SAPPassword']['value'] = sappassword
            dic['parameters']['SAPTables']['value'] = li_sap

        for key, value in dic['parameters'].items():
            if value['value'] == None:
                del dic['parameters'][key]

        with open(os.path.join(BASE_DIR, "ADFParameters.json"), "w") as f:
            f.write(json.dumps(dic))

        # new file

        dic2 = dict()
        dic2['$schema'] = 'https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#'
        dic2['contentVersion'] = '1.0.0.0'
        dic2['parameters'] = defaultdict(dict)
        dic2['parameters']['SubscriptionID']['value'] = str(subid)
        dic2['parameters']['TenantID']['value'] = tenid
        dic2['parameters']['ClientID']['value'] = clientid
        dic2['parameters']['CientSecret']['value'] = clientsecret
        dic2['parameters']['DataFactoryName']['value'] = datafactoryname
        dic2['parameters']['StorageAccountName']['value'] = accountname
        dic2['parameters']['StorageAccessKey']['value'] = accesskey
        dic2['parameters']['StorageConnectionString']['value'] = connectstring
        dic2['parameters']['SQLServerName']['value'] = servername
        dic2['parameters']['SQLUsername']['value'] = sqlusername
        dic2['parameters']['SQLPassword']['value'] = sqlpass
        dic2['parameters']['SQLConnectionString']['value'] = sqlcon
        dic2['parameters']['SQLDatabaseName']['value'] = dbname
        dic2['parameters']['DatabricksName']['value'] = databricksname
        dic2['parameters']['DataBricksWorkspaceURL']['value'] = workspaceurl
        dic2['parameters']['DataBricksScope']['value'] = databricksscope
        dic2['parameters']['DataBricksToken']['value'] = accesstoken
        dic2['parameters']['PowerBIEmbeddedName']['value'] = powerbiname
        dic2['parameters']['PowerBIEmbeddedAdmin']['value'] = powerbiadmin
        dic2['parameters']['AppServiceName']['value'] = appservicename
        dic2['parameters']['AppServiceURL']['value'] = appurl
        dic2['parameters']['AzureFunctionURL']['value'] = azurefunction
        dic2['parameters']['KeyVaultName']['value'] = keyvaultname
        dic2['parameters']['KeyVaultLocation']['value'] = keyvaultlocation
        dic2['parameters']['ResourceGroupName']['value'] = resourcegroup
        dic2['parameters']['ResourceGroupLocation']['value'] = rglocation
        
        test324.main(workspaceurl, accesstoken, databricksscope)

        #os.system("python3 /home/site/wwwroot/azure_blob_app/databricks_linux/test324.py {} {}".format(workspaceurl, accesstoken))

        with open(os.path.join(BASE_DIR, "KeyVaultParameters.json"), "w") as f:
            f.write(json.dumps(dic2))

        container_name = 'marketplacecodes'
        blob_name = 'ADFParameters.json'
        blob_client = BlockBlobService(connection_string=connectstring)
        resp = blob_client.create_blob_from_path(container_name=container_name, blob_name=blob_name,
                                                 file_path=os.path.join(BASE_DIR, "ADFParameters.json"))
        blob_name = 'KeyVaultParameters.json'
        resp = blob_client.create_blob_from_path(container_name=container_name, blob_name=blob_name,
                                                 file_path=os.path.join(BASE_DIR, "KeyVaultParameters.json"))
        obj = Deployer(resource_group, subscription_id, azure_client_id, azure_client_secret, azure_tenant_id)
        print(obj.deploy("DataFactoryDeployment.json", "ADFParameters.json", connectstring))
        print(obj.deploy("KeyVaultDeployment.json", "KeyVaultParameters.json", connectstring))
    except KeyError as k:
        logger.error(str(k))
        error_flag = True
    except Exception as e:
        logger.error(str(e))
        error_flag = True
    return


def index(request):
    logger = get_logger()
    error = False
    try:
        if str(request.method).lower() == 'post':
            form = UserDetails_Form(request.POST)
            if form.is_valid():
                form_data = dict(form.data.items())
                thread_var = Thread(target=execute_all_func,args=(form_data,))
                thread_var.start()
    except Exception as e:
        logger.error(str(e))
    form = UserDetails_Form()
    content = {'form': form, 'error': error}
    return render(request, "index.html", content)


# Create your views here.
class FirstTrail(APIView):
    logger = get_logger()

    def get(self, request):
        while True:
            random_no = "".join([str(random.randint(0, 9)) for i in range(0, 9)])
            random_obj = RandomId.objects.filter(random_id=random_no)
            if random_obj.exists():
                continue
            else:
                random_obj = RandomId()
                random_obj.random_id = random_no
                random_obj.save()
                return JsonResponse({"output": random_no})
