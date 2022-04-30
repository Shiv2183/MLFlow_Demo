import mlflow

def task():
  with mlflow.start_run() as mlrun:
    # logic of the step goes here
    print('Step2 executed')

if __name__ == '__main__':
    task()