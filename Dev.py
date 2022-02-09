from azureml.core import Workspace
from azureml.core import Model
from azureml.train.automl.run import AutoMLRun
from azureml.core import Workspace, Experiment

#Connect to wrokspace and Experiment again
ws = Workspace('8c96f3ed-e53f-4400-a002-420605371b18','Azure_Project','FRT_Project')
experiment_name = 'automl_loan_approval_prediction'
experiment =  Experiment(ws, experiment_name)

run_id = 'AutoML_9301b394-5cc4-49a7-beee-c3f879f52408'
run_id = "AutoML_9301b394-5cc4-49a7-beee-c3f879f52408"
remote_run = AutoMLRun(experiment,run_id)

best_run , fitted_model = remote_run.get_output()
model_name = best_run.properties["model_name"]
endpoint_name = "Loan-App-ep"

ws=Workspace.from_config()
model=Model(ws,name=model_name)

service = Model.deploy(ws,endpoint_name,[model])
service.wait_for_deployement(show_output=True)
