from datetime import datetime
import random

from airflow import DAG

from airflow.operators.bash import BashOperator

from airflow.operators.python_operator import PythonOperator

def hello():
    print("Airflow")
    
def ran():
    val1 = random.randint(0,100)
    val2 = random.randint(0,100)

    print(f'primera value: {val1}, segunda value: {val2}')
    
     
    file_path = "/var/tmp"
    
    

    # c. Запись сгенерированных чисел в файл
    with open(file_path +'/name.txt', "a+") as f:
        lines = f.readlines()
        
        f.truncate()

        f.write(f'{val1} {val2}\n')
    
def summ():
    file_path = "/var/tmp"
    with open(file_path +'/name.txt', 'r+') as f:
        sum_col1 = 0
        sum_col2 = 0
        for line in f:
            col1, col2 = map(int, line.split())
            sum_col1 += col1
            sum_col2 += col2
            diff = sum_col1 - sum_col2
        f.write(f'\n{diff}')
    
   
# A DAG represents a workflow, a collection of tasks

with DAG(dag_id="first_dag", start_date=datetime(2023, 3, 19), schedule="0,5,10 * * * *") as dag:
    
    # Task are represented as operators
    
    bash_task = BashOperator(task_id="Hello", bash_command="echo hello")
    
    python_task = PythonOperator(task_id="world", python_callable = hello)
    
    python_random = PythonOperator(task_id="random", python_callable = ran)
    
    python_summ = PythonOperator(task_id="summ", python_callable = summ)
    
    #Set dependencies between task_id
    
    bash_task >> python_task >> python_random >> python_summ