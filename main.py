# main.py
import mlflow

def workflow():
  with mlflow.start_run() as active_run:

    print("Launching 'step1'")
    step1_run = mlflow.run(".", "step1", parameters={})
    step1_run = mlflow.tracking.MlflowClient().get_run(step1_run.run_id)

    print("Launching 'step2'")
    step2_run = mlflow.run(".", "step2", parameters={})
    step2_run = mlflow.tracking.MlflowClient().get_run(step2_run.run_id)

if __name__ == '__main__':
    workflow()